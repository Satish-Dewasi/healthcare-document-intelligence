import pymupdf
from src.ocr.image_ocr import extract_text_from_image


def extract_text_from_pdf(file_path: str) -> str:
    document = pymupdf.open(file_path)
    page_texts = []

    for page in document:
        pixmap = page.get_pixmap()
        image = pixmap.tobytes("png")

        temp_path = "/tmp/pdf_page.png"

        with open(temp_path, "wb") as file:
            file.write(image)

        page_texts.append(extract_text_from_image(temp_path))

    document.close()

    return "\n".join(page_texts).strip()