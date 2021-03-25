"""variable reading"""
# pylint: disable=import-error
from __future__ import annotations
import os
from set_dirs import get_xdg, read_config  # type: ignore

config_dirs = read_config.read_config()
xdg_dirs = get_xdg.get_dirs()
dirs: list[str] = []

for dir_num in enumerate(config_dirs):
    if not os.path.exists(config_dirs[dir_num]):
        # TODO should this create the dir instead?
        dirs.append(xdg_dirs[dir_num])
        continue
    dirs.append(config_dirs[dir_num])

del config_dirs, xdg_dirs
