import time

from tqdm import tqdm

# for i in tqdm(range(1000)):
#      #do something
#      time.sleep(2)
#      pass


# from tqdm import trange
# for i in trange(100):
#     #do something
#     time.sleep(1)
#     pass

bar = tqdm(["a", "b", "c", "d"])
for char in bar:
    time.sleep(0.4)
    bar.set_description("Processing %s" % char)
