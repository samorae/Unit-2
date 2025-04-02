from PIL import Image, ImageFilter, ImageEnhance 

bo_nix = Image.open(r'Lesson 6\download.jpg')
rotated_nix = bo_nix.rotate(180)
rotated_nix.show()
blurry_nix = bo_nix.filter(ImageFilter.BoxBlur(5))
blurry_nix.show()
