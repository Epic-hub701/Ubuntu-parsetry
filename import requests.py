import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    # Get the image URL from the user
    url = input("Please enter the image URL: ").strip()
    
    # Create the destination directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)
    
    try:
        # Fetch the image with a timeout to avoid hanging
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
        
        # Determine a filename from the URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        # If no filename could be extracted, use a default name
        if not filename:
            filename = "downloaded_image.jpg"
        
        # Build the full path where the image will be saved
        filepath = os.path.join("Fetched_Images", filename)
        
        # Save the image content in binary mode
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        # Inform the user of success
        print(f" Successfully fetched: {filename}")
        print(f" Image saved to {filepath}")
        print("\nConnection strengthened. Community enriched.")
    
    except requests.exceptions.RequestException as e:
        # Handle network or HTTP errors
        print(f"✗ Connection error: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()