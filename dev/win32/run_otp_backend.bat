title Toontown [OTP Server]
:: cd into root
cd ../../../
call env.bat
call cta toontown
cd ttotp
:main
%PYTHON_LOCATION%\python.exe -m py_otp
goto main
