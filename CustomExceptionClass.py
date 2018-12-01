# This is Custom Exception. There are many Built in Exceptions and Error Type in python, but you can create your own error tpye or excepiton to handle this

#I am inheriting Builtin fuction in custom class

# Note: In this class, i defined so that Vowel dont accept
# You can check other file to see how to create class so that Capital letter not accepted
class VowelNotAccepted(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status

def check_character(word):
    for char in word:
        if char.lower() in ['a','i','e','o', 'u']:
            raise VowelNotAccepted("Vowel Is not Accepted ", 101)
    return word

try:
    print(check_character('love'))
except Exception as e:
    print("error reason: " + e.message,"and status code:", e.status)