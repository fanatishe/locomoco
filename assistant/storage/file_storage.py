from pathlib import Path
import pickle

from .base import StorageStrategy


class FileStorage(StorageStrategy):
    def __init__(self, filename: str | Path):
        self.filename = Path(filename)

    def save(self, data: dict) -> None:
        with open(self.filename, "wb") as file:
            pickle.dump(data, file)

    def load(self) -> dict:
        if not self.filename.exists():
            return {}

        with open(self.filename, "rb") as file:
            return pickle.load(file)
