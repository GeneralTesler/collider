from collider.languages.c.sourcefile import SourceFile
from collider.compiler.compileropts import CompileOptions
from collider.compiler.windows.gcc import GCC
from collider.languages.c.messagebox import Messagebox

if __name__ == "__main__":
    source = SourceFile(
        options=CompileOptions(options=["-shared"], extension=".dll"),
    ).add_to_source(Messagebox())
    source.save_to_disk()

    dst_path = GCC().compile_source(source=source)

    print(f"Src::{source.src_path}\nDst::{dst_path}")
