from .base import CLangBase


class EarlybirdAPC(CLangBase):
    """
    Spawns a suspended process, allocates shellcode into process memory, then queues APC to execute
        https://ired.team/offensive-security/code-injection-process-injection/early-bird-apc-queue-code-injection
    """

    def __init__(
        self, shellcode: str, target_process: str = "C:\\Windows\\System32\\calc.exe"
    ):
        super().__init__()
        self.name = "earlybird_apc"

        self.shellcode = shellcode

        # escape backslashes
        if "\\\\" not in target_process:
            target_process = target_process.replace("\\", "\\\\")

        self.target_process = target_process

    @property
    def invocation(self):
        return "earlybird();"

    @property
    def method(self):
        return self.template.render(
            shellcode=self.shellcode, target_process=self.target_process
        )
