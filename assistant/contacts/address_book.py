from collections import UserDict
from .record import Record
from .phone import Phone


class AddressBook(UserDict[str, Record]):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, query: str):
        query = query.lower()
        # пошук по всім полям
        for name, record in self.data.items():
            # перевіряємо по імені
            if query == name.lower():
                return record
            # приводимо запис до словника
            for key, value in record.to_dict().items():
                # по імені вже перевірили - пропускаємо
                if key == "Name":
                    continue
                # якщо телефони
                if key == "Phones":
                    # якщо є одразу співпадіння - вертаємо запис
                    if query in value:
                        return record
                    else:
                        # якщо телефон частково введений, то все приводимо до рядка цифрами і дивимось чи є query підрядком phone
                        for phone in value.split(","):
                            query_as_number = Phone.get_num(query)
                            if not len(query_as_number):
                                continue
                            if query_as_number in Phone.get_num(phone):
                                return record
                # по всіх інших полях перевіряємо співпадіння
                if query in value.lower():
                    return record
                
        return None
