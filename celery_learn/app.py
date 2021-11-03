from tasks import add, add2, add1
from celery.result import AsyncResult
from celery import group, chain, chord

if __name__ == '__main__':
    print('task start....')
    res1 = add.delay(2,3)
    print('task end....')
    print(res1)
    print(res1.ready())
    print(res1.get())
    print(res1.status)
    print(res1._cache)

    res2 = AsyncResult(res1.id)
    print(res2)
    print(res2.ready())
    print(res2.get())
    print(res2.status)

    # 使组式:
    add2_group = group([add2.s(i, i) for i in range(10)])
    # 同步堵塞返回值为止
    print(add2_group().get())
    # 异步 返回 id list
    result = add2_group.apply_async()

    # 使链式:
    # 说明: chain内部两个链式子任务,|表示前一个的输出作为另一个的输入,当调用chain(...)(5)时,其实是首先调用add.s(2).delay(5)计算出结果为7,然后|传递作为add.s(1)的输入,其实是调用add.s(1).delay(7)
    add_chain = chain(add.s(1, 2)| add1.s(3))
    print(add_chain().get())
    print(add_chain().parent.get())
    print(add_chain().parent.parent.get())

    add_chain = chain(add.s(2)| add1.s(4))
    print(add_chain(1).get())
    print(add_chain(1).parent.get())
    print(add_chain(1).parent.parent.get())


    # 使回调:
    add_chord = chord(add2_group, add(1, 1))
    print(add_chord().get())
