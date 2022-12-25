from PIL import Image

im = Image.open("xxxx")
out = im.resize((194, 64), Image.ANTIALIAS)
out.save("xxxxx", im.format)
im.close()
out.close()
