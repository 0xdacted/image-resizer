import os
from PIL import Image, ImageFilter
from io import BytesIO
import requests

def adjust_aspect_ratio(url, output_path, aspect_ratio=(2, 3)):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    
    width, height = img.size
    new_height = int((width / aspect_ratio[0]) * aspect_ratio[1])
    
    if new_height > height:
        new_width = int((height / aspect_ratio[1]) * aspect_ratio[0])
        new_height = height
    else:
        new_width = width
    
    img = img.resize((new_width, new_height), Image.LANCZOS)
    
    if img.mode in ('RGBA', 'LA'):
        img = img.convert("RGB")
    
    img.save(output_path)
urls = [
]

for i, url in enumerate(urls, 1):
    file_name = url.split('/')[-1].split('.')[0] + '-adjusted.jpg'
    output_dir = '/Users/codyclifton/Desktop/Website_Images/Adjusted_Directors/'
    os.makedirs(output_dir, exist_ok=True)  
    output_path = f'{output_dir}{file_name}'
    adjust_aspect_ratio(url, output_path)
