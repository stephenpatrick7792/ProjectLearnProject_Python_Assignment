import os
import requests
from urllib.parse import urlparse
import uuid

def download_image():
    # Prompt user for URL
    url = input("Enter the image URL: ").strip()
    
    # Create directory if it doesn't exist
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Fetch image from URL
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Full path
        file_path = os.path.join(save_dir, filename)

        # Save image in binary mode
        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"Image saved successfully as: {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download image: {e}")

if __name__ == "__main__":
    download_image()
