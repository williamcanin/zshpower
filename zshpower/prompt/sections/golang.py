from subprocess import run
from zshpower.prompt.sections.lib.utils import Version


class Golang(Version):
    def __init__(self):
        super(Golang, self).__init__()
        self.extensions = (".go",)
        self.files = ("go.mod", "glide.yaml")
        self.folders = ("Godeps",)

    def get_version(self, config, reg_version, key="golang", ext="go-", space_elem=" "):
        return super().get(config, reg_version, key=key, ext=ext, space_elem=space_elem)

    def set_version(self, key="golang", action=None):
        version = run("go version", capture_output=True, shell=True, text=True)

        if not version.stderr.replace("\n", ""):
            version = version.stdout.replace("go", "").split(" ")[2]
            return super().set(version, key, action)

        return False
