#atlassian.net
#Jira
#https://qa25.atlassian.net/jira/software/projects/QA25/boards/1/roadmap
import random

class Gender:
    male = 'male'
    female = 'female'

class User:
    names = ['Sten','Ben','Den','Glen']
    surnames = ['Smith','Batler','Fisher','Butcher']
    def __init__(self,nick='',email='',password='',gender=''):
        if not gender:
            self.gender = Gender.male
        else:
            self.gender = gender
        if not nick:
            self.nick = random.choice(self.names) + '_' + random.choice(self.surnames)
        else:
            self.nick = nick
        if not email:
            self.email = (self.nick).lower() + '@gmail.com'
        else:
            self.email = email
        if not password:
            self.password = ((random.choice(self.names))[random.randint(0, 2)]).upper() + \
                        ((random.choice(self.names))[random.randint(0, 2)]).lower() + \
                        (random.choice(self.names))[random.randint(0, 2)] + \
                        str(random.randint(0, 9)) + \
                        str(random.randint(0, 9)) + \
                        str(random.randint(0, 9))
        else:
            self.password = password