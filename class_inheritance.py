

class User :       #creates a Parent class called User and defines charactersictics
    name = '    '
    mailing_address = '    '
    email = '    '
    phone = '    '
    password = '    '
    user_id = 0

class Teacher(User) : #creates a child class called teacher that inherits user properties plus teacher properties
    base_pay = 30.00
    department = '  '

class Student(User) : #creates a child class called student that inherits user properties plus student properties
    class_id = '    '
    grade = '    '
    legal_guardian_name = '    '
    legal_guardian_phone = '    '
