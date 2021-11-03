import torch
from torch.utils.data import Dataset
from torchvision.transforms.functional import to_tensor, to_pil_image

from captcha.image import ImageCaptcha
import random
import numpy as np
from PIL import Image


class CaptchaDataset(Dataset):
    def __init__(self, characters, length, width, height, input_length, label_length):
        super(CaptchaDataset, self).__init__()
        self.characters = characters
        self.length = length
        self.width = width
        self.height = height
        self.input_length = input_length
        self.label_length = label_length
        self.n_class = len(characters)
        self.generator = ImageCaptcha(width=width, height=height)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        random_str = ''.join([random.choice(self.characters[1:]) for j in range(self.label_length)])
        image = to_tensor(self.generator.generate_image(random_str))
        target = torch.tensor([self.characters.find(x) for x in random_str], dtype=torch.long)
        input_length = torch.full(size=(1, ), fill_value=self.input_length, dtype=torch.long)
        target_length = torch.full(size=(1, ), fill_value=self.label_length, dtype=torch.long)
        print(image.shape)
        return image, target, input_length, target_length


if __name__ == "__main__":
    import string
    characters = '-' + string.digits + string.ascii_uppercase
    width, height, n_len, n_classes = 192, 64, 4, len(characters)#192 64
    n_input_length = 12
    batch_size = 70
    print(CaptchaDataset(characters, 1000 * batch_size, width, height, n_input_length, n_len).__getitem__(0))


    im = Image.open("./2.jpg")
    # 转 np
    np_im = np.array(im)
    # 转 tensor
    b = torch.from_numpy(np.transpose(np_im,  (2, 0, 1)))
    # 归一化
    b = b / 255
    print(b)
    print(b.shape)
    to_pil_image(b)

