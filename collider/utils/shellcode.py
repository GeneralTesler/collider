def sc_to_hexstr(shellcode) -> str:
    """
    Convert binary shellcode to a hex string (e.g. \x00)
    :param shellcode: shellcode
    :return: shellcode as hex string
    """
    # https://github.com/byt3bl33d3r/SILENTTRINITY/blob/master/silenttrinity/core/utils.py -> shellcode_to_hex_string
    byte_array = []
    shellcode_hex = shellcode.hex()
    for i in range(0, len(shellcode_hex), 2):
        byte = shellcode_hex[i : i + 2]
        byte_array.append(f"\\x{byte.upper()}")

    return "".join(byte_array)


def hexstr_to_sc_arr(shellcode: str, delimter: str = "\\x") -> list:
    """
    Decodes a hex shellcode string (e.g. \\x00\\x00) to a list
    :param shellcode: shellcode
    :param delimter: delimeter user to split string
    :return: list of int values
    """
    return [int(dec, 16) for dec in shellcode.split(delimter) if len(dec) == 2]


def hexstr_to_sc_file(path: str, **kwargs) -> None:
    """
    Calls hexstr_to_sc_arr on shellcode then writes to a file
    :param path: location to save output
    :param kwargs: options to pass to hexstr_to_sc_arr
    """
    sc = bytearray(hexstr_to_sc_arr(**kwargs))

    with open(path, "wb") as f:
        f.write(sc)


def xor(data: bytearray, key: str) -> bytes:
    """
    XORs a bytearray using a string key
    https://github.com/Arno0x/ShellcodeWrapper/blob/master/shellcode_encoder.py -> xor
    :param data: bytearry of data (e.g. shellcode
    :param key: key as string
    :return: bytes
    """
    key_len = len(key)
    key_int = list(map(ord, key))
    return bytes(
        bytearray(((data[i] ^ key_int[i % key_len]) for i in range(0, len(data))))
    )
