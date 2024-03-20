from PIL import Image, ImageEnhance

def change_saturation(image_path, saturation_level):
    # 打开图像
    img = Image.open(image_path)
    
    # 创建一个图像增强对象
    enhancer = ImageEnhance.Color(img)
    
    # 调整饱和度
    img_enhanced = enhancer.enhance(saturation_level)
    
    # 保存增强后的图像
    img_enhanced.save("D:enhanced_image.jpg")

# 调用函数，更改图像饱和度
change_saturation("D:IMG_0182.jpg", 2.0)  # 2.0表示饱和度提高两倍
