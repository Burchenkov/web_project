
class User:
    
    def __init__(self,email: str, login: str, role: str, password: str, avatar: str):
        self.email = email
        self.login = login
        self.role = role
        self.password = password
        self.avatar = avatar
        
        
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
        
        self.event_name = event_name
        self.date = date
        self.city = city
        self.title = title
        self.price = price
        self.image = image
        self.age_limit = age_limit
        self.time = time

class Comment:
    def __init__(self , data: int, text: str, ):
        self.data = data
        self.text = text   
        

        
    
        