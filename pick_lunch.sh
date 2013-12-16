#!/usr/bin/env bash

set -eu

if [[ $# != 1 ]]; then
    echo "usage: $0 <conf-directory>"
    exit 1
fi

confdir=$1

python pick_lunch.py $confdir/{places.conf,history.conf,*.prefs}

