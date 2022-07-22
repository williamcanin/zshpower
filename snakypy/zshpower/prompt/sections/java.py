from subprocess import run

from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version, detect_eff


class Java(Version, Base):
    def __init__(self, *args):
        super(Java, self).__init__()
        self.args: tuple = args
        self.key = "java"
        self.app_executable = "java"
        self.shorten = "java-"
        # detect_e = detect_eff(self.args[0], self.key, "detect_extensions")
        # detect_fo = detect_eff(self.args[0], self.key, "detect_folders")
        # detect_fi = detect_eff(self.args[0], self.key, "detect_files")
        self.finder = {
            "extensions": [".java", ".class"],
            "folders": [],
            "files": [".java-version", "project.clj", "build.boot"],
        }

    def get_version(self, space_elem: str = " ") -> str:
        # args[0]: dict = config file (toml)
        # args[1]: dict = database registers
        return super().get(
            self.args[0], self.args[1], self.key, self.shorten, space_elem=space_elem
        )

    def set_version(self, action: str = "") -> bool:
        command = run(
            f"""{self.app_executable} -version 2>&1 | awk -F '"' '/version/ {{print $2}}'""",
            capture_output=True,
            shell=True,
            text=True,
        )
        version = command.stdout.replace("\n", "").split("_")[0]
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()
