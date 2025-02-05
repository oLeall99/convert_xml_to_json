import json
import xmltodict
import re
import os
from html import unescape

def clean_xml_content(xml_content):
    """
    Remove invalid characters that may cause XML parsing errors.
    Replaces invisible ASCII control characters with spaces.
    """
    xml_content = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]', '', xml_content)
    xml_content = xml_content.replace("&nbsp;", " ")
    xml_content = xml_content.replace("\ufeff", "")
    return xml_content

def parse_wordpress_xml(xml_file):
    """
    Parses a WordPress XML export file and extracts posts.
    """
    with open(xml_file, 'r', encoding='utf-8') as file:
        xml_content = file.read()
    
    cleaned_xml = clean_xml_content(xml_content)
    parsed_data = xmltodict.parse(cleaned_xml)
    
    # Adjust path according to WordPress structure
    posts = parsed_data.get("rss", {}).get("channel", {}).get("item", [])
    
    return posts

def write_to_json(posts, output_file):
    with open(output_file, 'w', encoding="utf-8") as json_file:
        json.dump(posts, json_file, indent=2, ensure_ascii=False)

def process_all_xml_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".xml"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name.replace(".xml", ".json"))
            
            parsed_posts = parse_wordpress_xml(input_path)
            write_to_json(parsed_posts, output_path)
            print(f"Conversion completed. Posts saved to: {output_path}")

if __name__ == "__main__":
    input_folder = "Files"
    output_folder = "Convert"
    process_all_xml_files(input_folder, output_folder)
