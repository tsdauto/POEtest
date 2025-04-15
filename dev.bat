@echo off
setlocal enabledelayedexpansion

:: Step 1: Get timestamp
for /f "tokens=1-4 delims=/ " %%a in ("%date%") do (
    set MM=%%a
    set DD=%%b
    set YYYY=%%c
)
for /f "tokens=1-2 delims=:." %%a in ("%time%") do (
    set HH=%%a
    set MIN=%%b
)
if "!HH:~0,1!"==" " set HH=0!HH:~1,1!

:: Step 2: Get Git short commit hash
for /f %%i in ('git rev-parse --short HEAD') do set GIT_HASH=%%i

:: Step 3: Build report filename and folder
set TIMESTAMP=!YYYY!-!MM!-!DD!_!HH!!MIN!
set REPORT_NAME=report_!TIMESTAMP!_git-!GIT_HASH!.html
set REPORT_DIR=reports

:: Step 4: Ensure reports/ exists
if not exist "!REPORT_DIR!" (
    mkdir "!REPORT_DIR!"
)

:: Step 5: Run tests
poetry run pytest .

:: Step 6: Generate single-file Allure report
allure generate --single-file allure-results -o tmp-report

:: Step 7: Move HTML + launch report + serve live UI
if exist tmp-report\index.html (
    move tmp-report\index.html "!REPORT_DIR!\!REPORT_NAME!"
    rmdir /s /q tmp-report
    echo ✅ Static report saved as !REPORT_DIR!\!REPORT_NAME!
    start "" "!REPORT_DIR!\!REPORT_NAME!"

    echo 🌐 Launching interactive Allure web server...
    allure serve allure-results
) else (
    echo ⚠️ No HTML report generated. Skipping save/serve.
)

endlocal
