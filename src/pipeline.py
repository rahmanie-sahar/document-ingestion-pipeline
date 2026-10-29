from examples.fetch_web_data import FetchWebData
from src.loader import TextLoader


fetch_web_data = FetchWebData()
file_path = fetch_web_data.fetch_text()
text_loader = TextLoader(file_path)
print(text_loader.load())
