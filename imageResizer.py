import requests
from PIL import Image
from io import BytesIO

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
    
    img = img.resize((new_width, new_height), Image.ANTIALIAS)
    img.save(output_path)

urls = [

]

for i, url in enumerate(urls, 1):
    output_path = f'image{i}_adjusted.jpg'
    adjust_aspect_ratio(url, output_path)
