from PIL import Image, ImageFilter, ImageEnhance 

orange_cat = Image.open(r"Lesson 6\orange_cat.jpg")
blurry_cat = orange_cat.filter(ImageFilter.GaussianBlur(20))
blurry_cat.show()
blurry_cat.save("blurry_cat.jpg")
bw_cat = ImageEnhance.Color(orange_cat).enhance(0).save("Lesson 6/bw_cat.jpg")
bright_cat = ImageEnhance.Color(orange_cat).enhance(5).save("Lesson 6/bright_cat_cat.jpg")