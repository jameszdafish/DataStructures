from abc import ABC, abstractmethod


class MyMap(ABC):
    @abstractmethod
    def put(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def contains_key(self):
        pass

    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass
