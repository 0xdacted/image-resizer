import os
from PIL import Image
from io import BytesIO
import requests

# Define a function to adjust the aspect ratio of an image from a given URL
def adjust_aspect_ratio(url, output_path, aspect_ratio=(2, 3)):
    # Get the image from the URL
    response = requests.get(url)
    # Open the image using PIL
    img = Image.open(BytesIO(response.content))
    
    # Get the current width and height of the image
    width, height = img.size
    # Calculate the new height based on the desired aspect ratio
    new_height = int((width / aspect_ratio[0]) * aspect_ratio[1])
    
    # If the new height is greater than the original height, calculate the new width based on the desired aspect ratio and set the new height to the original height
    if new_height > height:
        new_width = int((height / aspect_ratio[1]) * aspect_ratio[0])
        new_height = height
    # If the new height is not greater than the original height, set the new width to the original width
    else:
        new_width = width
    
    # Resize the image to the new dimensions using the LANCZOS resampling filter
    img = img.resize((new_width, new_height), Image.LANCZOS)
    
    # If the image has an alpha channel, convert it to RGB
    if img.mode in ('RGBA', 'LA'):
        img = img.convert("RGB")
    
    # Save the resized and potentially converted image to the specified output path
    img.save(output_path)

# Define a list of URLs of images to adjust
urls = [
    
]

# Loop over each URL in the list
for i, url in enumerate(urls, 1):
    # Derive the file name from the URL and add a suffix to indicate that it has been adjusted
    file_name = url.split('/')[-1].split('.')[0] + '-adjusted.jpg'
    # Define the directory where the adjusted images will be saved
    output_dir = ''
    # Create the output directory if it doesn't already exist
    os.makedirs(output_dir, exist_ok=True)  
    # Combine the output directory and file name to form the output path
    output_path = f'{output_dir}{file_name}'
    # Call the function to adjust the aspect ratio of the image at the current URL and save it to the output path
    adjust_aspect_ratio(url, output_path)
