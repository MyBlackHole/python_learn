from datetime import datetime
import pytz

# 配置redis模块
from apscheduler.jobstores.redis import RedisJobStore

# 配置线程
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor

# 创建定时任务的包
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler

# 其中  REDIS  这个是redis的配置信息

REDIS = {
    "host": "127.0.0.1",
    "port": "6379",
    "db": 2,
    "password": "",
}

jobstores = {"redis": RedisJobStore(**REDIS)}

executors = {
    "default": ThreadPoolExecutor(10),  # 默认线程数
    "processpool": ProcessPoolExecutor(3),  # 默认进程
}


def tick():
    print("Tick! The time is: %s" % datetime.now())


# 将配置信息放在里边
sched = BackgroundScheduler(
# sched = BlockingScheduler(
    jobstores=jobstores,
    # executors=executors,
    next_run_time=datetime.now,
)

sched.configure(timezone=pytz.timezone("Asia/Shanghai"))

# 其中的func指的是定时任务需要的方法名称，
# trigger 根据时间触发      默认值为 date
# jobstore 持久化的方式     如果要持久化必须写， 不写的话就会默认将定时任务保存在内存中，当项目重启之后就会失效
# seconds 执行的周期
# run_date 执行的时间     执行需要的时间
# args			执行方法的参数
job = sched.add_job(
    tick,
    "interval",
    id="tick_job_id",
    # trigger="date",
    # jobstore="redis",
    seconds=30,
    # run_date="%Y-%m-%d %H:%M:%S",
    next_run_time=datetime.now(),
    # args=(notice,),
)


sched.start()
