from fastapi import APIRouter, UploadFile, File, HTTPException
import tempfile
import os

from src.api.validators import validate_file_type
from src.ocr.document_ocr import extract_text_from_document

router = APIRouter()


@router.post("/api/v1/analyze-document")
async def analyze_document(file: UploadFile | None = File(None)):
    if file is None:
        raise HTTPException(status_code=400, detail="FILE_REQUIRED")

    try:
        validate_file_type(file.filename)

        content = await file.read()

        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp:
            temp.write(content)
            temp_path = temp.name

        try:
            text = extract_text_from_document(temp_path)
        finally:
            os.unlink(temp_path)

        return {
            "text": text
        }

    except ValueError as error:
        if str(error) == "FILE_REQUIRED":
            raise HTTPException(status_code=400, detail="FILE_REQUIRED")

        if str(error) == "UNSUPPORTED_FILE_TYPE":
            raise HTTPException(status_code=400, detail="UNSUPPORTED_FILE_TYPE")

        raise HTTPException(status_code=500, detail="DOCUMENT_PROCESSING_FAILED")

    except ValueError as error:
        if str(error) == "FILE_REQUIRED":
            raise HTTPException(status_code=400, detail="FILE_REQUIRED")

        if str(error) == "UNSUPPORTED_FILE_TYPE":
            raise HTTPException(status_code=400, detail="UNSUPPORTED_FILE_TYPE")

        raise HTTPException(
            status_code=500,
            detail="DOCUMENT_PROCESSING_FAILED"
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="DOCUMENT_PROCESSING_FAILED"
        )