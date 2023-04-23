import pdb


def main(*arg):
    pdb.set_trace()
    print(arg)


# python3 main.py
# 遇到 pdb.set_trace 会自动停下
if __name__ == "__main__":
    main(1, 2, 3, 4)
