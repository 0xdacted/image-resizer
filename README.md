# Image Aspect Ratio Adjuster

This Python script is designed to adjust the aspect ratio of images from given URLs and save them locally. The script utilizes several Python libraries including `os`, `PIL` (Pillow), `io`, and `requests`.

## How it Works

1. The script takes a list of URLs pointing to images.
2. For each URL, it sends a GET request to fetch the image and opens it using the Python Imaging Library (Pillow).
3. The script then resizes the image to a specific aspect ratio, defaulting to 2:3 if no aspect ratio is provided.
4. If the image has an alpha channel, the script converts it to RGB format.
5. Finally, the script saves the adjusted image to a specified local directory, creating the directory if it doesn't already exist.

## Usage

To adjust the aspect ratio of images, simply add the URLs to the `urls` list in the script. You can also specify a different aspect ratio by passing it as a tuple to the `adjust_aspect_ratio` function.

The output directory can be modified by changing the value of `output_dir` in the script.

### Example:

urls = [
    'https://i.postimg.cc/rFGvCVgP/theodoros-angelopoulos.jpg',
]

for i, url in enumerate(urls, 1):
    file_name = url.split('/')[-1].split('.')[0] + '-adjusted.jpg'
    output_dir = '/Users/______/Desktop/Website_Images/Adjusted_Directors/'
    os.makedirs(output_dir, exist_ok=True)  
    output_path = f'{output_dir}{file_name}'
    adjust_aspect_ratio(url, output_path, aspect_ratio=(16, 9))

In this example, the aspect ratio is set to 16:9.

## Dependencies
You need to have the following Python libraries installed:

os
PIL (Pillow)
io
requests

## Notes
This script does not handle exceptions or errors. You should ensure the URLs are valid and point to accessible images. Additionally, you should have the necessary permissions to create directories and write files to the specified output location.

If you want to use a version that handles errors and allows you to download anywhere on your system, visit codyc.xyz/image_resizer.