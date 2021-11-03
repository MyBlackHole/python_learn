import torch
# import torch.nn as nn
#
# from collections import OrderedDict
from PIL import Image
import numpy as np
#
# class Model(nn.Module):
#     def __init__(self, n_classes, input_shape=(3, 64, 128)):
#         super(Model, self).__init__()
#         self.input_shape = input_shape
#         channels = [32, 64, 128, 256, 256]
#         layers = [2, 2, 2, 2, 2]
#         kernels = [3, 3, 3, 3, 3]
#         pools = [2, 2, 2, 2, (2, 1)]
#         modules = OrderedDict()
#
#         def cba(name, in_channels, out_channels, kernel_size):
#             modules[f'conv{name}'] = nn.Conv2d(in_channels, out_channels, kernel_size,
#                                                padding=(1, 1) if kernel_size == 3 else 0)
#             modules[f'bn{name}'] = nn.BatchNorm2d(out_channels)
#             modules[f'relu{name}'] = nn.ReLU(inplace=True)
#
#         last_channel = 3
#         for block, (n_channel, n_layer, n_kernel, k_pool) in enumerate(zip(channels, layers, kernels, pools)):
#             for layer in range(1, n_layer + 1):
#                 cba(f'{block+1}{layer}', last_channel, n_channel, n_kernel)
#                 last_channel = n_channel
#             modules[f'pool{block + 1}'] = nn.MaxPool2d(k_pool)
#         modules[f'dropout'] = nn.Dropout(0.25, inplace=True)
#         self.cnn = nn.Sequential(modules)
#         self.lstm = nn.LSTM(input_size=self.infer_features(), hidden_size=128, num_layers=2, bidirectional=True)
#         self.fc = nn.Linear(in_features=256, out_features=n_classes)
#
#     def infer_features(self):
#         x = torch.zeros((1,)+self.input_shape)
#         x = self.cnn(x)
#         x = x.reshape(x.shape[0], -1, x.shape[-1])
#         return x.shape[1]
#
#     def forward(self, x):
#         x = self.cnn(x)
#         x = x.reshape(x.shape[0], -1, x.shape[-1])
#         x = x.permute(2, 0, 1)
#         x, _ = self.lstm(x)
#         x = self.fc(x)
#         return x
#

import string
# -0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ
characters = '-' + string.digits + string.ascii_uppercase

def decode(sequence):
    a = ''.join([characters[x] for x in sequence])
    s = ''.join([x for j, x in enumerate(a[:-1]) if x != characters[0] and x != a[j+1]])
    if len(s) == 0:
        return ''
    if a[-1] != characters[0] and s[-1] != a[-1]:
        s += a[-1]
    return s

# width, height, n_len, n_classes = 192, 64, 4, len(characters)
#
# model = Model(n_classes, input_shape=(3, height, width))

# torch.save(model.state_dict(), "./ctc3.pth")
# model.load_state_dict(torch.load("./ctc3.pth"))
# torch.load(model, "./ctc3.pth")
# model.load_state_dict(torch.load("./ctc3.pth"))

# 加载模型
model = torch.load("./ctc3.pth")

model.eval()

im = Image.open("./3.png")
# im = Image.open("./2.jpg")
# 转 np
np_im = np.array(im)
# 转 tensor
b = torch.from_numpy(np.transpose(np_im,  (2, 0, 1)))
# 归一化
image = b / 255

output = model(image.unsqueeze(0).cpu())
output_argmax = output.detach().permute(1, 0, 2).argmax(dim=-1)
print('pred:', decode(output_argmax[0]))

