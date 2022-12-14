REM We setup our needed enviorment here.
call env.bat
call cta toontown
cd ttotp

title Toontown [OTP Server]

%PYTHON_LOCATION%\python.exe -m py_otp
pause