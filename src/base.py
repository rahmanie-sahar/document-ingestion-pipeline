from abc import ABC, abstractmethod

class BaseDocumentLoader(ABC):
    def __init__(self, file_path):
        self.file_path = file_path
        self.raw_content = ""

    @abstractmethod
    def load(self):
        pass

    def __repr__(self):
        return f'<{self.__class__.__name__}(file_path= {self.file_path})>'