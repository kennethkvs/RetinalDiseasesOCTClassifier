import os
from PIL import Image

def load_images_from_folder(folder_path: str):
    """Returns a list of images from a specified dataset folder.

    Args:
        folder_path (str): Path to the folder containing images.

    Returns:
        list[PIL.Image.Image]: A list of loaded images.
    """
    
    folder_names = [
            "CNV",
            "DME",
            "DRUSEN",
            "NORMAL"
        ]

    images = []
    
    for folder_name in folder_names:
        path = "Dataset/" + folder_path + "/" + folder_name + "/"
        for filename in os.listdir(path):
            # Construct the full path to the image file
            img_path = os.path.join(path, filename)
            
            # List of all folders underneath the specified folder
            # Check if the file is a JPEG image

            if os.path.isfile(img_path) and filename.lower().endswith((".jpeg")):
                try:
                    img = Image.open(img_path)
                    images.append(img)
                    print(f"Loaded image: {filename}")
                except IOError:
                    print(f"Could not open or identify image file: {filename}")
    return images

# Example usage:
folder_of_images = "test"  # Replace with your actual folder path
loaded_images = load_images_from_folder(folder_of_images)

if loaded_images:
    print(f"Successfully loaded {len(loaded_images)} images.")
else:
    print("No images found or loaded in the specified folder.")
