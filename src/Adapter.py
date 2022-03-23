# -Adapter cho phép các interface không liên quan đến nhau có thể làm việc cùng nhau
# - Đối tượng kết nối giữa 2 interface gọi là Adapter , điều này cho phép các interface khác nhau có thể giao tiếp thông qua Adapter mà không cần thay đổi code có sẵn của hai bên.



# Adaptee Interface (source)
class IEU_Socket(object):
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass

    def earth(self): pass


class IUS_Socket(object):
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass


# Adaptee
class EU_Socket(IEU_Socket):
    def voltage(self): return 220

    def live(self): return 1

    def neutral(self): return -1


class US_Oven(object):
    __power = None

    def __init__(self, power):
        self.__power = power

    def defrost(self):
        if self.__power.voltage() > 110:
            print("Oven is burning !!")
        elif self.__power.live() == 1 and self.__power.neutral() == -1:
            print("Pizza is defrosting...")
        else:
            print("No power!!")


# Adapter
class SocketAdapter(IUS_Socket):
    __socket = None

    def __init__(self, socket1):
        self.__socket = socket1

    def voltage(self): return 110

    def live(self): return self.__socket.live()

    def neutral(self): return self.__socket.neutral()


# Client
socket = EU_Socket()
Oven = US_Oven(socket)
print("Plug in without socket adapter")
Oven.defrost()
print('-'*40)
print("Plug in with socket adapter")
Oven2 = US_Oven(SocketAdapter(socket))
Oven2.defrost()

