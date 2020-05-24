# Collider examples

Shellcode in examples generated using the following **msfvenom** commands

**x86**

> msfvenom -a x86 --platform windows -p windows/exec cmd=calc.exe -f c


**x64**: 

> msfvenom -a x64 --platform windows -p windows/x64/exec cmd=calc.exe -f c

