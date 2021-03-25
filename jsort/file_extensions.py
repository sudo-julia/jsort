"""
dictionary of file extensions
"""
from __future__ import annotations

extensions: dict[str, list[str]] = {
    "archives": ["7z", "bz2", "gz", "rar", "tar", "xz", "zip", "zst", "zz"],
    "audio": ["aac", "aiff", "alac", "flac", "mp3", "ogg", "opus", "wav"],
    "books": ["azw", "epub", "fb2", "mobi"],
    "disks": ["img", "iso"],
    "documents": ["doc", "docx", "md", "odf", "pdf", "rtf", "tex", "txt", "wpd"],
    "images": ["gif", "jpeg", "jpg", "png", "raw", "tiff"],
    "videos": ["avi", "mkv", "mp4", "mpeg", "mpg", "wmv"],
}
