from torchvision import transforms
from PIL import Image

img = Image.open("./2.jpg")

tt = transforms.ToTensor()
tensor_img = tt(img)

print(tensor_img)
print(tensor_img.shape)


