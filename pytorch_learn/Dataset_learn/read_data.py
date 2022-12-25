import os
from torch.utils.data import Dataset
from PIL import Image


class Data(Dataset):
    def __init__(self, jpg_dir_path) -> None:
        super().__init__()
        self.jpg_dir_path = jpg_dir_path
        self.img_path_list = os.listdir(self.jpg_dir_path)

    def __getitem__(self, index):
        img_path = self.img_path_list[index]
        img = Image.open(os.path.join(self.jpg_dir_path, img_path))
        return img, 111



if __name__ == "__main__":
    d = Data("/home/black/Documents/Code/Python/python_learn/pytorch_learn/Dataset_learn/jpg/")
    print(d[0])

