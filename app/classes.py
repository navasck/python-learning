class User:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello {self.name}")


user1 = User("Abdul")

user1.say_hello()