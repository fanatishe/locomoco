from .field import Field
from re import sub


class Phone(Field):
    FORMATTED_LEN = 19
    COUNTRY_CODE = "+38"
    NUM_LEN = 10
    NUM_PATTERN = r"[^0-9]+"

    def __init__(self, phone):
        if not self.validate(phone):
            raise ValueError("Incorrect phone format")

        formated_phone = self.format(phone)
        super().__init__(formated_phone)

    def _get_num(self, phone: str) -> str:
        return sub(Phone.NUM_PATTERN, "", phone)

    def format(self, phone: str) -> str:
        number = self._get_num(phone)
        without_code = number[-10:]
        operator_code = without_code[0:3]

        part_1 = without_code[3:6]
        part_2 = without_code[6:8]
        part_3 = without_code[8:]

        return f"{Phone.COUNTRY_CODE} ({operator_code}) {part_1}-{part_2}-{part_3}"

    def validate(self, phone: str) -> bool:
        return len(self._get_num(phone)) == Phone.NUM_LEN
