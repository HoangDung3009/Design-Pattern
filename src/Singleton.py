# - Là một design pattern khởi tạo cho phép ta đảm bảo rằng một class chỉ có duy nhất một instance, cung cấp truy cập instance này với phạm vi toàn ứng dụng
# - Chỉ có duy nhất 1 instance: Giả sử ta tao mới một object, sau đó lại tạo thêm một object nữa. Thay vì nhận được một object mới, ta nhận lại object đã tạo trước đó. Ta có thể tái sử dụng code thông qua instance duy nhất của class.
# - Truy cập toàn cục: Singleton pattern cung cấp instance để truy nhập toàn cục. Bất cứ đâu đều có thể truy nhập class thông qua instance như một hình thức tái sử dụng code.


class Singleton:
    __INSTANCE = None

    @staticmethod
    def getInstance():
        if Singleton.__INSTANCE is None:
            Singleton()
        return Singleton.__INSTANCE

    def __init__(self):
        if Singleton.__INSTANCE is not None:
            raise Exception("This is a singleton")
        else:
            Singleton.__INSTANCE = self


s = Singleton()
print(s)
t = Singleton.getInstance()
print(t)
aa = Singleton.getInstance()
print(aa)

