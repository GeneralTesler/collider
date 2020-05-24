from .base import WindowsCompiler


class GCC(WindowsCompiler):
    def __init__(self):
        """
        MinGW w64 GCC compiler
        """
        super().__init__(x64bin="x86_64-w64-mingw32-gcc", x86bin="i686-w64-mingw32-gcc")
