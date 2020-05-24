from .base import WindowsCompiler


class Clang(WindowsCompiler):
    def __init__(self):
        """
        Clang/LLVM compiler

        x64/x86 binary should be the target rather than the compiler binary
        """
        super().__init__(x64bin="x86_64-pc-windows-gnu", x86bin="i686-pc-windows-gnu")
        self.cli = (
            self.cli
        ) = "clang {src_path} -o {dst_path} -target {compiler} {options}"
