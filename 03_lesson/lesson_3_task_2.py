from smartphone import Smartphone

catalog = [
    Smartphone("Realme", "C85", "+79191234567"),
    Smartphone("Xiaomi", "15", "+791275654321"),
    Smartphone("Honor", "X9b", "+791353344500"),
    Smartphone("Huawei", "XT3", "+79925544399"),
    Smartphone("Iphone", "17pro", "+79571122333")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}.")
