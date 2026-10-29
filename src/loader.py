from src.base import BaseDocumentLoader

import json, csv


class TextLoader(BaseDocumentLoader):
    def load(self):
        with open(file=self.file_path, mode='r', encoding="utf-8") as file:
            self.raw_content = file.read()
        return self.raw_content
        
        
class JsonLoader(BaseDocumentLoader):
    def load(self):
        with open(file=self.file_path, mode='r',  encoding="utf-8") as file:
            self.raw_content = json.load(file)
        return json.dumps(self.raw_content, ensure_ascii=False, indent=2)
        

class CSVLoader(BaseDocumentLoader):
    def load(self):
        with open(file=self.file_path, mode='r',  encoding="utf-8", newline="") as csvfile:
            spamreader = csv.reader(csvfile)
            for line in spamreader:
                self.raw_content += ",".join(line) + "\n"
        return self.raw_content    


# text_path = "C:\\Users\\Beethovon\\Desktop\\Python_AmirHossein_Mentorship\\3.OOP_in_python\\DocumentIngestionPipeline\\examples\\data\\data.txt"
# json_path = "C:\\Users\\Beethovon\\Desktop\\Python_AmirHossein_Mentorship\\3.OOP_in_python\\DocumentIngestionPipeline\\examples\\data\\data.json"
# csv_path = "C:\\Users\\Beethovon\\Desktop\\Python_AmirHossein_Mentorship\\3.OOP_in_python\\DocumentIngestionPipeline\\examples\\data\\data.csv"

# if __name__ == "__main__":
#     textloader = TextLoader(text_path)
#     jsonloader = JsonLoader(json_path)
#     csvloader = CSVLoader(csv_path)
#     print((textloader.load()))
#     print((jsonloader.load()))
#     print((csvloader.load()))
