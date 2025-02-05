# XML to JSON Converter

## Overview
This project is designed to convert XML files into JSON format, with a primary focus on WordPress XML exports. However, it can also work with other XML structures. The conversion is handled using the `xmltodict` library, which allows easy transformation of XML into Python dictionaries.

## Technologies Used
- Python
- `xmltodict` ([GitHub Repository](https://github.com/martinblech/xmltodict))
- `json`
- `re` (for cleaning invalid characters)
- `os`

## How It Works
1. Place the XML files you want to convert inside the `Files` folder.
2. Run the script `ConvertXML.py`.
3. The converted JSON files will be saved in the `Convert` folder with the same filename as the original XML file.

## Installation & Usage
### Prerequisites
Ensure you have Python installed (version 3.x recommended). You also need to install the required dependencies:

```sh
pip install xmltodict
```

### Running the Script
```sh
python ConvertXML.py
```

## Example
### Input (`Files/sample.xml`)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <item>
      <title>Sample Post</title>
      <link>https://example.com/sample-post</link>
      <pubDate>Tue, 05 Feb 2025 12:00:00 +0000</pubDate>
      <content:encoded><![CDATA[<p>Sample post content.</p>]]></content:encoded>
    </item>
  </channel>
</rss>
```

### Output (`Convert/sample.json`)
```json
[
  {
    "title": "Sample Post",
    "link": "https://example.com/sample-post",
    "pubDate": "Tue, 05 Feb 2025 12:00:00 +0000",
    "content:encoded": "<p>Sample post content.</p>"
  }
]
```
