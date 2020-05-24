from collider.utils.commands import run_command


class UPX:
    @staticmethod
    def run(path: str, options: list = None) -> None:
        """
        Calls UPX on compiled payload
        :param path: compiled payload path
        :param options: command line arguments for UPX
        """
        if options is None:
            options = []

        args = ["upx"]
        args.extend(options)
        args.extend([path])

        run_command(args)
