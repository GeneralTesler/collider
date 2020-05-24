import unittest
import os
import tempfile
from collider.utils.shellcode import *
from collider.utils.commands import *


class TestShellcodeUtils(unittest.TestCase):
    def test_sc_to_hexstr(self):
        # char "a" -> hex 61
        self.assertEqual(sc_to_hexstr(b"a"), "\\x61")

    def test_hexstr_to_sc_arr(self):
        # hex 61 -> dec 97
        self.assertEqual(hexstr_to_sc_arr("\\x61"), [97])
        self.assertEqual(hexstr_to_sc_arr("0x61", "0x"), [97])

    def test_xor(self):
        # "a" ^ "a" = 0
        x1 = xor(bytearray([97]), key="a")
        self.assertEqual(x1, b"\x00")

        x2 = xor(bytearray([97, 97]), key="a")
        self.assertEqual(x2, b"\x00\x00")


class TestCommandUtils(unittest.TestCase):
    def test_run_command_noenv(self):
        # test without setting "COLLIDER_ENV" env var
        if "COLLIDER_ENV" in os.environ:
            del os.environ["COLLIDER_ENV"]
        self.assertEqual(run_command(["hostname"]), None)

    def test_run_command_env(self):
        # test after setting "COLLIDER_ENV" to path then call bin not in path
        orig_env = dict(os.environ)  # https://stackoverflow.com/a/13143076
        envfile = mk_collider_env(path="/usr/bin")

        with self.assertRaises(FileNotFoundError) as ctx:
            run_command(["hostname"])

        os.remove(envfile)
        os.environ = orig_env


def mk_collider_env(path: str):
    envfile = tempfile.mkstemp()[1]
    with open(envfile, "w") as f:
        f.write(f"PATH={path}")
    os.environ["COLLIDER_ENV"] = envfile
    return envfile


if __name__ == "__main__":
    unittest.main()
