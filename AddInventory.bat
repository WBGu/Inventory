@echo off
echo Running inventory update script...

REM Run the Python script (change 'update_inventory.py' to your actual script name)
python addToInventory.py

REM Check if the Python script succeeded before running Git commands
if %errorlevel% neq 0 (
    echo.
    echo Python script encountered an error. Stopping Git sync.
    pause
    exit /b %errorlevel%
)

echo.
echo Python script finished successfully. Proceeding with Git operations...
echo.

REM Add all changes (both the updated JSON and the cleared CSV)
git add .

REM Commit the changes with an automated timestamp message
git commit -m "Automated inventory update: %date% %time%"

REM Push the changes to your remote repository
git push

echo.
echo Inventory update and Git sync complete! (100%)
pause