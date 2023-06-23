import os
from PIL import Image

# 指定目标文件夹路径
folder_path = "C:\\Users\\14162\\Desktop\\graduate"

# 获取目标文件夹内的所有文件列表
file_list = os.listdir(folder_path)

# 构建一个字典，用于存储已经出现过的图片
image_dict = {}

# 循环遍历文件列表，并判断是否为图片格式
for filename in file_list:
    if filename.endswith(".jpg") or filename.endswith(".png"):

        # 打开图片并获取其像素值（即图片内容）
        with Image.open(os.path.join(folder_path, filename)) as im:
            image_pixels = im.tobytes()

        # 构建一个用于比较的字符串（由像素值组成）
        compare_str = str(image_pixels)

        # 如果该字符串已经存在于字典中，则说明该图片内容已重复，可以删除这个文件
        if compare_str in image_dict:
            os.remove(os.path.join(folder_path, filename))
            print(f"{filename} deleted as its same as {image_dict[compare_str]}")
        else:
            # 否则，将当前字符串添加到字典中
            image_dict[compare_str] = filename
