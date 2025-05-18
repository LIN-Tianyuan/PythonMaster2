class Phone:
    serial_number = None
    producer = None

    def call_by_4g(self):
        print("4g call.")

class Phone2025(Phone):
    face_id = True

    def call_by_5g(self):
        print("5g call.")

phone = Phone2025()
phone.call_by_5g()
phone.call_by_4g()

phone1 = Phone()
phone1.call_by_4g()