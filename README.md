# Journal Parser Application
  This application has an important role as a tool for students in class 12 in the first semester who are carrying out PKL. With its main feature called "parsing journal from WhatsApp zip file" students will be helped in writing activity journals required for school assessments, especially in terms of PKL assessments.

# Documentation 📖
## Get the app file via "dist" directory
1. Open branch main on the git repository

<p align="center">  
   <img src="https://github.com/user-attachments/assets/8472a294-c019-42a9-8c06-9fc75b49cc52" style="width:75%; height:auto;">
</p>

2. Click "dist" directory and download file .exe from them

<p align="center">  
   <img src="https://github.com/user-attachments/assets/22340b26-2484-41c8-a112-aec0c07b9ee0" style="width:75%; height:auto;">
</p>

<p align="center">  
   <img src="https://github.com/user-attachments/assets/65406e55-449f-4875-be88-538198ffdb3a" style="width:75%; height:auto;">
</p>

## Follow this solution if you find this problem while running .exe file

<p align="center">
  <img src="https://github.com/user-attachments/assets/d421926a-6e0a-483d-9dcb-8ef6b98aa883" style="width:70%; height:auto;">
</p>

Right-click the downloaded file in the specified download path.
choose "properties" option and checklist unblock checkbox at the bottom section. After that, click apply at the right bottom corner.

   <p align="center"> 
       <img src="https://github.com/user-attachments/assets/42ab77a9-e91a-4dcf-9a0c-19c959b1b8d7" style="width:70%; height:auto;">
   </p>


# The following is the display window when running the application 

  <p align="center"> 
      <img src="https://github.com/user-attachments/assets/1efa60c2-dc9a-41c7-aa37-f2f06919c664" style="width:70%; height:auto;">
  </p>

# Guide how to use the application
## Get the whatsapp chat file zip
Before download file chat from whatsapp application, there are several things you need to pay attention to first
- Messages from chat should have a format like this, (FYI: explanation of the details of the activities below is optional).
  <p align="center"> 
      <img src="https://github.com/user-attachments/assets/a4f1f36a-b2d9-4be9-b495-f543fc34479f" style="width:65%; height:auto;">
  </p>
  
  <p align="center"> 
      <img src="https://github.com/user-attachments/assets/5e589efd-cd15-48d1-9044-6744f37e7e45" style="width:65%; height:auto;">
  </p>

- And the next step, if you have formatted the message as per the guide above then download the chat file on WhatsApp.

1. Download chat file from WhatsApp Mobile.

  <p align="center"> 
      <img src="https://github.com/user-attachments/assets/f4e36b01-16f4-4a14-9d97-3718a6a64e83" style="width:65%; height:auto;">
  </p>

  - click other

  <p align="center"> 
      <img src="https://github.com/user-attachments/assets/eb4871c3-bdc3-4f6a-b731-fedb4b25eb2e" style="width:65%; height:auto;">
  </p>

  - and then "export chat"
    
    <p align="center"> 
      <img src="https://github.com/user-attachments/assets/bc4ae420-512c-45f7-a074-65ee4374461f" style="width:65%; height:auto;">
    </p>
    
  - click without media when export the chat
    
    <p align="center">
      <img src="https://github.com/user-attachments/assets/0a29ef30-330e-4cce-be0f-912c85aa3743" style="width:65%; height:auto;">
    </p>

  - send the export file to your personal number
      
    <p align="center"> 

      <img src="https://github.com/user-attachments/assets/902da787-ed91-44ce-9467-2ef71714e5e5" style="width:65%; height:auto;">
    </p>

  - Download the file from your whatsapp computer (or web) and upload the file in the app. Wait until the data is displayed in the window
  
    <p align="center"> 
      <img src="https://github.com/user-attachments/assets/72b8a920-33b3-40e8-a7e3-caa0ce5f5dac" style="width:65%; height:auto;">
    </p>


2. Export the data to excel file
   - give the file a name
   - wait until the success message appears in the window
   
    <p align="center"> 
      <img src="https://github.com/user-attachments/assets/27da5e6c-0b59-488f-8b25-a58fde92a1c7" style="width:65%; height:auto;">
    </p>

   - open the excel file, the export results display will look like the following image

    <p align="center">
      <img src="https://github.com/user-attachments/assets/6614d4e0-bb1f-463b-89fb-ea60616f44c0" style="width:65%; height:auto;">
    </p>


# For Your Information
  This application is open source to the public. Anyone can use it, please note that if you want to make changes or modify the source code, do it by forking the repository or by cloning the repository, because the source code in the repository is original. Never make direct changes to the original branch or change the name of the original branch, because it will damage the original version. Just fork this repository to make modifications or changes to the source code.

Warm greetings from FawzyCode as the author and developer of this application (●'◡'●)
   
## this is the main code of the program in the app.py file
  <p align="center">
      <img src="https://github.com/user-attachments/assets/a00c0c04-6b31-49f8-b780-1eb9faa43f27" style="width:65%; height:auto;">
  </p>

## if you want to create a modified application and build it
Use this command to create it
```
pyinstaller --onefile --noconsole --name "<NamaAplikasiBaru>" --icon=icon.png app.py
```
