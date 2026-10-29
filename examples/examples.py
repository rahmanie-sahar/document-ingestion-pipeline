
import os
from src.loader import CSVLoader, JsonLoader, TextLoader
from src.pipeline import DocumentPipeline
from src.processor import Processor

# مسیر فایل‌ها بر اساس ساختار پروژه
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

txt_path = os.path.join(DATA_DIR, "data.txt")
json_path = os.path.join(DATA_DIR, "data.json")
csv_path = os.path.join(DATA_DIR, "data.csv")

if __name__ == "__main__":
    # پردازشگر را با سایز چانک دلخواه می‌سازیم
    processor = Processor(chunk_size=150, chunk_overlap=30)

    # تست ۱: فایل متنی
    txt_pipeline = DocumentPipeline(
        loader=TextLoader(txt_path), processor=processor
    )
    txt_chunks = txt_pipeline.run()
    print(f"--- TXT Chunks ({len(txt_chunks)}) ---")
    for i, ch in enumerate(txt_chunks):
        print(f"Chunk {i+1}: {ch}")

    # تست ۲: فایل CSV
    csv_pipeline = DocumentPipeline(
        loader=CSVLoader(csv_path), processor=processor
    )
    csv_chunks = csv_pipeline.run()
    print(f"\n--- CSV Chunks ({len(csv_chunks)}) ---")
    print(f"First chunk of CSV: {csv_chunks[0]}")