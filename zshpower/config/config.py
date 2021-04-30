from datetime import datetime
from zshpower import __version__


content = f"""# Generate by: ZSHPower - D{datetime.today().isoformat()}
# Version: {__version__}
# ---------------------------------------------------------------------
# For more information, see the documentation at:
# https://github.com/snakypy/zshpower#configuration-file

[general]
jump_line.enable = true
config.editor = "vim"
separator.element = "-"
separator.color = "white"
position = [
    "virtualenv",
    "python",
    "package",
    "nodejs",
    "rust",
    "golang",
    "java",
    "php",
    "ruby",
    "elixir",
    "julia",
    "dart",
    "dotnet",
    "docker",
    "perl",
    "scala",
    "git"
    ]

[username]
enable = false
symbol = "\\uf007"
color = "cyan"

[hostname]
enable = false
symbol = "\\ue0a2"
color = "magenta"
prefix.color = "white"
prefix.text = "at"

[directory]
truncation_length = 1
symbol = "\\ue5fe"
color = "cyan"
prefix.color = "white"
prefix.text = "in"

[git]
enable = true
symbol = "\\uf418"
branch.color = "cyan"
color.symbol = "magenta"
prefix.color = "white"
prefix.text = "on"

[git.status]
symbols.enable = true
symbol.clean = "\\uf62c"
symbol.added = "\\ufc03"
symbol.modified = "\\ufc07"
symbol.deleted = "\\ufbc7"
symbol.renamed = "\\uf101"
symbol.unmerged = "\\uf6fb"
symbol.untracked = "\\uf41e"
symbol.copied = "\\ufab1"
symbol.ahead = "\\uf55c"
symbol.behind = "\\uf544"
symbol.diverged = "\\ufb15"
symbol.conflicts = "\\uf0e7"

[command]
new_line.enable = true
symbol = "\\u276f"
color = "green"
error.symbol = "\\u276f"
error.color = "red"

[python]
symbol = "\\uf81f"
color = "yellow"
prefix.color = "white"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[package]
enable = false
symbol = "\\uf8d6"
color = "red"
prefix.color = "white"
prefix.text = "is"

[docker]
symbol = "\\uf308"
color = "cyan"
prefix.color = "white"
prefix.text = "on"
version.enable = false
version.micro.enable = true

[nodejs]
symbol = "\\uf898"
color = "green"
prefix.color = "white"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[rust]
symbol = "\\ue7a8"
color = "red"
prefix.color = "white"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[golang]
symbol = "\\ue627"
color = "cyan"
prefix.color = "white"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[php]
symbol = "\\ue608"
color = "magenta"
prefix.color = "white"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[dart]
symbol = "\\ue798"
color = "cyan"
prefix.color = "white"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[java]
symbol = "\\ue256"
color = "red"
prefix.color = "white"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[elixir]
symbol = "\\ue62d"
color = "blue"
prefix.color = "white"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[perl]
symbol = "\\ue769"
color = "blue"
prefix.color = "white"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[julia]
symbol = "\\ue624"
color = "blue"
prefix.color = "white"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[scala]
symbol = "\\ue737"
color = "red"
prefix.color = "white"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[dotnet]
symbol = "\\ue77f"
color = "cyan"
prefix.color = "white"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[ruby]
symbol = "\\ue21e"
color = "red"
prefix.color = "white"
prefix.text = "via"
version.enable = false
version.micro.enable = true

[virtualenv]
enable = false
symbol = "\\uf7c9"
involved = "()"
color = "yellow"
prefix.color = "white"
prefix.text = "via"

[virtualenv.name]
normal.enable = true
text = "venv"

[timer]
enable = false
symbol = "\\uf43a"
color = "blue"
seconds.enable = false
"""
