from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version, detect_eff


class Crystal(Version, Base):
    def __init__(self, *args):
        super(Crystal, self).__init__()
        self.args: tuple = args
        self.key = "crystal"
        self.app_executable = "crystal"
        self.shorten = "cr-"
        # detect_e = detect_eff(self.args[0], self.key, "detect_extensions")
        # detect_fo = detect_eff(self.args[0], self.key, "detect_folders")
        # detect_fi = detect_eff(self.args[0], self.key, "detect_files")
        self.finder = {
            "extensions": [".cr"],
            "folders": [],
            "files": ["shard.yml"],
        }

    def get_version(self, space_elem: str = " ") -> str:
        # args[0]: dict = config file (toml)
        # args[1]: dict = database registers
        return super().get(
            self.args[0], self.args[1], self.key, self.shorten, space_elem=space_elem
        )

    def set_version(self, action: str = "") -> bool:
        command = run("crystal version", capture_output=True, shell=True, text=True)
        version = command.stdout.split()[1]
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()
