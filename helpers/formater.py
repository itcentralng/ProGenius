import re
import base64
import os
import uuid
from html import escape
from .stability import dream
from .upload import add
from app.image.model import Image

def clean(text: str, note_id: int):
    # Define the regular expression pattern to match [image: prompt]
    pattern = r'\[image:\s+([^\]]*)\]'

    # Use re.sub() to replace each [image: prompt] with a base64-encoded image
    def replace(match):
        prompt = match.group(1)
        encoded_string = dream(prompt)
        image_url = add(encoded_string)
        image = Image.create(prompt, image_url, note_id)
        return f'[img:{image.id}]'

    # Use re.sub() to replace all [image: prompt] patterns with images
    text = re.sub(pattern, replace, text)

    # Return the modified string wrapped in <p> tags
    return text

def filter_image_prompts(text: str):
    # Define the regular expression pattern to match [image: prompt]
    pattern = r'\[image:\s+([\w\s]*)\]'

    # Use re.findall() to extract all [image: prompt] from the input text
    filtered_list = re.findall(pattern, text)

    # Return the list of filtered [image: prompt]
    return filtered_list

def replace_image_prompts(title: str, text: str):
    # Define the regular expression pattern to match [image: prompt]
    pattern = r'\[image:\s+([\w\s]*)\]'

    # Use re.sub() to replace each [image: prompt] with a base64-encoded image
    def replace(match):
        prompt = match.group(1)
        encoded_string = dream(prompt)
        image_path = save_base64_image(encoded_string)
        return f'<img src={image_path}>'

    # Replace any newline characters with <br> tags
    text = text.replace('\n', '<br>')

    # Use re.sub() to replace all [image: prompt] patterns with images
    text = re.sub(pattern, replace, text)

    # Return the modified string wrapped in <p> tags
    return f'<h4>{title.upper()}</h4><p>{text}</p>'


def save_base64_image(base64_image):
    # Decode the base64 image data
    image_data = base64.b64decode(base64_image)

    # Create a unique file name for the image
    file_name = str(uuid.uuid4()) + '.png'
    file_path = os.path.join(os.getcwd(), file_name)

    # Write the image data to a file
    with open(file_path, "wb") as f:
        f.write(image_data)

    # Return the path of the saved image file
    return file_path

