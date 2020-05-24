import tempfile
from collider.compiler.compileropts import CompileOptions
from .base import CLangBase


class SourceFile:
    """
    Used to house one or more CLangBase source code objects

    Most methods return the object to support method chaining
    """

    def __init__(self, options: CompileOptions, extension=".c", entry="main"):
        """
        :param options: CompileOptions object
        :param extension: the extension to use when saving the source to disk
        :param entry: the name of entry method; leave as "main" unless required to change (e.g. wmain for unicode)
        """
        self.imports = ["#include <windows.h>"]
        self.methods = []
        self.main = []

        self.options = options
        self.entry = entry

        self.src_path = tempfile.mkstemp(suffix=extension)[1]

    def add_to_source(self, snippet_class: CLangBase) -> "SourceFile":
        """
        Adds a source code object to the manager
        :param snippet_class: CLangBase opject
        :return: this SourceFile object
        """
        self.imports.extend(snippet_class.imports)
        self.methods.append(snippet_class.method)
        self.main.append(snippet_class.invocation)

        return self

    def render(self) -> str:
        """
        Converts the contained source code to an actual file on disk.

        If the compiler options are set to use a dll, will create a DllMain method that calls the entry method
        :return: generated source code
        """
        src = ""

        for i in self.imports:
            src += i + "\n"

        for m in self.methods:
            src += m

        src += "void {0}(){{\n".format(self.entry)
        for m in self.main:
            src += m + "\n"
        src += "}\n"

        if self.options.extension == ".dll":
            src += """
            BOOL APIENTRY DllMain(HMODULE hModule, DWORD ul_reason_for_call, LPVOID lol){{
                switch (ul_reason_for_call){{
                    case DLL_PROCESS_ATTACH:
                        {entry}();
                        break;
                    case DLL_THREAD_ATTACH:
                        break;
                    case DLL_THREAD_DETACH:
                        break;
                    case DLL_PROCESS_DETACH:
                        break;
                }}
                return TRUE;
            }}\n""".format(
                entry=self.entry
            )

        return "\n".join([line.strip() for line in src.splitlines()])

    def save_to_disk(self):
        """
        Renders the source then saves it to disk
        :return: this SourceFile object
        """
        with open(self.src_path, "w") as f:
            f.write(self.render())

        return self
