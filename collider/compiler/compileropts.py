class UnknownExtensionException(Exception):
    """raised when an unkown extension is supplied for compilation"""


class CompileOptions:
    """
    CompilerOptions provide a class to manage arguments passed to a compiler
    """

    def __init__(
        self,
        options: list = [],
        arch: str = "x64",
        extension: str = ".exe",
        target: str = None,
    ):
        """
        :param options: list of options that will be passed through to the compiler
        :param arch: compilation architecture; defaults to x64
        :param extension: compiled output extension; either exe or dll
        :param target: output target for use by certain compilers like clang
        """
        if extension not in [".exe", ".dll"]:
            raise UnknownExtensionException(f"Extension {extension} unknown")

        self.options = options
        self.arch = arch
        self.extension = extension
        self.target = target  # used by clang
