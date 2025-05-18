class Phone:
    serial_number = None
    producer = "HUAWEI"

    def call_by_5g(self):
        print("Father 5g calls.")

class MyPhone(Phone):
    producer = "Apple"

    def call_by_5g(self):
        print("Child 5g calls.")

my_phone = MyPhone()
print(my_phone.producer)

