from abc import ABC, abstractmethod


class AbstractModel(ABC):

    @abstractmethod
    def train(self, path):
        pass

    @abstractmethod
    def evaluate(self):
        pass
