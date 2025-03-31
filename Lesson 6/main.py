from PIL import Image, ImageFilter, ImageEnhance 

orange_cat = Image.open(r"Unit-2\Lesson 6\orange_cat.jpg")
blurry_cat = orange_cat.filter(ImageFilter.GaussianBlur(20))
blurry_cat.show()
blurry_cat.save("blurry_cat.jpg")