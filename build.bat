@echo off
echo Installing required packages...
pip install cx_Freeze pandas openpyxl pillow

echo Creating executable...
python setup.py build

echo Build complete!
pause