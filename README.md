# Personal Assistant CLI

## Description

A command-line interface (CLI) assistant designed to help you manage your contacts (phone numbers, emails, physical addresses, birthdays) and text notes with tags. Built with Python, the application features an interactive terminal UI with smart auto-completion and beautiful table rendering.

## Key Features

- **Contact Management:** Create, edit, search, and delete contacts.
- **Smart Data Validation:** Ensures phone numbers contain exactly 10 digits and emails follow standard formats.
- **Birthday Tracking:** Search contacts by specific birthday dates or find upcoming birthdays within a specified number of days.
- **Notebook & Tags:** Save text notes, categorize them with tags, and sort or search through your notebook.
- **Persistent Storage:** Data is automatically saved to your hard drive (`~/.personal_assistant`) and restored upon restart.
- **Interactive CLI:** Supports Tab/Right-Arrow auto-completion and visually appealing data tables.

## Installation

Ensure you have Python 3.10+ installed on your system.

1. Clone the repository.

2. Navigate to the project directory.

3. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To start the Personal Assistant, simply run the main script:

```bash
python main.py
```

Once the application starts, you can type commands to interact with the assistant. Press `TAB` or the `RIGHT ARROW` key to auto-complete commands.

## Command Reference

### General

| Command | Description |
|---|---|
| `hello` | Greet the assistant |
| `help` | Show main help menu or use `help <command>` for specific details |
| `all` | Show all contacts |
| `exit` / `close` | Close the application and save data |

### Contacts (General)

| Command | Description |
|---|---|
| `contact add <name> [phone] [birthday]` | Create a new contact |
| `contact change <old_name> <new_name>` | Rename a contact |
| `contact delete <name>` | Delete a contact completely |
| `contact search [<name>]` | Search contacts by name |

### Phones, Emails, Addresses & Birthdays

| Command | Description |
|---|---|
| `contact <field> add <name> <value>` | Add a new record (phone/email) |
| `contact <field> set <name> <value>` | Set a single record (birthday/address) |
| `contact <field> change <name> <old> <new>` | Update an existing record |
| `contact <field> delete <name> <value>` | Remove a record from a contact |
| `contact <field> search <query>` | Find contacts by value (e.g., upcoming birthdays: `contact birthday search 7`) |

### Notes & Tags

| Command | Description |
|---|---|
| `note add <title> <text>` | Create a new text note |
| `note change <id> <text>` | Edit note text |
| `note delete <id>` | Delete a note |
| `note search <keyword>` | Search notes by text |
| `note tag add <id> <tag>` | Add a tag to a note |
| `note tag search <tag>` | Search notes by tag |
| `note tag sort` | Sort notes alphabetically by tags |
