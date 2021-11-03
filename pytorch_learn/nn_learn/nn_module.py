import torch
from torch import nn

class M(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input):
        output = input + 1
        return output


m = M()
x = torch.tensor(1.0)

output = m(x)
print(output)
