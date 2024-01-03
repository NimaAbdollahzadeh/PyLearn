import os
import imageio

IMAGES = []
for file_name in sorted(os.listdir("1.Introduction/Assignment-8/gif/image")):
    file_path = os.path.join("1.Introduction/Assignment-8/gif/image", file_name)
    IMAGES.append(imageio.imread(file_path))
imageio.mimsave("1.Introduction/Assignment-8/gif/output.gif", IMAGES)