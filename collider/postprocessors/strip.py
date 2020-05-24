from collider.utils.commands import run_command


class Strip:
    @staticmethod
    def run(path: str, options: list = None) -> None:
        """
        Calls "strip" on compiled payload
        :param path: compiled payload path
        :param options: command line arguments for strip
        """
        if options is None:
            options = ["-s"]

        args = ["strip"]
        args.extend(options)
        args.extend([path])

        run_command(args)
