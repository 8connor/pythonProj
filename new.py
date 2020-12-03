import subprocess
import win32api
import win32com.client

shell = win32com.client.Dispatch("WScript.shell")

win32api.Sleep(5000)

for x in range(0, 2):
    shell.SendKeys("hello world")
    shell.SendKeys("{ENTER}")
print(x)
