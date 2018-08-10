# INHERITANCE:
# class Animal():
#     def __init__(self):
#         print("ANIMAL CREATED")

#     def whoAmI(self):
#         print("Animal")

#     def eat(self):
#         print("Eating")
    
#     def bark(self):
#         print("BARKING!")

# class Dog(Animal):   # inheriting from the animal class
#     def __init__(self):
#         # Animal.__init__(self)
#         print("DOG CREATED")

# mya = Animal() # Creating class
# mya.whoAmI() # running who am i method
# mya.eat()  # running eat method

# mydog = Dog()
# mydog.whoAmI()
# mydog.eat()
# mydog.bark()
# NOTICE HOW DOG DIDNT HAVE EAT OR WHOAMI METHODS IN IT, BUT WAS ABLE TO INHERIT IT FROM THE ANIMAL CLASS!



# SPECIAL METHODS:
class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Special Method: always has double under in front to signify its a special method
    # String representation =  __str__
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {} ".format(self.title, self.author, self.pages)
    
    # Length special method: Object doesnt have a length by default so we must create one under a special method
    def __len__(self):
        return self.pages

    # Delete special method: Notice how all special methods have __{name}__  The double under
    def __del__(self):
        print("a book is detroyed!")

# create book
b = Book("Python", "ryan", 200)  # inputting the name of book "python" name of author "ryan" and "200" pages
print(b)
print(len(b))

#Destroy the book!
del b  
