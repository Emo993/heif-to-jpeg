
import os
from PIL import Image

input_folder = r"E:\图片\4.29-5.1烟台大连照片"  # 替换为包含HEIC文件的文件夹路径
output_folder = r"E:\图片\4.29-5.1烟台大连照片"  # 替换为保存转换后JPEG文件的文件夹路径

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(".HEIC"):
        heic_path = os.path.join(input_folder, filename)
        jpeg_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpeg")
        with Image.open(heic_path) as image:
            image.save(jpeg_path, "JPEG")