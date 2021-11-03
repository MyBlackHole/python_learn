from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np

writer = SummaryWriter("logs")


# img
writer.add_image("img", np.array(Image.open("./2.jpg")), 0, dataformats='HWC')

# # logs 生成
# for i in range(1000):
#     writer.add_scalar(tag="blackhole", scalar_value=i, global_step=i+1)

writer.close()

# 启动
# tensorboard --logdir logs
