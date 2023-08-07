from collections import defaultdict


if __name__ == "__main__":
    keys = ["1", "2"]
    dict_ = defaultdict(int)
    for key in keys:
        # 不存在不会报错
        dict_[key] += 1

    print(dict_)
