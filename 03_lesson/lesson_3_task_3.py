from address import Address
from mailing import Mailing

address_to = Address("610000", "Киров", "Цветочнаяы", "6", "112")
address_from = Address("454081", "Челябинск", "проспект Победы", "117", "6")
mailing = Mailing(to_address=address_to, from_address=address_from,
                  track="RU5234584902", cost=500)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartament} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartament}. Стоимость {mailing.cost} рублей.")
