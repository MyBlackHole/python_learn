#!/user/bin/env python
# -*- coding: utf-8 -*-
from abc import abstractmethod


# 实现抽象的状态类
class LiftState:
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# 实现各个具体的状态类
class OpenState(LiftState):
    def open(self):
        print("OPEN:The door is opened...")
        return self

    def close(self):
        print("OPEN:The door start to close...")
        print("OPEN:The door is closed")
        return StopState()

    def run(self):
        print("OPEN:Run Forbidden.")
        return self

    def stop(self):
        print("OPEN:Stop Forbidden.")
        return self


class RunState(LiftState):
    def open(self):
        print("RUN:Open Forbidden.")
        return self

    def close(self):
        print("RUN:Close Forbidden.")
        return self

    def run(self):
        print("RUN:The lift is running...")
        return self

    def stop(self):
        print("RUN:The lift start to stop...")
        print("RUN:The lift stopped...")
        return StopState()


class StopState(LiftState):
    def open(self):
        print("STOP:The door is opening...")
        print("STOP:The door is opened...")
        return OpenState()

    def close(self):
        print("STOP:Close Forbidden")
        return self

    def run(self):
        print("STOP:The lift start to run...")
        return RunState()

    def stop(self):
        print("STOP:The lift is stopped.")
        return self


# 为在业务中调度状态转移，还需要将上下文进行记录，需要一个上下文的类
class Context:
    def __init__(self):
        self.lift_state = None

    def get_state(self):
        return self.lift_state

    def set_state(self, lift_state):
        self.lift_state = lift_state

    def open(self):
        self.set_state(self.lift_state.open())

    def close(self):
        self.set_state(self.lift_state.close())

    def run(self):
        self.set_state(self.lift_state.run())

    def stop(self):
        self.set_state(self.lift_state.stop())


# 这样，在进行电梯的调度时，只需要调度Context就可以了。业务逻辑中如下
if __name__ == "__main__":
    ctx = Context()
    ctx.set_state(StopState())
    ctx.open()
    ctx.run()
    ctx.close()
    ctx.run()
    ctx.stop()
