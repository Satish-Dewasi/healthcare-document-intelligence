from pathlib import Path

from src.ocr.image_ocr import extract_text_from_image
from src.ocr.pdf_ocr import extract_text_from_pdf


def extract_text_from_document(file_path: str) -> str:
    extension = Path(file_path).suffix.lower()

    if extension in {".jpg", ".jpeg", ".png"}:
        return extract_text_from_image(file_path)

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    raise ValueError("UNSUPPORTED_FILE_TYPE")