from os import listdir, mkdir

if "raw_files" not in listdir():
    mkdir("raw_files")

from Akame.services.converter.converter import convert

__all__ = ["convert"]
