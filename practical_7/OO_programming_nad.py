###

# Example

class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

car1 = Car("Ferrari", "red", 2018)
car2 = Car("Toyota", "green", 2008)
car3 = Car("Volvo", "blue", 2024)

## Exercise

# - Hospital -

# -- Video game --

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

weapon1 = Weapon("Cannon", 120)
weapon2 = Weapon("Archer tower", 140)
weapon3 = Weapon("Wizard tower", 90)
weapon4 = Weapon("Eagle artillery", 420)
weapon5 = Weapon("Monolith", 570)

print(weapon1.name)

for weapon in [weapon1, weapon2, weapon3, weapon4, weapon5]:
    print(weapon.name, weapon.damage)

# --- University ---

# ---- Library ----

# ----- Book class -----

class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

book1 = Book("Dune", "Frank Herbert", 1965,
             ["Science fiction", "Philosophical fiction",
             "Epic", "Soft science fiction"])
book2 = Book("Hyperion", "Dan Simmons", 1989,
             ["Soft science fiction", "Space opera"])
book3 = Book("Foundation", "Isaac Asimov", 1951,
             ["Science fiction",
              "Political drama"])

print(book1.title, book1.author, book1.year, book1.genre)

for book in [book1, book2, book3]:
    print(
        book.title, book.author, book.year,
        ", ".join(book.genre)
    )

#################################################################

## Part 2 | Working with methods

# - Example -

class Parrot:
    def speak(self, text):
        print(f"Parrot says: {text}")

my_parrot = Parrot()
my_parrot.speak("Good day")
# Parrot says: Good day

# -- Exercise --

# Task 1

class Calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add(self):
        add_number = self.number1 + self.number2
        return add_number

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        multiply_numbers = self.number1 * self.number2
        return multiply_numbers

my_calc = Calculator(4, 6)
print(my_calc.add())        # 10
print(my_calc.subtract())   # -2
print(my_calc.multiply())   # 24

# Task 2

import math

# pi = 3.14

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.perimeter = self.calc_perimeter()
        self.area = self.calc_area()

    def calc_perimeter(self):
        return 2 * math.pi * self.radius
    
    def calc_area(self):
        circle_area = math.pi * self.radius ** 2
        return circle_area

input_radius = float(input("Enter the radius: "))
my_circle = Circle(input_radius)

print("Radius:", my_circle.radius)
print("Perimeter:", round(my_circle.perimeter, 2))
print("Area:", round(my_circle.area, 2))

#################################################################

## Part 3 | Classes/objects within classes

# - Exercise -

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = False
        self.borrower = None

    def __str__(self):
        if self.available:
            status = "available"
        elif self.borrower:
            status = f"borrowed by {self.borrower.name}"
        else:
            status = "not in a library"
        return f"'{self.title}' by {self.author} ({self.year}), {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        book.available = True
        print(f"Added '{book.title}' to the library.")

    @property
    def available_books(self):
        return [book for book in self.books if book.available]

    def __str__(self):
        word = "book" if len(self.books) == 1 else "books"
        return (f"Library with {len(self.books)} {word}, "
                f"{len(self.available_books)} available")


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, library, book):
        if book not in library.books:
            print(f"Sorry {self.name}, '{book.title}' is not in this library.")
        elif not book.available:
            print(f"Sorry {self.name}, '{book.title}' is already "
                  f"borrowed by {book.borrower.name}.")
        else:
            book.available = False
            book.borrower = self
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            book.borrower = None
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} hasn't borrowed '{book.title}'.")

    def __str__(self):
        titles = ", ".join(book.title for book in self.borrowed_books)
        return f"{self.name} has borrowed: {titles or 'nothing'}"

# Example usage
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
library = Library()
library.add_book(book1) # Should add book1 to the library and make it available for borrowing
member1 = Member("France")
member1.borrow_book(library, book1) # Now the book should be borrowed by France
print("Available books:", [str(book) for book in library.available_books])

# Expanded usage: things that should fail
member2 = Member("Andreja")
member2.borrow_book(library, book1)   # Sorry, already borrowed by France
member2.borrow_book(library, book2)   # Sorry, not in this library
member1.return_book(book1)            # France returned '1984'
member2.borrow_book(library, book1)   # Alice borrowed '1984'

print(book1)
print(member2)
print(library)