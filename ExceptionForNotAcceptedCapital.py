# Creating Exception class not to accept Capital latter

class CapitalNotAccepted(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status

# Above Fuction are Constructor you know, lol

def char_check(word):
    for char in word:
        if char.upper() in ['A','I','E','O', 'U']:
            raise CapitalNotAccepted("Capital Letter will not be accepted", 101)
    return word

try:
    print(char_check("ABC"))
except Exception as e:
    print("The Error reasion is: " + e.message, e.status)
finally:
    print("Finally The Custom Exception class excuated")