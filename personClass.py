class Person(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def set_email(self, new_email):
        self.email = new_email
        return self.email

    def set_phone(self, new_phone):
        self.phone = new_phone
        return new_phone
     
    def __str__(self):
        return 'Person[name = ' + self.name + \
               ', phone = ' + self.phone + \
               ', email = ' + self.email + \
               ']'
        

def main():
    friend = Person('husen', '6263789619', 'hxz116@gmail.com')
    print(friend)
    friend.set_email('ucfgut@gmail.com')
    friend.set_phone('240')
    print(friend)

if __name__ ==  '__main__':
    main()
