# locomoco — assistant bot

CLI-помічник для роботи з адресною книгою (контакти, телефони, дні народження) із збереженням даних на диск.

## Структура

```
locomoco/
├── main.py                    # точка входу
└── assistant/
    ├── domain/                # бізнес-сутності
    │   ├── fields.py          # Field, Name, Phone, Birthday, ContactCongratulation
    │   ├── record.py          # Record
    │   └── address_book.py    # AddressBook (UserDict)
    ├── storage/               # шар persistence (Strategy)
    │   ├── base.py            # StorageStrategy (ABC)
    │   └── file_storage.py    # FileStorage (pickle)
    ├── cli/                   # презентаційний шар
    │   ├── parser.py          # parse_input
    │   ├── decorators.py      # input_error, unexpected_exit
    │   ├── handlers.py        # хендлери команд
    │   └── runner.py            # головний цикл
    └── utils/
        ├── paths.py           # get_path
        └── mock.py            # seed-дані
```

## Шари

- **domain** — чисті моделі, без I/O.
- **storage** — абстракція + реалізація збереження. Щоб додати, скажімо, JSON-сховище — створіть новий клас, що наслідує `StorageStrategy`, і передайте його в `AddressBook`.
- **cli** — парсер вводу, декоратори помилок, хендлери команд, REPL.
- **utils** — допоміжні функції та фікстури.

## Запуск

```bash
python main.py
```

## Команди

- `hello` — привітання
- `add <name> <phone>` — додати контакт або телефон
- `change <name> <old_phone> <new_phone>` — змінити телефон
- `phone <name>` — показати контакт
- `all` — показати всі контакти
- `add-birthday <name> <DD.MM.YYYY>` — додати день народження
- `show-birthday <name>` — показати день народження
- `birthdays` — найближчі ДН (7 днів)
- `del <name>` — видалити контакт
- `fill` — наповнити мок-даними
- `exit` / `close` / `quit` — вихід
