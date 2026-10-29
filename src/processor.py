import re

class Processor:
    def __init__(self, chunk_size: int=500, chunk_overlap: int = 50):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def clean_text(self, text:str):
        if not isinstance(text, str):
            text = str(text)

        cleaned = (re.sub(f'/s+', ' ', text)).strip()
        return cleaned 

    def chunk_text(self, text) :
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        if self.chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")

        if not 0 <= self.chunk_overlap < self.chunk_size:
            raise ValueError("chunk_overlap must be between 0 and chunk_size - 1")

        chunks = []
        start = 0

        while start < len(text):
            end = start + self.chunk_size
            chunks.append(text[start:end])

            if end >= len(text):
                break

            # החלק הזה מהچانک قبلی دوباره در چانک بعدی قرار می‌گیرد
            start = end - self.chunk_overlap

        return chunks

from src.loader import TextLoader, JsonLoader, CSVLoader

text_path = "C:\\Users\\Beethovon\\Desktop\\Python_AmirHossein_Mentorship\\3.OOP_in_python\\DocumentIngestionPipeline\\examples\\data\\data.txt"
json_path = "C:\\Users\\Beethovon\\Desktop\\Python_AmirHossein_Mentorship\\3.OOP_in_python\\DocumentIngestionPipeline\\examples\\data\\data.json"
csv_path = "C:\\Users\\Beethovon\\Desktop\\Python_AmirHossein_Mentorship\\3.OOP_in_python\\DocumentIngestionPipeline\\examples\\data\\data.csv"

textloader = TextLoader(text_path)
jsonloader = JsonLoader(json_path)
csvloader = CSVLoader(csv_path)

processor = Processor(500,50)
text_cleaned = processor.clean_text(textloader)

if __name__ == "__main__":

    print(text_cleaned)
    #print((jsonloader.load()))
    #print((csvloader.load()))