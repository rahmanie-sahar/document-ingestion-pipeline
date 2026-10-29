from src.base import BaseDocumentLoader
from src.processor import Processor


class DocumentPipeline:
    def __init__( self, loader, processor):
        self.loader = loader
        self.processor = processor 

    def run(self) -> list[str]:
        raw_text = self.loader.load()

        cleaned_text = self.processor.clean_text(raw_text)

  
        chunks = self.processor.chunk_text(cleaned_text)

        return chunks