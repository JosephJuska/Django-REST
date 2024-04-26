import requests
import os

def create_article(title, content, banner_path, api_endpoint):
    """
    Create an article by sending title, content, and banner to the API endpoint.

    Args:
        title (str): Title of the article.
        content (str): Content of the article.
        banner_path (str): Path to the banner image file.
        api_endpoint (str): URL of the API endpoint.

    Returns:
        requests.Response: Response object from the API.
    """
    # Prepare the data to be sent
    data = {
        'title': title,
        'content': content
    }

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the image file
    image_path = os.path.join(script_dir, banner_path)

    # Open and attach the banner image file
    files = {'banner': open(image_path, 'rb')}

    # Send the POST request
    response = requests.put(api_endpoint, data=data, files=files)

    return response

# Example usage:
title = 'Sample Title 3'
content = 'Sample content of the article. 3'
banner_path = 'image-3.jpg'
api_endpoint = 'http://127.0.0.1:8000/api/update-article/3/'

response = create_article(title, content, banner_path, api_endpoint)
print(response.text)
