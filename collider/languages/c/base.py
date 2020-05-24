import jinja2


class CLangBase:
    """
    Used to manage C language source code that can be added to a C SourceFile

    Each class that extends this is expected to provide 5 pieces of information:
    1. a friendly name for the code (e.g. messagebox); this should be the same name as the template file
    2. a Jinja2 template containing the templatized source code
    3. a list of any imports used by the code
    4. a method property that returns the rendered template
    5. an invocation that specifies how to call the rendered method from the main method (e.g. foo(abc);)

    When a child class is added to a SourceFile via add_to_source, the imports are added to the import list,
    the methods are appended to the overall source, and the invocation is added to main

    Function names should be globally unique
    """

    def __init__(self):
        self.imports = []
        self.name = ""

    @property
    def invocation(self):
        pass

    @property
    def method(self):
        pass

    @property
    def template(self):
        loader = jinja2.PackageLoader(
            package_name="collider.languages.c", package_path="templates"
        )
        env = jinja2.Environment(loader=loader)
        return env.get_template(f"{self.name}.c.j2")
