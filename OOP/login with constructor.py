class User:
    name = ''
    email = ''
    passwords = ''
    login = False

    def __init__(self, name, email, passwords):
        self.name = name
        self.email = email
        self.passwords = passwords


    def login(self):
        email = input('Enter Your Mail :')
        passwords = input("Enter Your Passwords :")

        if email == self.email and passwords == self.passwords:
            login = True
            print("Login Successfull")
        else:
            print("Login Failed")

    def logout(self):
        login = False
        print("Logged out")

    def islogin(self):
        if self.login:
            return True
        else:
            return False

    def profile(self):
        if self.islogin():
            print(self.name, "\n", self.email)
        else:
            print("User Not Logged in")


user1 = User('abul', 'abul@mail.com', '1234') # This is how we pass paramater to constructor
user1.login()
