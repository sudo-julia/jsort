"""read the config.ini file.
if directories are set, override the defaults found by get_xdg
"""
# pylint: disable=import-error
from __future__ import annotations
import configparser
import os
import sys
from get_xdg import get_dirs  # type: ignore


config_dir: str | None = os.environ.get("XDG_CONFIG_HOME")
if not config_dir:
    print("Variable $XDG_USER_HOME not set. Cannot find config file.")
    sys.exit(1)
config_dir = f"{config_dir}/jsort"


def write_config(config_file: str):
    """write the config file"""
    if not os.path.exists(config_dir):  # type: ignore
        os.makedirs(config_dir)  # type: ignore
    config: configparser.ConfigParser = configparser.ConfigParser()
    # pylint: disable=unbalanced-tuple-unpacking
    downloads, documents, music, pictures, videos = get_dirs()
    config["DIRECTORIES"] = {
        "Downloads": downloads,
        "Documents": documents,
        "Music": music,
        "Pictures": pictures,
        "Videos": videos,
    }
    with open(config_file, "w") as configfile:
        config.write(configfile)


def read_config() -> list[str]:
    """get options from config.ini"""
    config_file = f"{config_dir}/config.ini"
    config: configparser.ConfigParser = configparser.ConfigParser()
    if not os.path.exists(config_file):
        write_config(config_file)
    config.read(config_file)
    dirs: list[str] = []
    for dir_ in dict(config["DIRECTORIES"]).values():
        dirs.append(expand_tilde(dir_))
    return dirs


def expand_tilde(path: str) -> str:
    """expand the tilde to home path"""
    if path[0] == "~":
        path = os.path.expanduser(path)
    return path
