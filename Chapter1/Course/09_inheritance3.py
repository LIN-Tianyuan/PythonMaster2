class Phone:
    serial_number = None
    producer = "Apple"

    def call_by_5g(self):
        print("5g calls.")

class NFCReader:
    nfc_type = "Fifth Generation"
    producer = "HM"

    def read_card(self):
        print("Read NFC cards.")

    def write_card(self):
        print("Write NFC cards.")

class RemoteControl:
    rc_type = "IR remote control"

    def control(self):
        print("Infrared remote control opening.")

# Héritage multiple
class XiaoMiPhone(Phone, NFCReader, RemoteControl):
    pass

phone = XiaoMiPhone()
phone.read_card()
phone.control()
print(phone.producer)