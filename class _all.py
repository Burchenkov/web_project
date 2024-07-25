
import hashlib
from datetime import datetime

class User:
    user_id = 1  # переменная для хранения ID пользователей
    users = {}  # Хеш-таблица для хранения пользователей

    def __init__(self, email: str, login: str, role: str, password: str, avatar: str):
        self.email = email #!!!
        self.login = login#!!!
        self.role = role#!!!
        self.password = self.encrypt_password(password) #!!! # Шифруем пароль
        self.avatar = avatar#!!!
        self.id = User.user_id#!!!  # Присваиваем ID пользователю
        User.users[self.id] = self  #Добавляем пользователя в хеш-таблицу
        User.user_id += 1  # Увеличиваем ID для следующего пользователя

    @classmethod
    def login(cls, login: str, password: str):  # Проверка логина и пароля пользователя (верны ли они)
        for user in cls.users.values():
            if user.login == login and user.decrypt_password(password) == user.password:
                return user
        print("Логин или пароль неверны")  # Выводим сообщение, если логин и пароль неверны
        return None

    def encrypt_password(self, password: str) ->str:
        # Шифруем пароль с помощью SHA-256
        return hashlib.sha256(password.encode()).hexdigest()




        
class Organizer(User):
    def __init__(self, email: str, login: str, role: str, password: str,image: str, name: str, surname: str):
        super().__init__(email, login, role, password , image)
        self.events = []

    def add_event(self, event: 'Event'): # Добавляет мероприятие
        if isinstance(event, Event): # проверка, является ли объект event экземпляром класса Event
            self.events.append(event) # добавляет мероприятие в конец списка 
       
    def remove_event(self, event: 'Event'): # Удаляем мероприятие.
        if event in self.events: # проверка есть ли мероприятие 
            self.events.remove(event) # удаляем
        
   
class Event:
    #MAX_SIZE = 1000  # байт

    def __init__(self, event_name: str, date: int, city: str, title: str, price: str, image: str, age_limit: int, time: int):
        
        self.event_name = event_name#!!!
        self.date = date#!!!
        self.city = city#!!!
        self.title = title#!!!
        self.price = price#!!!
        self.image = image#!!!
        self.age_limit = age_limit#!!!
        self.time = time#!!!



class Comment(User):
    def __init__(self, email: str, login: str, role: str, password: str, avatar: str, rating: int, text: str, image: str):
        super().__init__(email, login, role, password, avatar)
        self.rating = rating
        self.text = text
        self.image = image
        self.created_at = datetime.now()  # Добавляем дату и время написания

    def __str__(self):
        return f"Email: {self.email}\nLogin: {self.login}\nRole: {self.role}\nAvatar: {self.avatar}\nRating: {self.rating}\nText: {self.text}\nImage: {self.image}\nCreated at: {self.created_at}"
  
        

        
    
        
