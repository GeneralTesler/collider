# Setup

*note: generation tested on Ubuntu 18.04 and payloads tested on Server 2016*

## Compilers

*only the tools you plan to use need to be installed*

- mingw64 for GCC compiler
    - http://mingw-w64.org/doku.php/download
- clang/llvm for Clang compiler
    - https://releases.llvm.org/download.html

## Post-processors

*only the tools you plan to use need to be installed*

- UPX
    - https://github.com/upx/upx/releases
- sRDI
    - > git submodule init && git submodule update
- Donut
    - pip install donut-shellcode 
    - note: included in requirements.txt

## Python 

- Python 3
- install requirements from requirements.txt
    - requirements-dev.txt is only for development purposes
