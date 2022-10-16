import threading


def thread_j():
    print("This is added Thread,number is %s" % threading.current_thread())


def mul_thread(target):
    # print("active_threads_count:", threading.active_count())
    # print("threading_enumerate:", threading.enumerate())  # 查看激活的线程名称
    # print("threading.current_thread:", threading.current_thread())  # 运行程序时，运行的线程是什么
    added_thread = threading.Thread(target=target)  # 自己添加的线程,这只是定义
    added_thread.start()


if __name__ == '__main__':
    mul_thread(target=thread_j)
