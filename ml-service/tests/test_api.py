from urllib import response

from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_file_required():
    response = client.post("/api/v1/analyze-document")

    assert response.status_code == 400
    assert response.json()["detail"] == "FILE_REQUIRED"


def test_unsupported_file_type():
    response = client.post(
        "/api/v1/analyze-document",
        files={"file": ("test.txt", b"hello", "text/plain")},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "UNSUPPORTED_FILE_TYPE"



def test_document_processing_failed(monkeypatch):
    def mock_ocr(file_path):
        raise RuntimeError("OCR failed")

    monkeypatch.setattr(
        "src.api.routes.extract_text_from_document",
        mock_ocr,
    )

    response = client.post(
        "/api/v1/analyze-document",
        files={"file": ("test.png", b"fake image", "image/png")},
    )

    assert response.status_code == 500
    assert response.json()["detail"] == "DOCUMENT_PROCESSING_FAILED"