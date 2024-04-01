# Convert an integer to a Roman numeral
class roman_numeral:
    def __init__(self):
        self.numeral_map = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

    def convert_int(self, num):
        result = ""
        for value, numeral in self.numeral_map.items():
            while num >= value:
                result += numeral
                num -= value
        return result


print(roman_numeral().convert_int(8))

# ----------------- alternative solution ---------------------------


class solution:
    def __init__(self):
        self.numeral_map = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

    def int_to_numeral(self, num):
        i = 0
        roman = ""
        val = list(self.numeral_map.keys())
        sym = list(self.numeral_map.values())
        while num > 0:
            for x in range(num // val[i]):
                roman += sym[i]
                num -= val[i]
            i += 1
        return roman


sol = solution()
print(sol.int_to_numeral(8))


# Employee class
class Employee:
    def __init__(self, name, emp_id, salary, department):
        self.name = name
        self.id = emp_id
        self.salary = salary
        self.department = department

    def calculate_salary(self, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.salary += overtime * (self.salary / 50)

    def assign_department(self, emp_department):
        self.department = emp_department

    def print_employee_details(self):
        print(
            f"Name: {self.name}\nID: {self.id}\nSalary: ${self.salary}\nDepartment: {self.department}\n--------------"
        )


emp = Employee("Alex", 321, 3450, "CE")
emp.print_employee_details()
emp.calculate_salary(55)
emp.assign_department("SWE")
emp.print_employee_details()


# Bank Account class
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        print("-- Deposit done --")

    def withdraw(self, amount):
        if amount > self.balance:
            print("-- Failed withdraw because of low budget --")
            self.check_balance()
            return
        else:
            self.balance -= amount
            print("-- Withdraw done --")

    def check_balance(self):
        print(f"Current Balance of {self.customer_name}: {self.balance}\n")

    def print_customer_details(self):
        print(
            f"Name: {self.customer_name}\nAccount Number: {self.account_number}\nDate of opening: {self.date_of_opening}\nBalance: {self.balance}"
        )


acc1 = BankAccount(1132, 0, "12-02-1980", "Phil")
acc1.deposit(3000)
acc1.check_balance()
acc1.print_customer_details()

acc2 = BankAccount(1341, 1220, "10-12-1980", "Chris")
acc2.withdraw(2000)
acc2.print_customer_details()

acc3 = BankAccount(981, 200, "01-03-1978", "Lizzie")
acc3.withdraw(10)
acc3.print_customer_details()


# artithmetics operations using decorator functions
def addition(func):
    def wrapper(*args, **kwargs):
        print("add")
        num_sum = func(*args, **kwargs)
        print("Inside the addition function: ", num_sum)
        return num_sum + num_sum

    return wrapper


def mutliplication(func):
    def wrapper(*args, **kwargs):
        print("mul")
        num_mul = func(*args, **kwargs)
        print("Inside the multiplication function: ", num_mul)
        return num_mul * num_mul

    return wrapper


@addition
@mutliplication
def calculation(num):
    print("Inside the calculation function: ", num)
    return num


calculation(3)


# arithmetics operations for rational numbers
class RationalNumber:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):  # overloading method
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)
        numerator = (self.numerator * other.denominator) + (
            self.denominator * other.numerator
        )
        denominator = self.denominator * other.denominator
        return RationalNumber(numerator, denominator)

    def __sub__(self, other):  # overloading method
        numerator = (self.numerator * other.denominator) - (
            self.denominator * other.numerator
        )
        denominator = self.denominator * other.denominator
        return RationalNumber(numerator, denominator)

    def __mul__(self, other):  # overloading method
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return RationalNumber(numerator, denominator)

    def __truediv__(
        self, other
    ):  # overloading method (the division function in Python3)
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return RationalNumber(numerator, denominator)

    def __str__(self):
        # return f"({self.numerator}, {self.denominator})" # alternative
        return "%s/%s" % (self.numerator, self.denominator)


a = RationalNumber(1, 2)
b = RationalNumber(1, 3)

print(f"Rational Numbers: {a}, {b}")
print("-- Addition --")
print(RationalNumber.__add__(a, b))
print(a.__add__(b))
print(a + b)

print("-- Subtraction --")
print(RationalNumber.__sub__(a, b))
print(a.__sub__(b))
print(a - b)
print("-- Multiplication --")
print(RationalNumber.__mul__(a, b))
print(a.__mul__(b))
print(a * b)
print("-- Division --")
print(RationalNumber.__truediv__(a, b))
print(a.__truediv__(b))
print(a / b)


