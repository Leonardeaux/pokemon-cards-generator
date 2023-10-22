import os
import numpy as np

from PIL import Image


def get_images(directory):
    pixel_values_list = []
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with Image.open(file_path) as img:
                    pixel_values = np.array(img)
                    pixel_values_list.append(pixel_values)
            except Exception as e:
                print(f"Erreur lors du traitement de l'image {file_path}: {e}")

    return pixel_values_list


list = get_images('data/raw_HD')

i = 0
for image in list:
    new_image = Image.fromarray(image, mode='RGB').resize((224, 336))

    
    # Save image
    new_image.save(f"data/processed_images_v2/{i}.jpg")
    i += 1