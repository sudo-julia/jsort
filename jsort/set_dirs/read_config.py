"""read the config.ini file.
if directories are set, override the defaults found by get_xdg
"""
from __future__ import annotations
import configparser
import os
import sys
from jsort.set_dirs.get_xdg import get_dirs


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


def read_config():
    """get options from config.ini"""
    config_file = f"{config_dir}/config.ini"
    config: configparser.ConfigParser = configparser.ConfigParser()
    if not os.path.exists(config_file):
        write_config(config_file)
    config.read(config_file)
