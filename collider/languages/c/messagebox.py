from .base import CLangBase


class Messagebox(CLangBase):
    """
    Shows a hello world message box
    """

    def __init__(self):
        super().__init__()
        self.name = "messagebox"

    @property
    def invocation(self):
        return "messagebox();"

    @property
    def method(self):
        return self.template.render()
