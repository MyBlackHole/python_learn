import time
import setproctitle
import multiprocessing


def sub_process(proc_title):
    proc_title_old = setproctitle.getproctitle()
    print(f"proc_title_old: {proc_title_old}")

    setproctitle.setproctitle(proc_title)
    proc_title_new = setproctitle.getproctitle()
    print(f"proc_title_new: {proc_title_new}")

    # time.sleep(10)


def main_process():
    process_list = []
    setproctitle.setproctitle("blackhole")

    # 创建进程1
    proc_title = "python sub_process_1"
    tmp_process = multiprocessing.Process(target=sub_process, args=(proc_title,))
    process_list.append(tmp_process)

    # 创建进程2
    proc_title = "python sub_process_2"
    tmp_process = multiprocessing.Process(target=sub_process, args=(proc_title,))
    process_list.append(tmp_process)

    # 启动所有进程
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()


if __name__ == "__main__":
    main_process()
