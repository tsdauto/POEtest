@echo off
setlocal enabledelayedexpansion

:: Step 1: Timestamp
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
if "!MIN:~0,1!"==" " set MIN=0!MIN:~1,1!

:: Step 2: Git hash
set GIT_HASH=nogit
for /f %%i in ('git rev-parse --short HEAD 2^>nul') do set GIT_HASH=%%i

:: Step 3: Report naming
set TIMESTAMP=!YYYY!-!MM!-!DD!_!HH!!MIN!
set REPORT_NAME=report_!TIMESTAMP!_git-!GIT_HASH!.html
set REPORT_DIR=reports

if not exist "!REPORT_DIR!" mkdir "!REPORT_DIR!"

:: Step 4: Run tests
echo 🧪 Running tests...
poetry run pytest --alluredir=allure-results .

:: Step 5: Generate single HTML report
echo 📄 Generating single-file Allure report...
call allure generate --single-file allure-results -o tmp-report --clean

:: Step 6: Move report and clean up
if exist ".\tmp-report\index.html" (
    move /Y ".\tmp-report\index.html" "!REPORT_DIR!\!REPORT_NAME!"
    rmdir /s /q tmp-report
    echo ✅ Report saved to !REPORT_DIR!\!REPORT_NAME!

    :: Directly open the HTML report in browser
    start "" "!REPORT_DIR!\!REPORT_NAME!"
) else (
    echo ⚠️ No HTML report generated.
)

:: Step 7: Optionally serve the report (skip allure-results cleanup)
echo 🌐 Optionally Starting live server...
call allure serve allure-results

endlocal
