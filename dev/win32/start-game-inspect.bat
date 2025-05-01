@echo off

REM We setup our needed environment here.
call env.bat
call cta toontown

%PYTHON_EXE% -i -m toontown.toonbase.ToontownStart
pause