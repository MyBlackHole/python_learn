import os
import time
import random
import mmap
from pathlib import Path
from datetime import datetime, timedelta
import uuid
class FileModifier:
    @staticmethod
    def modify_file(file_path, new_data, offset=None, mode='overwrite'):
        """
        文件修改操作支持偏移量控制
        :param file_path: 目标文件路径
        :param new_data: 要写入的新数据
        :param offset: 写入起始偏移量（字节）
        :param mode: 写入模式 [overwrite|insert|safe]
        """
        file_path = Path(file_path)
        if not file_path.exists():
            raise FileNotFoundError(f"{file_path} 不存在")
        with open(file_path, 'r+b') as f:
            with mmap.mmap(f.fileno(), 0) as mm:
                original_size = len(mm)
                # 自动确定偏移量
                if offset is None:
                    offset = random.randint(0, original_size) if original_size > 0 else 0
                else:
                    offset = min(offset, original_size)
                # 处理不同写入模式
                if mode == 'overwrite':
                    end_pos = offset + len(new_data)
                    if end_pos > original_size:
                        mm.resize(end_pos)
                    mm[offset:end_pos] = new_data
                elif mode == 'insert':
                    mm.resize(original_size + len(new_data))
                    mm.move(offset + len(new_data), offset, original_size - offset)
                    mm[offset:offset+len(new_data)] = new_data
                elif mode == 'safe':
                    safe_end = min(offset + len(new_data), original_size)
                    mm[offset:safe_end] = new_data[:safe_end - offset]
        return {
            'path': str(file_path),
            'original_size': original_size,
            'new_size': file_path.stat().st_size,
            'offset': offset,
            'mode': mode
        }
class TimelineOperationGenerator:
    def __init__(self, config):
        self.config = config
        self.operations = []
        self.file_pool = set()
    def generate_operations(self):
        """生成带偏移量的操作时间线"""
        current_time = datetime.now()
        # 生成初始文件
        for _ in range(self.config['initial_files']):
            file_path = self._create_random_file()
            self.file_pool.add(file_path)
            current_time += self._random_interval()
        # 生成修改操作
        for _ in range(self.config['modify_ops']):
            if not self.file_pool:
                break
            file_path = random.choice(list(self.file_pool))
            op = {
                'time': current_time,
                'type': 'modify',
                'path': file_path,
                'offset': self._generate_offset(file_path),
                'size': random.randint(*self.config['modify_size']),
                'mode': random.choice(['overwrite', 'insert', 'safe'])
            }
            self.operations.append(op)
            current_time += self._random_interval()
        return sorted(self.operations, key=lambda x: x['time'])
    def _create_random_file(self):
        """创建初始随机文件"""
        file_path = Path(self.config['base_dir']) / f"file_{uuid.uuid4().hex[:8]}.dat"
        size = random.randint(*self.config['file_size'])
        file_path.write_bytes(os.urandom(size))
        return file_path
    def _generate_offset(self, file_path):
        """生成智能偏移量"""
        file_size = file_path.stat().st_size
        if file_size == 0:
            return 0
        # 偏移量生成策略
        strategy = random.choices(
            ['head', 'middle', 'end', 'random'],
            weights=[0.2, 0.5, 0.2, 0.1],
            k=1
        )[0]
        if strategy == 'head':
            return random.randint(0, file_size//10)
        elif strategy == 'middle':
            return random.randint(file_size//3, 2*file_size//3)
        elif strategy == 'end':
            return random.randint(9*file_size//10, file_size)
        else:
            return random.randint(0, file_size)
    def _random_interval(self):
        """生成随机时间间隔"""
        return timedelta(seconds=random.expovariate(1/self.config['interval']))
# 使用示例
config = {
    'base_dir': '/tmp/file_ops',
    'initial_files': 100,
    'modify_ops': 500,
    'file_size': (1024, 1048576),  # 1KB-1MB
    'modify_size': (512, 524288),   # 512B-512KB
    'interval': 2                   # 平均间隔秒数
}
generator = TimelineOperationGenerator(config)
operations = generator.generate_operations()

print(operations)

# 执行操作
for op in operations:
    while datetime.now() < op['time']:
        time.sleep(0.001)
    if op['type'] == 'modify':
        new_data = os.urandom(op['size'])
        result = FileModifier.modify_file(
            op['path'],
            new_data,
            offset=op['offset'],
            mode=op['mode']
        )
        print(f"Modified {result['path']} at offset {result['offset']} ({op['mode']} mode)")
