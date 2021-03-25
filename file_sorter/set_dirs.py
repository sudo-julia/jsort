"""
map out the locations of all XDG_DIRS defined by 'xdg-user-dir'
"""
from __future__ import annotations
from pathlib import Path
import subprocess


# pylint: disable=unbalanced-tuple-unpacking
cmd: str = "xdg-user-dir"
home: str = str(Path.home())
xdg_dirs: dict[str, list[str]] = {
    "Desktop": [cmd, "DESKTOP"],
    "Downloads": [cmd, "DOWNLOAD"],
    "Documents": [cmd, "DOCUMENTS"],
    "Music": [cmd, "MUSIC"],
    "Pictures": [cmd, "PICTURES"],
    "Videos": [cmd, "VIDEOS"],
}


def get_dirs(directories: dict[str, list[str]]) -> list[str]:
    """iterate through directories to find and return as a list
    returns in the order of: desktop, downloads, documents, music, pictures, videos
    """
    results: list = []
    for name, command in directories.items():
        try:
            directory = subprocess.run(
                command,
                capture_output=True,
                check=True,
                text=True,
            ).stdout.strip("\n")
        except FileNotFoundError:
            directory: str = f"{home}/{name}"
        results.append(directory)
    return results


def main():
    """test that the xdg_dirs are set properly"""
    desktop, downloads, documents, music, pictures, videos = get_dirs(xdg_dirs)
    print(desktop, downloads, documents, music, pictures, videos)


if __name__ == "__main__":
    main()
