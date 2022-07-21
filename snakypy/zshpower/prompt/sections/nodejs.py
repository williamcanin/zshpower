from os import getcwd
from subprocess import run

from snakypy.zshpower import HOME
from snakypy.zshpower.config.base import Base
from snakypy.zshpower.prompt.sections.utils import Version, detect_eff
from snakypy.zshpower.utils.catch import get_key


class NodeJs(Version, Base):
    def __init__(self, *args):
        super(NodeJs, self).__init__()
        self.args: tuple = args
        self.key = "nodejs"
        self.version_in_home = get_key(self.args[0], self.key, "version", "in_home")
        self.app_executable = "node"
        self.shorten = "node-"
        detect_e = detect_eff(self.args[0], self.key, "detect_extensions")
        detect_fo = detect_eff(self.args[0], self.key, "detect_folders")
        detect_fi = detect_eff(self.args[0], self.key, "detect_files")
        self.finder = {
            "extensions": [".js"] + detect_e,
            "folders": ["node_modules"] + detect_fo,
            "files": ["package.json"] + detect_fi,
        }

    def get_version(self, space_elem: str = " ") -> str:
        if getcwd() == HOME and self.version_in_home is False:
            return ""
        # args[0]: dict = config file (toml)
        # args[1]: dict = database registers
        return super().get(
            self.args[0], self.args[1], self.key, self.shorten, space_elem=space_elem
        )

    def set_version(self, action: str = "") -> bool:
        command = run("node -v", capture_output=True, shell=True, text=True)
        version = command.stdout.replace("\n", "").split("v")[1]
        return super().set(
            command, version, self.app_executable, self.key, action=action
        )

    def __str__(self):
        return self.get_version()


# def _nodejs(config, key):
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         future = executor.submit(NodeJs().get_version, config, key)
#         return_value = future.result()
#         return return_value
