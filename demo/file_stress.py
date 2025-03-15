import os
import random
import uuid
import threading
import time
import argparse
from pathlib import Path

class FileStressTool:
    def __init__(self):
        self.lock = threading.Lock()
        self.file_list = []
        self.running = True
        self.stats = {
            'total_created': 0,
            'total_read': 0,
            'total_written': 0,
            'errors': 0
        }

    def generate_content(self, min_size, max_size, binary=True):
        size = random.randint(min_size, max_size)
        if binary:
            return os.urandom(size)
        return bytearray(random.getrandbits(8) for _ in range(size))

    def create_file(self, target_dir, min_size, max_size, binary=True):
        try:
            content = self.generate_content(min_size, max_size, binary)
            filename = Path(target_dir) / f"{uuid.uuid4().hex}.dat"
            with open(filename, 'wb') as f:
                f.write(content)
            with self.lock:
                self.file_list.append(filename)
                self.stats['total_created'] += 1
            return True
        except Exception as e:
            with self.lock:
                self.stats['errors'] += 1
            return False

    def read_file(self):
        with self.lock:
            if not self.file_list:
                return False
            filename = random.choice(self.file_list)
        
        try:
            with open(filename, 'rb') as f:
                f.read()
            with self.lock:
                self.stats['total_read'] += 1
            return True
        except Exception as e:
            with self.lock:
                self.stats['errors'] += 1
            return False

    def write_file(self, min_size, max_size, binary=True):
        try:
            content = self.generate_content(min_size, max_size, binary)
            with self.lock:
                if not self.file_list:
                    return False
                filename = random.choice(self.file_list)
            
            with open(filename, 'wb') as f:
                f.write(content)
            with self.lock:
                self.stats['total_written'] += 1
            return True
        except Exception as e:
            with self.lock:
                self.stats['errors'] += 1
            return False

    def worker(self, args):
        while self.running:
            if args.mode in ['create', 'mixed']:
                self.create_file(args.directory, args.min_size, args.max_size, args.binary)
            
            if args.mode in ['read', 'mixed'] and self.file_list:
                if random.random() < args.read_ratio:
                    self.read_file()
                else:
                    self.write_file(args.min_size, args.max_size, args.binary)
            
            time.sleep(random.uniform(0, args.max_delay))

    def run(self, args):
        threads = []
        start_time = time.time()

        # Create initial files if needed
        if args.initial_files > 0:
            for _ in range(args.initial_files):
                self.create_file(args.directory, args.min_size, args.max_size, args.binary)

        # Create worker threads
        for _ in range(args.threads):
            t = threading.Thread(target=self.worker, args=(args,))
            t.start()
            threads.append(t)

        try:
            while time.time() - start_time < args.duration:
                time.sleep(1)
                with self.lock:
                    print(f"\rCreated: {self.stats['total_created']} | "
                          f"Read: {self.stats['total_read']} | "
                          f"Written: {self.stats['total_written']} | "
                          f"Errors: {self.stats['errors']}", end='')
        except KeyboardInterrupt:
            print("\nStopping...")
        finally:
            self.running = False
            for t in threads:
                t.join()
            
            if args.cleanup:
                self.cleanup(args.directory)

            total_time = time.time() - start_time
            print("\n--- Final Statistics ---")
            print(f"Total operation time: {total_time:.2f} seconds")
            print(f"Files created: {self.stats['total_created']}")
            print(f"Files read: {self.stats['total_read']}")
            print(f"Files written: {self.stats['total_written']}")
            print(f"Total errors: {self.stats['errors']}")

    def cleanup(self, target_dir):
        for f in Path(target_dir).glob('*.dat'):
            try:
                f.unlink()
                with self.lock:
                    self.stats['total_created'] -= 1
            except:
                pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='File Stress Test Tool')
    parser.add_argument('-d', '--directory', required=True, help='Target directory')
    parser.add_argument('-t', '--threads', type=int, default=4, help='Number of worker threads')
    parser.add_argument('--min-size', type=int, default=1024, help='Minimum file size in bytes')
    parser.add_argument('--max-size', type=int, default=1048576, help='Maximum file size in bytes')
    parser.add_argument('--duration', type=int, default=60, help='Test duration in seconds')
    parser.add_argument('--initial-files', type=int, default=100, help='Initial number of files')
    parser.add_argument('--max-delay', type=float, default=0.1, help='Maximum delay between operations')
    parser.add_argument('--read-ratio', type=float, default=0.7, help='Read ratio for mixed mode')
    parser.add_argument('--mode', choices=['create', 'read', 'mixed'], default='mixed',
                       help='Operation mode')
    parser.add_argument('--binary', action='store_true', help='Use binary random data')
    parser.add_argument('--cleanup', action='store_true', help='Cleanup files after test')

    args = parser.parse_args()

    if not Path(args.directory).exists():
        Path(args.directory).mkdir(parents=True, exist_ok=True)

    tool = FileStressTool()
    tool.run(args)


# # 混合模式测试（默认参数）
# python file_stress.py -d /tmp/stress_test --threads 8 --duration 300
#
# # 纯创建模式
# python file_stress.py -d /tmp/create_test --mode create --threads 4 --min-size 4096 --max-size 1048576
#
# # 带自动清理的读取测试
# python file_stress.py -d /tmp/read_test --mode read --initial-files 1000 --cleanup
#
# # 自定义读写比例
# python file_stress.py -d /tmp/mixed_test --mode mixed --read-ratio 0.9 --threads 8
