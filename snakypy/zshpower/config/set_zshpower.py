from snakypy.zshpower.config import package

# author = package.info["author"]["name"]
# website_author = package.info["author"]["website"]
# email = package.info["author"]["email"]

content = f"""#!/usr/bin/env zsh

## Information:
## ******************************************************************************
## Theme: {package.info["name"]}
## Description: Call script to start {package.info["name"]}.
## ******************************************************************************

## Export PATH local user
export PATH="$PATH:$HOME/.local/bin"

function preexec() {{
  timer=$(date +%S)
}}

function precmd() {{
    if [ $timer ]; then
      now=$(date +%S)
      elapsed=$(($now-$timer))
      unset timer
    fi
}}

## Option using "add-zsh-hook"
function zshpower_precmd() {{
  state=$(which zshpower-draw > /dev/null 2>&1)
  if [ ! $? -ne 0 ]; then
    PROMPT="$(zshpower-draw prompt $elapsed)"
    RPROMPT="$(zshpower-draw rprompt)"
  else
    PROMPT='%F{{green}}%n%f@%F{{magenta}}%m%f %F{{blue}}%B%~%b%f %# '
    RPROMPT='[%F{{yellow}}%?%f]'
  fi
}}

function install_zshpower_precmd() {{
  for s in "${{precmd_functions[@]}}"; do
    if [ "$s" = "zshpower_draw" ]; then
      return
    fi
  done
  precmd_functions+=(zshpower_precmd)
}}

## Option using "add-zsh-hook"
autoload -Uz add-zsh-hook
add-zsh-hook precmd zshpower_precmd

## Option not using "add-zsh-hook"
# if [ "$TERM" != "linux" ]; then
#    install_zshpower_precmd
# fi
"""
