from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha
import numpy as np

audio = AudioCaptcha()
image = ImageCaptcha()

# data = audio.generate('1234')
# audio.write('1234', 'out.wav')

data = image.generate('1234')
print(type(data))

image.write('1234', 'out.png')

data1 = image.generate_image("1234")
print(type(data1))

image.write('1234', 'out1.png')


from PIL import Image
im = Image.open("2.jpg")
print(type(im))
im = np.array(im)
print(im.shape)
print(im.dtype)

