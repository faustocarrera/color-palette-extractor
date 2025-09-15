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
webcolors>=1.12
```

## Basic Usage

```bash
python color_extractor.py input_image.jpg
```

## Output

The script generates several output files:

### Color Data Files

- `[image_name]_palette.txt`: List of colors in hex format
- `[image_name]_palette.json`: JSON format with additional color information
- `[image_name]_palette.png`: Visual color palette with swatches

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
    {
      "hex": "#FF6B6B",
      "percentage": 23.5
    }
  ],
  "total_colors": 100,
  "image_info": {
    "filename": "sunset.jpg",
    "dimensions": [1920, 1080],
    "processed_date": "2025-09-15T10:30:00"
  }
}
```

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details.
