# your improved User class goes here
class Users: 
    def __init__(self, user_name, first_name=None, last_name=None, email_address=None, password) :  
        self.user_name = user_name
        self.name = first_name + " " + last_name
        self.email = email_address
        self._password = password
    
    def __str__(self):
        return f"Username: {self.user_name} Name:{self.name} Email:{self.email}"


Kinetic = Users('kinetic', 'kaleb', 'kalebvarnes@yahoo.com', 'kineticvenom')