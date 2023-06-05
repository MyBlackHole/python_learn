# rpyc

1. Client 一定要 close() 连接哦！
2. Server 中 exposed_ 打头的函数才能被 客户端调用。所以如果写服务端代码的时候想要让客户端调用 就要加这一个前缀
3. client 要访问服务器端代码通过 c.root.xxx 才能访问，如: c.root.get_time() 调用服务器端 get_time 方法
4. RPYC没有认证机制，任何客 户端都可以直接访问服务器端的暴露的方法
