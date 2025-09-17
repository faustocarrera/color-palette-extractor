Color pallete extractor
=======================

A Python script that analyzes images to extract dominant colors and generates beautiful color palettes for design and creative projects.

## Features

- Extract dominant colors from any image format (PNG, JPG, JPEG)
- Command-line interface for easy automation

## Installation

### Prerequisites

Make sure you have Python 3.7 or higher installed on your system.

### Required Dependencies

```bash
pip install -r requirements.txt
```

### requirements.txt
```
Pillow>=7
click>=7.0
pandas>1.0
```

## Basic Usage

```bash
python color_extractor.py input_image.jpg
python color_extractor.py images/
```

## Output

The script generates several output files:

### Color Data Files

- `palette_[image_name].txt`: List of colors in hex format
- `palette_[image_name].json`: JSON format with additional color information
- `palette_[image_name].png`: Visual color palette with swatches

### Example Output Format

**HEX Format:**

```
#FF6B6B
#4ECDC4
#45B7D1
#96CEB4
#FFEAA7
```

**JSON Format:**

```json
{
  "colors": [
    "#FF6B6B",
    "#175459",
    "#175459",
    "#14272e",
    "#192e31",
    "#175459",
    "#f8cb32"
  ],
  "total_colors": 64,
  "image_info": {
    "filename": "sunset.jpg",
    "processed_date": "2025-09-15T10:30:00"
  }
}
```

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.
