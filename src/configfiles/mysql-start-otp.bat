@echo off
title Toontown Online - MySQL OTP Server
cd otpgo

set DEBUG=Client
rem set DEBUG=*

:main
"../../../../OtpGo/otpgo" mysql_otp.yml
pause
goto :main
