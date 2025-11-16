@echo off
REM The Planters House - Booking Confirmation Transformer
REM Windows batch script with poppler PATH configured

REM Add poppler to PATH for this session
set PATH=%~dp0poppler\poppler-24.08.0\Library\bin;%PATH%

REM Run the transformation
python "%~dp0claude_transform.py" %*

REM Usage examples:
REM   run_transform.bat --input "path\to\cloudbeds.pdf"
REM   run_transform.bat --input "path\to\cloudbeds.pdf" --debug
