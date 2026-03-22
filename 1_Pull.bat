@echo off
echo Pulling Inventory from Git

git fetch --all

git reset --hard origin/main
echo.
pause