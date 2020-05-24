from collider.languages.c.sourcefile import SourceFile
import tempfile
import shlex
from collider.utils.commands import run_command


class WindowsCompiler:
    def __init__(self, x64bin, x86bin):
        """
        Creates a Windows-compatible compiler manager. Compiler binary should be in $PATH
        :param x64bin: compiler for x64 output
        :param x86bin: compiler for x86 output
        """
        self.x64bin = x64bin
        self.x86bin = x86bin

        self.cli = "{compiler} {src_path} -o {dst_path} {options}"

    def compile_source(self, source: SourceFile) -> str:
        """
        Compiles the source code
        :param source: SourceFile object
        :return: path to compile output
        """
        dst_path = tempfile.mkstemp(suffix=source.options.extension)[1]
        compiler = self.x64bin if source.options.arch == "x64" else self.x86bin

        args = self.cli.format(
            compiler=compiler,
            src_path=source.src_path,
            dst_path=dst_path,
            options=" ".join(source.options.options),
        )
        args = shlex.split(args)

        run_command(args)

        return dst_path
