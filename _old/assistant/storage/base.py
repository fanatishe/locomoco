from abc import ABC, abstractmethod


class StorageStrategy(ABC):
    @abstractmethod
    def save(self, data: dict) -> None:
        """Save the address book data."""

    @abstractmethod
    def load(self) -> dict:
        """Return a dict {name: Record} of stored contacts."""