# Collatz Problem
def collatz(num):
    count = 0
    print("Number: ", num)
    print("Steps: ", count)
    print("--Start--")
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num *= 3
            num += 1
        count += 1
        print("Number: ", num)
        print("Steps: ", count)
    print("--End--")
    return count


collatz(20)

# Caesar Cipher
# The key is an integer from 1 to 25. This cipher rotates the letters of alphabet (A to Z).
# The encoding replaces each letter with the 1st to 25th next letter in alphabet (wrapping Z to A).
# So key = 2 encrypts "HI" to "JK", but key = 20 encrypts "HI" to "BC".
# (Note: ASCII code starts from A = 65 and a = 97,
#       chr() is to get character from ASCII table,
#       ord() is to get ASCII value of character.
#       English alphabet has 26 letters).

# ---------------------- ENCRYPTION ----------------------------


# A python program to illustrate Caesar Cipher Technique
def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


text = "ATTACKATONCE"
s = 4
print("Text : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s) + "\n")

# ---------------------- DECRYPTION ----------------------------


# A python program to illustrate Caesar Cipher Technique
def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Dencrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)

        # Dencrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result


text = "EXXEGOEXSRGI"
s = 4
print("Text : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))


# Student scenario
class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.skills = list()

    def student_info(self):
        return f"Fullname: {self.firstname} {self.lastname}\nSkills: {self.skills}"

    def add_skill(self, skill):
        self.skills.append(skill)


s = Student("John", "Doe")
print(s.student_info())
s.add_skill("Bowling")
s.add_skill("Swimming")
print(f"\n{s.student_info()}")


# Employee scenario
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def employee_info(self):
        return f"Name: {self.__name}\nSalary: {self.__salary}"

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary


e = Employee("John", 2950)
print(e.employee_info())
print("\nThe salary of %s is %s" % (e.get_name(), e.get_salary()))

# Check user info


# Custom exceptions
class DuplicateUsernameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class UnderageError(Exception):
    pass


class InvalidEmailError(Exception):
    pass


# A class for a user's data
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return "Username: %s\nEmail: %s" % (self.username, self.email)


example_list = [
    ("jane", "jane@example.com", 21),
    ("bob", "bob@example.com", 19),
    ("jane", "jane2@example.com", 25),
    ("steve", "steve@example.com", 15),
    ("joe", "joe", 23),
    ("anna", "anna@example.com", -3),
]

directory = {}

for username, email, age in example_list:
    try:
        if username in directory:
            raise DuplicateUsernameError()
        if age < 0:
            raise InvalidAgeError()
        if age < 16:
            raise UnderageError()

        email_parts = email.split("@")
        if len(email_parts) != 2 or not email_parts[0] or not email_parts[1]:
            raise InvalidEmailError()
    except DuplicateUsernameError:
        print("Username '%s' is in use." % username)
    except InvalidAgeError:
        print("Invalid age: %d" % age)
    except UnderageError:
        print("User %s is underage." % username)
    except InvalidEmailError:
        print("%s is not a valid email address." % email)
    # if no exception occured
    else:
        directory[username] = User(username, email)

# Print objects
print("-------------------------")
for user in directory.values():
    print("Username: %s" % user.username)
    print("Email: %s" % user.email)
print("-------------------------")
for key, val in directory.items():
    print("Key: %s" % key)
    print("Value: \n%s" % val)
    print("---")

# Song list


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self) -> str:
        return self.name


class Artist:
    def __init__(self, name):
        self.name = name

        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self) -> str:
        return self.name


class Album:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        self.tracks = []

        artist.add_album(self)

    def add_track(self, title, artist=None):
        if artist is None:
            artist = self.artist
        track_number = len(self.tracks)
        song = Song(title, artist, self, track_number)
        self.tracks.append(song)

    def __str__(self) -> str:
        return f"{self.title} ({self.year})"


class Song:
    def __init__(self, title, artist, album, track_number):
        self.title = title
        self.artist = artist
        self.album = album
        self.track_number = track_number

        artist.add_song(self)

    def __str__(self) -> str:
        return f"Title: {self.title}\nArtist: {self.artist}\nAlbum: {self.album}\nTrack #: {self.track_number}"


# Create objects
band = Artist("Bob's Awesome Band")
album = Album("Bob's First Single", band, 2013)
album.add_track("A Ballad about Cheese")
album.add_track("A Ballad about Cheese (dance remix)")
album.add_track("A Third Song to Use Up the Rest of the Space")

playlist = Playlist("My Favourite Songs")

for song in album.tracks:
    playlist.add_song(song)

# Print
for song in album.tracks:
    print(song)
    print("---")
