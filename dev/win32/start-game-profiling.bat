@echo off

REM We setup our needed environment here.
call env.bat
call cta toontown

%PYTHON_EXE% -i -m cProfile -o game_profile.dat -m toontown.toonbase.ToontownStart
pause
%PYTHON_EXE% -m snakeviz game_profile.dat