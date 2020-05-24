from sRDI.Python.ShellcodeRDI import *
from collider.utils.shellcode import sc_to_hexstr


class sRDI:
    @staticmethod
    def run(dll_path: str, **kwargs) -> str:
        """
        Given a DLL on disk, convert it to shellcode using sRDI
        :param dll_path: dll path
        :param kwargs: sRDI arguments
        :return: shellcode as string os hex values (e.g. \x00)
        """
        with open(dll_path, "rb") as f:
            dll = f.read()

        return sc_to_hexstr(ConvertToShellcode(dll, **kwargs))
