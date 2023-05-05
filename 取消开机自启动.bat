chcp 65001
@echo off
::获取管理员权限
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
::创建快捷方式
if exist "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\假期倒计时.lnk" (
  del /Q "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\假期倒计时.lnk"
) 
echo 自启动卸载成功！

choice /t 2 /d y /n >nul
 
 