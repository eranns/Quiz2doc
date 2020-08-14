from abc import ABC, abstractmethod


class AQuizScrapper(ABC):

    @abstractmethod
    def run(self):
        pass

    @property
    @abstractmethod
    def questions(self):
        pass

    @property
    @abstractmethod
    def quiz_title(self):
        pass
