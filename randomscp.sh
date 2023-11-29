#!/bin/bash
dir=$(dirname -- "$(readlink -f -- "${BASH_SOURCE[@]}")")
cd "$dir" || exit

source "$dir/scpbot-3.10/bin/activate"

if [ $# -eq 1 ]; then
    python "$dir/randomscp.py" "$1"
fi
