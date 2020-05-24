import subprocess
from collider.config.env import get_env


def run_command(args: list) -> None:
    """
    Thin wrapper around subprocess.run that adds the COLLIDER_ENV to the command
    :param args: full command line as list
    """
    try:
        # TODO: logger
        subprocess.run(
            args,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            env=get_env(),
        )
    except subprocess.CalledProcessError as e:
        print(e.stdout)
        pass
