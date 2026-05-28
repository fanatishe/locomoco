from collections import UserDict
from .record import Record
from .phone import Phone
from .birthday import Birthday, ContactCongratulation
from datetime import date, timedelta


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

    
    def get_upcoming_birthdays(self, from_date = None, within=7) -> list[ContactCongratulation]:
        weekdays = (5, 6) 
        today_date = date.today()

        if from_date is not None:
            today_date = date.strptime(from_date, Birthday.DATE_FORMAT)
        
        current_year = today_date.year
        bd_list = []
        for name, record in self.data.items():
            if record.birthday is None:
                continue

            birth_date = record.birthday.value
            congrats_date = birth_date.replace(year = current_year)

            if congrats_date < today_date:
                congrats_date = congrats_date.replace(year = current_year + 1)

            days_left = (congrats_date - today_date).days
            
            if days_left in [i for i in range(within)]:
                weekday = congrats_date.weekday()
                if weekday in weekdays:
                    congrats_date = congrats_date + timedelta(days = 7 - weekday)

                bd_list.append(ContactCongratulation(congrats_date.strftime(Birthday.DATE_FORMAT), name))   

        return bd_list
    
    def show_upcoming_birthdays(self, from_date = None, within=7):
        bd_list = self.get_upcoming_birthdays(from_date, within)
        for bd in bd_list:
            print(bd)

