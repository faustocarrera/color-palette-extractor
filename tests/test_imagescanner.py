import pytest
from pathlib import Path
from palettextract import ImageScanner


def test_init():
    "Start testing"
    scanner = ImageScanner()
    assert '.jpg' in scanner.supported_formats
    assert len(scanner.supported_formats) == 5


def test_invalid_path():
    "Test invalid path"
    scanner = ImageScanner()
    with pytest.raises(ValueError, match="Invalid path"):
        scanner.scan_directory(Path("nonexistent/path"))


def test_single_valid_image(tmp_path):
    "Test single image file"
    scanner = ImageScanner()
    image_file = tmp_path / "test.jpg"
    image_file.touch()

    result = scanner.scan_directory(image_file)
    assert len(result) == 1
    assert result[0] == image_file


def test_single_invalid_image(tmp_path):
    "Test single invalid image file"
    scanner = ImageScanner()
    invalid_file = tmp_path / "test.txt"
    invalid_file.touch()

    with pytest.raises(ValueError, match="Unsupported file format"):
        scanner.scan_directory(invalid_file)


def test_directory_with_images(tmp_path):
    "Test directory with mixed files"
    scanner = ImageScanner()
    # Create test files
    (tmp_path / "test1.jpg").touch()
    (tmp_path / "test2.png").touch()
    (tmp_path / "test3.txt").touch()

    result = scanner.scan_directory(tmp_path)
    assert len(result) == 2
    assert all(f.suffix.lower() in scanner.supported_formats for f in result)


def test_empty_directory(tmp_path):
    "Test empty directory"
    scanner = ImageScanner()
    result = scanner.scan_directory(tmp_path)
    assert len(result) == 0


def test_mixed_case_extensions(tmp_path):
    "Test files with mixed case extensions"
    scanner = ImageScanner()
    (tmp_path / "test1.JPG").touch()
    (tmp_path / "test2.jpg").touch()

    result = scanner.scan_directory(tmp_path)
    assert len(result) == 2  # Should find both files


def test_invalid_path_type(tmp_path):
    "Test path that's neither file nor directory"
    scanner = ImageScanner()
    special_path = tmp_path / "special"
    # Create a path that's neither file nor directory
    with pytest.raises(ValueError, match="Invalid path"):
        scanner.scan_directory(special_path)
