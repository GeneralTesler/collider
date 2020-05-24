from .base import CLangBase


class VACPExec(CLangBase):
    """
    Uses VirtualAlloc + memcpy to allocate shellcode then executes
        https://ired.team/offensive-security/code-injection-process-injection/process-injection
    """

    def __init__(self, shellcode: str):
        super().__init__()
        self.name = "va_cp_exec"

        self.shellcode = shellcode

    @property
    def invocation(self):
        return "vacpe();"

    @property
    def method(self):
        return self.template.render(shellcode=self.shellcode)
