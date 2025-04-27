class Phone:
    serial_number = None        # Numéro de série
    producer = None             # Fabricant

    # Variable privé
    __current_voltage = 50    # Tension actuelle

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            self.__keep_single_core()
            print("Les appels 5g sont désormais possible.")
        else:
            print("Défaut d'appel, batterie faible.")

    # Méthode privé
    def __keep_single_core(self):
        print("Faire fonctionner l'unité centrale en mode mono-coeur pour économiser de l'énergie.")

phone = Phone()
phone.serial_number = "123"
print(phone.serial_number)
# phone.__current_voltage = "456"
# print(phone.__current_voltage)
phone.call_by_5g()
# phone.__keep_single_core()
