from .base import CLangBase


class LocalAdmin(CLangBase):
    """
    Creates a new user then adds them to the local administrator group
    """

    def __init__(self, username, password):
        super().__init__()
        self.name = "local_admin"

        self.imports.extend(
            ["#include <windows.h>", "#include <lmaccess.h>", "#include <lmerr.h>"]
        )
        self.username = username
        self.password = password

    @property
    def invocation(self):
        return "newla_user();\nnewla_group();"

    @property
    def method(self):
        return self.template.render(username=self.username, password=self.password)
