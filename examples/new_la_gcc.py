from collider.languages.c.sourcefile import SourceFile
from collider.compiler.compileropts import CompileOptions
from collider.compiler.windows.gcc import GCC
from collider.languages.c.local_admin import LocalAdmin

if __name__ == "__main__":
    source = SourceFile(
        entry="wmain",
        options=CompileOptions(options=["-lnetapi32", "-municode"], arch="x86"),
    ).add_to_source(LocalAdmin(username="admin", password="Password123!",))
    source.save_to_disk()

    dst_path = GCC().compile_source(source=source)

    print(f"Src::{source.src_path}\nDst::{dst_path}")
