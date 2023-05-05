chcp 65001
@echo off
::获取管理员权限
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
::创建快捷方式
mshta VBScript:Execute("Set a=CreateObject(""WScript.Shell""):Set b=a.CreateShortcut(a.SpecialFolders(""AllUsersStartup"") & ""\假期倒计时.lnk""):b.TargetPath=""%~dp0假期倒计时.exe"":b.WorkingDirectory=""%~dp0"":b.Save:close")
echo 自启动安装成功！

choice /t 2 /d y /n >nul
 
 