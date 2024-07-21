# classes of the WEB_EVENT project

class User:
    def __init__(self, name, surname, email, login, age, role, password):
        # ToDo self.id = generator of id
        self.name = name
        self.surname = surname
        self.email = email
        self.login = login
        self.age = age
        self.role = role
        self.password = password

    def delete(self):
        pass

    def change_password(self):
        pass

    def change_email(self):
        pass


class Organizer(User):
    def __init__(self, name, surname, email, login, age, role, password, phone_number, events_list):
        super().__init__(name, surname, email, login, age, role, password)
        self.phone_number = phone_number
        self.events_list = events_list

    def change_phone(self, new_phone_number) -> None:
        pass


class Event:
    def __init(self, title, category, date, location, description):
        self.title = title
        self.category = category
        self.date = date
        self.location = location
        self.description = description

    def get(self):
        pass

    def add(self):
        pass

    def change(self):
        pass

    def remove(self):
        pass
