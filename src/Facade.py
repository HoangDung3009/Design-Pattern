# Pattern này cung cấp một giao diện chung đơn giản thay cho một nhóm các giao diện có trong một hệ thống con (subsystem).
# Facade Pattern định nghĩa một giao diện ở một cấp độ cao hơn để giúp cho người dùng có thể dễ dàng sử dụng hệ thống con này.
# Facade Pattern cho phép các đối tượng truy cập trực tiếp giao diện chung này để giao tiếp với các giao diện có trong hệ thống con.
# Mục tiêu là che giấu các hoạt động phức tạp bên trong hệ thống con, làm cho hệ thống con dễ sử dụng hơn.


class Engine(object):
    def __init__(self):
        self.spinner = 0

    def start(self, spin):
        self.spinner = min(spin, 300)


class Starter(object):
    def __init__(self):
        self.spin = 0

    def start(self, charge):
        if charge > 50:
            self.spin = 2000


class Power(object):
    def __init__(self):
        self.charge = 0


class Motocycle(object):
    def __init__(self):
        self.engine = Engine()
        self.starter = Starter()
        self.power = Power()

    def start_engine(self):
        self.starter.start(self.power.charge)
        self.power.charge -= 50
        self.engine.start(self.starter.spin)
        if self.engine.spinner > 0:
            print("Engine start")
        else:
            print("Engine not start")

    def run(self):
        self.power.charge = 100
        print("Running")


moto = Motocycle()
moto.start_engine()
print(moto.power.charge)
moto.run()
print(moto.power.charge)
moto.start_engine()
print(moto.power.charge)


