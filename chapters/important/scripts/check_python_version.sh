#!/bin/sh
ver=$(python -V 2>&1 | sed 's/.* \([0-9]\).\([0-9]\).*/\1\2/')
echo $ver
if [ "$ver" -eq "36" ]; then
    poetry run python -m pip install dataclasses
fi