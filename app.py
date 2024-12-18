import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime
import pandas as pd
import zipfile
import re
import os
import locale
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set locale untuk format tanggal Indonesia
try:
    locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'id_ID')
    except locale.Error:
        logger.warning("Tidak dapat mengatur locale Indonesia. Menggunakan locale default.")

class JournalParser:
    def __init__(self):
        self.df = None
        self.setup_gui()
        
    def parse_whatsapp_chat(self, chat_text):
        data = []
        # Pattern yang lebih fleksibel untuk menangkap format jurnal
        journal_pattern = r'(\d{1,2}/\d{1,2}/\d{2,4}),?\s*(\d{1,2}[:\.]\d{2})(?:\s*[AP]M)?\s*-\s*(.*?):\s*(?:Nama\s*:?\s*)(.*?)[\n\r]+(?:Jurnal\s*:?\s*)(.*?)[\n\r]+((?:(?!\d{1,2}/\d{1,2}/\d{2}).)*)'
        
        matches = re.finditer(journal_pattern, chat_text, re.DOTALL | re.IGNORECASE)
        
        for match in matches:
            try:
                date_str, time_str, sender, name, journal_date, activities = match.groups()
                
                # Normalisasi format tanggal
                date_parts = date_str.split('/')
                if len(date_parts[2]) == 2:
                    date_parts[2] = '20' + date_parts[2]
                date_str = '/'.join(date_parts)
                
                # Konversi tanggal dan waktu
                date_obj = datetime.strptime(date_str, "%d/%m/%Y")
                
                # Handle both . and : in time format
                time_str = time_str.replace('.', ':')
                time_obj = datetime.strptime(time_str, "%H:%M").time()
                
                # Bersihkan dan format tanggal jurnal
                journal_date = journal_date.strip()
                formatted_journal_date = journal_date  # Default value jika semua parsing gagal
                
                # Daftar format tanggal yang mungkin
                date_formats = [
                    "%A, %d %B %Y",
                    "%A,%d %B %Y",
                    "%A, %d-%B-%Y",
                    "%d %B %Y",
                    "%d-%B-%Y",
                    "%A, %d %b %Y",
                    "%d %b %Y",
                    "%Y-%m-%d",
                    "%d/%m/%Y"
                ]
                
                # Coba parse dengan berbagai format
                for date_format in date_formats:
                    try:
                        journal_date_obj = datetime.strptime(journal_date, date_format)
                        formatted_journal_date = journal_date_obj.strftime("%A, %d %B %Y")
                        logger.info(f"Berhasil parsing tanggal jurnal: {journal_date} dengan format {date_format}")
                        break
                    except ValueError:
                        continue
                
                # Jika semua format gagal, gunakan string asli
                if formatted_journal_date == journal_date:
                    logger.warning(f"Tidak dapat mem-parsing tanggal jurnal: {journal_date}")
                
                # Bersihkan dan format aktivitas
                activities = activities.strip()
                activity_list = [line.strip() for line in activities.split('\n') if line.strip()]
                formatted_activities = "\n".join([f"{i+1}. {activity}" for i, activity in enumerate(activity_list)])
                
                entry_data = {
                    "No": len(data) + 1,
                    "Nama": name.strip(),
                    "Tanggal Input": date_obj.strftime("%d/%m/%Y"),
                    "Waktu Input": time_obj.strftime("%H:%M"),
                    "Tanggal Jurnal": formatted_journal_date,
                    "Kegiatan": formatted_activities
                }
                
                logger.info(f"Berhasil memproses entri untuk {name.strip()}")
                data.append(entry_data)
                
            except Exception as e:
                logger.error(f"Error processing entry: {str(e)}")
                logger.error(f"Raw match: {match.groups()}")
                continue
        
        if not data:
            raise Exception("Tidak ada data yang berhasil diparsing dari file")
            
        return pd.DataFrame(data)

    def process_zip_file(self, zip_path):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                txt_files = [f for f in zip_ref.namelist() if f.endswith('.txt')]
                if not txt_files:
                    raise Exception("Tidak ditemukan file text dalam ZIP")
                
                with zip_ref.open(txt_files[0]) as file:
                    chat_text = file.read().decode('utf-8')
                
                self.df = self.parse_whatsapp_chat(chat_text)
                return True
        except Exception as e:
            logger.error(f"Error processing ZIP file: {str(e)}")
            messagebox.showerror("Error", f"Error memproses file ZIP: {str(e)}")
            return False

    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("Journal Parser")
        self.root.geometry("1200x800")

        # Style
        style = ttk.Style()
        style.theme_use('clam')

        # Custom colors for modern look
        style.configure("TButton", font=("Helvetica", 12), background="#0078D7", foreground="#FFFFFF")
        style.map("TButton", background=[("active", "#005A9E")])
        style.configure("TLabel", font=("Helvetica", 12), background="#F3F3F3", foreground="#333333")
        style.configure("TFrame", background="#F3F3F3")
        style.configure("Treeview", font=("Helvetica", 11), rowheight=25)
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), background="#E1E1E1", foreground="#333333")

        # Frame utama
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(0, 10))

        # Upload button
        upload_btn = ttk.Button(button_frame, text="Upload WhatsApp ZIP", command=self.upload_file)
        upload_btn.pack(side=tk.LEFT, padx=5)

        # Export button
        self.export_btn = ttk.Button(button_frame, text="Export ke Excel", command=self.export_to_excel, state=tk.DISABLED)
        self.export_btn.pack(side=tk.LEFT, padx=5)

        # Preview frame dengan scrollbar
        preview_frame = ttk.Frame(main_frame)
        preview_frame.pack(fill=tk.BOTH, expand=True)

        # Scrollbars
        y_scrollbar = ttk.Scrollbar(preview_frame)
        y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        x_scrollbar = ttk.Scrollbar(preview_frame, orient=tk.HORIZONTAL)
        x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Treeview untuk preview data
        self.tree = ttk.Treeview(preview_frame, yscrollcommand=y_scrollbar.set, xscrollcommand=x_scrollbar.set)
        self.tree.pack(fill=tk.BOTH, expand=True)

        y_scrollbar.config(command=self.tree.yview)
        x_scrollbar.config(command=self.tree.xview)

        # Status bar
        self.status_var = tk.StringVar()
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.root.mainloop()

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("ZIP Files", "*.zip")],
            title="Pilih file ZIP ekspor WhatsApp"
        )
        
        if file_path:
            self.status_var.set("Memproses file...")
            if self.process_zip_file(file_path):
                self.update_preview()
                self.export_btn.config(state=tk.NORMAL)
                self.status_var.set(f"File berhasil diproses: {os.path.basename(file_path)}")
            else:
                self.status_var.set("Gagal memproses file")

    def update_preview(self):
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Configure columns
        self.tree['columns'] = list(self.df.columns)
        self.tree['show'] = 'headings'
        
        # Set column headings
        for column in self.df.columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=150)  # Default width
        
        # Insert data
        for _, row in self.df.iterrows():
            self.tree.insert("", tk.END, values=list(row))
    
    def export_to_excel(self):
        if self.df is None:
            messagebox.showerror("Error", "Tidak ada data untuk diekspor")
            return
        
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel Files", "*.xlsx")],
            title="Simpan file Excel"
        )
        
        if file_path:
            try:
                self.df.to_excel(file_path, index=False, engine='openpyxl')
                messagebox.showinfo("Sukses", f"Data berhasil diekspor ke:\n{file_path}")
                self.status_var.set(f"File berhasil diekspor: {os.path.basename(file_path)}")
            except PermissionError:
                messagebox.showerror("Error", "Tidak dapat menulis ke file. Pastikan file tidak sedang dibuka di aplikasi lain.")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal mengekspor file: {str(e)}")
                self.status_var.set("Terjadi kesalahan saat mengekspor file")
                
if __name__ == "__main__":
    app = JournalParser()