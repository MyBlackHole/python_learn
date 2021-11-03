s = "this is string example....wow!!!"
print(s.startswith('this'))
print(s.startswith('is', 2, 4))
print(s.startswith('this', 2, 4))
_str = 'aHR0cDovL3Y5LXhnLXdlYi1zLml4aWd1YS5jb20vOWNmYjVjZmFmZmNjNjFhNGMyNjZjOTMzYjFhYzNhZTMvNWZkOTkzYTIvdmlkZW8vdG9zL2h4c3kvdG9zLWh4c3ktdmUtMDAyMi8yOTlhNzVjM2U0OTM0ZGJiOThhMjk2MDQ1ODVjYzI0Ny8\u002FYT0xNzY4JmJyPTEzNTAmYnQ9NDUwJmNkPTAlN0MwJTdDMCZjcj0wJmNzPTAmZHI9MCZkcz0xJmVyPTAmbD0yMDIwMTIxNjExNTUwMDAxMDAyOTA1NTAxODJEMDAzMzhEJmxyPWRlZmF1bHQmbWltZV90eXBlPXZpZGVvX21wNCZxcz0wJnJjPWFtbHRkM2c3TzJsdVp6TXphVHd6TTBBcE96YzRPVGxrTmpzMk56UThOek04TldjMllHZGthVEkxY1d0ZkxTMHRNeTl6Y3pZellUWXlNbDh2THpGZ05UQmpOakk2WXclM0QlM0Qmdmw9JnZyPQ=='
print(_str.encode().decode())
