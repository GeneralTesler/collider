from collider.languages.c.sourcefile import SourceFile

from collider.compiler.compileropts import CompileOptions
from collider.compiler.windows.gcc import GCC

from collider.languages.c.messagebox import Messagebox
from collider.languages.c.va_cp_exec import VACPExec

from collider.postprocessors.srdi import sRDI
from collider.postprocessors.strip import Strip
from collider.postprocessors.upx import UPX


if __name__ == "__main__":
    source1 = SourceFile(
        options=CompileOptions(options=["-shared"], extension=".dll"),
    ).add_to_source(Messagebox())
    source1.save_to_disk()

    dll = GCC().compile_source(source=source1)

    sc = sRDI.run(dll_path=dll)

    source2 = SourceFile(options=CompileOptions(options=["-s"]),).add_to_source(
        VACPExec(shellcode=sc)
    )
    source2.save_to_disk()

    exe = GCC().compile_source(source=source2)

    Strip.run(exe)
    UPX.run(exe)

    print(
        f"DLL Src::{source1.src_path}\nDLL::{dll}\n\nExe Src::{source2.src_path}\nExe::{exe}"
    )
