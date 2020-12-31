from pathlib import Path
import subprocess
from typing import Dict, List


cmd: str = "xdg-user-dir"
home: str = str(Path.home())
xdg_dirs: dict = {
    "Desktop": [cmd, "DESKTOP"],
    "Downloads": [cmd, "DOWNLOAD"],
    "Documents": [cmd, "DOCUMENTS"],
    "Music": [cmd, "MUSIC"],
    "Pictures": [cmd, "PICTURES"],
    "Videos": [cmd, "VIDEOS"],
}


def get_dirs(directories: Dict[str, List[str]]) -> List[str]:
    """iterate through directories to find and return as a list"""
    results: list = []
    for name, command in directories.items():
        try:
            directory = subprocess.run(
                command, capture_output=True, text=True
            ).stdout.strip("\n")
        except FileNotFoundError:
            directory = f"{home}/{name}"
        results.append(directory)
    return results


def main():
    """do the thing"""
    desktop, downloads, documents, music, pictures, videos = get_dirs(xdg_dirs)
    print(desktop, downloads, documents, music, pictures, videos)


if __name__ == "__main__":
    main()
