ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png"}


def validate_file_type(filename: str) -> None:
    if not filename:
        raise ValueError("FILE_REQUIRED")

    extension = filename.lower().rsplit(".", 1)[-1]

    if f".{extension}" not in ALLOWED_EXTENSIONS:
        raise ValueError("UNSUPPORTED_FILE_TYPE")