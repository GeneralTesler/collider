import os


# TODO: revisit
def get_env() -> dict:
    """
    If the COLLIDER_ENV environment variable is set, overrides the current PATH with the one set in COLLIDER_ENV

    COLLIDER_ENV is an environment variable that can be used to specify a path to an env file for use with this tool
    Currently, this function only looks for a PATH variable
        If one is found, it is used to override the current PATH
        If the found PATH contains a reference to the current PATH ($PATH), it will be replaced by the one found in
            os.environ

        Example:
            PATH=/bin
            COLLIDER_ENV PATH = /opt/tools:$PATH
            New PATH -> /opt/tools:/bin
    :return: dict of new env variables
    """
    env = dict(os.environ)

    if "COLLIDER_ENV" in env:
        collider_env = env["COLLIDER_ENV"]
        with open(collider_env) as f:
            # https://stackoverflow.com/a/60878313
            collider_dict = dict(
                tuple(line.strip().split("=")) for line in f.readlines()
            )

        if "PATH" in collider_dict:
            if "$PATH" in collider_dict["PATH"]:
                env["PATH"] = collider_dict["PATH"].replace("$PATH", env["PATH"])
            else:
                env["PATH"] = collider_dict["PATH"]

    return env
