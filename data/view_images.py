import pickle
import random
from pathlib import Path
from PIL import Image



img = Image.open("data\cifar10\cifar10\test\airplane\0001.png")
print(f"Random image path: data\cifar10\cifar10\test\airplane\0001.png")
print(f"Image class: Airplane")
print(f"Image height: {img.height}")
print(f"Image width: {img.width}")


# # 1. Define path properly
# data_path = Path(r"data\cifar10\cifar10\test")  # ✅ Use raw string or forward slashes

# # 2. Check if the folder exists
# if not data_path.exists():
#     print(f"Error: Folder '{data_path}' does not exist.")
# else:
#     # 3. Get all image paths
#     image_path_list = list(data_path.glob("*.png"))

#     # 4. Check if images are found
#     if not image_path_list:
#         print(f"Error: No PNG images found in '{data_path}'.")
#     else:
#         # 5. Pick a random image
#         random_image_path = random.choice(image_path_list)

#         # 6. Get image class (folder name)
#         image_class = random_image_path.parent.stem

#         # 7. Open image
#         img = Image.open(random_image_path)

#         # 8. Print metadata
#         print(f"Random image path: {random_image_path}")
#         print(f"Image class: {image_class}")
#         print(f"Image height: {img.height}")
#         print(f"Image width: {img.width}")

#         # 9. Show the image
#         img.show()
