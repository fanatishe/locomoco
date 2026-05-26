from pathlib import Path

from .base import StorageStrategy


class FileStorage(StorageStrategy):
    def __init__(self, filename: str | Path):
        self.filename = Path(filename)

    def save(self, data: dict) -> None:
        ...

    def load(self) -> dict:
        ...
