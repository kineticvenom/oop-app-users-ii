# your improved User class goes here
from datetime import date, datetime
class Users: 
    user_post={}
    def __init__(self, user_name, password, first_name=None, last_name=None, email_address=None) :  
        self.user_name = user_name
        self.name = first_name + " " + last_name
        self.email = email_address
        self._password = password
        self.posts = []
        Users.user_post[user_name] =[]

    def __str__(self):
        return str(f"Hello you can call me {self.user_name}")

    current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
    

    def NewUser_post(self, str):

        post = f"Username: {self.user_name} posted:  {str} on {Users.current_time}"
        self.posts.append(post)
        Users.user_post[self.user_name].append(post)
        return post
    
    def Delete_post(self, str):
        for post in self.posts:
            if str in post:
                self.posts.remove(post)
        for post in Users.user_post[self.user_name] :
            if str in post:
             Users.user_post[self.user_name].remove(post)
            
           
        

Kinetic = Users('kinetic','kineticvenom', 'kaleb',"varnes", 'kalebvarnes@yahoo.com')
Absol = Users('Raygo', "slipme", 'jimmy', 'brown', 'jimmybrown@gmail.com')

test = Kinetic.NewUser_post("This is starting to make sense!")
test2 = Absol.NewUser_post(" Maybe I  should play video games next?")
all_posts = Users.user_post

Kinetic.Delete_post("This is starting to make sense!")

print(Kinetic.Delete_post)
print(all_posts)