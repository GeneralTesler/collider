import donut
from collider.utils.shellcode import sc_to_hexstr


class DonutPostProcessor:
    @staticmethod
    def run(file, **kwargs) -> str:
        """
        Given a file on disk, convert it to shellcode using Donut
        :param file: compiled payload path
        :param kwargs: Donut arguments
        :return: shellcode as string os hex values (e.g. \x00)
        """
        # https://github.com/TheWover/donut/blob/master/docs/2019-08-21-Python_Extension.md#keywords
        return sc_to_hexstr(donut.create(file=file, **kwargs))
