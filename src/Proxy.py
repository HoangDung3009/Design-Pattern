# Proxy Pattern là mẫu thiết kế mà ở đó tất cả các truy cập trực tiếp đến một đối tượng nào đó
# sẽ được chuyển hướng vào một đối tượng trung gian (Proxy Class). Mẫu Proxy (người đại diện) đại diện cho một đối tượng khác thực thi các phương thức,
# phương thức đó có thể được định nghĩa lại cho phù hợp với múc đích sử dụng.

class IRemote(object):
    def showMessage(self): pass

class Remote(IRemote):



    def showMessage(self):
        print("Turn on the light")



class Proxy(IRemote):
    def __init__(self, remote):
        self.__remote = remote

    def showMessage(self):
        print("This is proxy access control")
        self.__remote.showMessage()


rs = Remote()
rs.showMessage()
print('-'*50)
proxy = Proxy(rs)
proxy.showMessage()

