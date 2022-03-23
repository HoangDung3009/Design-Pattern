# - là một design pattern khởi tạo object thay vì tạo ra một object, Prototype pattern sử dụng việc cloning (copy một nguyên mẫu của object)
# - Việc tạo mới object sẽ dựa trên object mẫu mà không cần sử dụng các toán tử new hay constructor được cấp.
# - Mục đích: che giấu thông tin của object, chỉ cung cấp ra bên ngoài một lượng thông tin giới hạn. Vì vậy không thể dùng toán tử new và sao hceps dữ liệu được Object cung cấp


from copy import deepcopy
# Computer
class Computer(object):
    def __init__(self):
        self.__motherboard = None
        self.__CPU = None
        self.__VGA = None
        self.__RAM = None

    def setMotherboard(self, motherboard):
        self.__motherboard = motherboard

    def setCPU(self, CPU):
        self.__CPU = CPU

    def setVGA(self, VGA):
        self.__VGA = VGA

    def setRAM(self, RAM):
        self.__RAM = RAM

    def toString(self):
        print("mother board: " + self.__motherboard.name)
        print("CPU: " + self.__CPU.name)
        print("VGA: " + self.__VGA.name)
        print("RAM: " + self.__RAM.type)

    def clone(self):
        return deepcopy(self)

# Computer component
class Motherboard:
    name = None


class CPU:
    name = None


class VGA:
    name = None


class RAM:
    type = None


# Computer Builder Interface
class IComputerBuilder(object):
    def addMotherboard(self): pass

    def addCPU(self): pass

    def addVGA(self): pass

    def addRAM(self): pass

    def Build(self): pass


# Computer Builder 1
class ComputerBuilder1(IComputerBuilder):

    def addMotherboard(self):
        motherboard = Motherboard()
        motherboard.name = "z370"
        return motherboard

    def addCPU(self):
        cpu = CPU()
        cpu.name = "i7 8700K"
        return cpu

    def addVGA(self):
        vga = VGA()
        vga.name = "180ti"
        return vga

    def addRAM(self):
        ram = RAM()
        ram.type = "DDR4 8GB"
        return ram


class ComputerBuilder2(IComputerBuilder):

    def addMotherboard(self):
        motherboard = Motherboard()
        motherboard.name = "z322"
        return motherboard

    def addCPU(self):
        cpu = CPU()
        cpu.name = "i5 10040F"
        return cpu

    def addVGA(self):
        vga = VGA()
        vga.name = "180ti"
        return vga

    def addRAM(self):
        ram = RAM()
        ram.type = "DDR4 16GB"
        return ram


class Director(object):
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def BuildComputer(self):
        computer = Computer()

        motherboard = self.__builder.addMotherboard(self.__builder)
        computer.setMotherboard(motherboard)

        cpu = self.__builder.addCPU(self.__builder)
        computer.setCPU(cpu)

        vga = self.__builder.addVGA(self.__builder)
        computer.setVGA(vga)

        ram = self.__builder.addRAM(self.__builder)
        computer.setRAM(ram)

        return computer


director = Director()
director.setBuilder(ComputerBuilder1)
computer1 = director.BuildComputer()

print("-----------------------------------")
print(computer1)
computer1.toString()
print("-----------------------------------")
computer2 = computer1.clone()
print(computer2)
director.setBuilder(ComputerBuilder2)
computer2 = director.BuildComputer()
computer2.toString()


