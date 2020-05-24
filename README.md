# Collider

Templatized payload generation

**this is an alpha - there are bound to be issues and breaking changes**

## What is it

Collider is a simple Python library for building payloads from scratch.
It allows the user to store code snippets as templates then expose them as Python classes.
These classes can be used to generate full payload source code then compile it. 
Collider also provides a mechanism for postprocessing using tools like [UPX](https://upx.github.io/) and [Donut](https://github.com/TheWover/donut).

Collider is designed to be easy to extend and relies mainly on external tools to do the heavy lifting rather 
than internalizing it (e.g. compilation is done by standard compilers like GCC and LLVM).

## Example

The following example demonstrates how to use Collider to create a exe to launch a message box

**Imports**

First import the required modules. 
Messagebox is the Python class for the message box source code.
SourceFile is the class used to house the code classes.
CompilerOptions and GCC are the classes used to manage the compiler. Currently, GCC and Clang are supported.

```python
from collider.languages.c.sourcefile import SourceFile
from collider.compiler.compileropts import CompileOptions
from collider.compiler.windows.gcc import GCC
from collider.languages.c.messagebox import Messagebox
```

**Source code & Compilation**

Next, create the source code for the message box and write it to disk.
CompileOptions can be used to specify things like output format and architecture as well as arbitrary compiler arguments.

```python
source = SourceFile(
    options=CompileOptions(options=["-s"]),
).add_to_source(Messagebox())

source.save_to_disk()
```

Then, cross compile the payload. The architecture defaults to x64 and the format defaults to exe.

```python
dst_path = GCC().compile_source(source=source)
print(dst_path)
```

For more examples, see the [**examples**](examples/) folder

## Included Templates (C)

Name|Description
--|--
messagebox|Hello world message box; mainly used for testing
va_cp_exec|Uses VirtualAlloc + memcp to allocate shellcode then execute it
va_cp_exec_xor|va_cp_exec + XOR'd shellcode
hc_ha_exec|HeapCreate + HeapAllocc + memcp to allocate shellcode then execute it
earlybird_apc|Early bird APC shellcode execution (Create suspended process -> VirtualAlloc + WriteProcessMemory -> QueueUserAPC)
local_admin|Create a new user then add them to the local admins group


## Additional Config

Collider supports the following configuration options

- COLLIDER_ENV environment variable: path to an env file (newline delimited list of KEY=VALUE) 
that will be added to the environment when running external commands. 
The main purpose of this is to allow for PATH overriding when running commands.
    - see [**collider/config/env.py**](collider/config/env.py) for more info
    - example env provided -> see [**env.sample**](env.sample)

## Changelog

- 5/24/2020 - Initial commit
