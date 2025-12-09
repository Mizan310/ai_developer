# Inheritance--> allows new one class (chiled) to reuse the property and methods of another class (parent)

# Python-এ inheritance (উত্তরাধিকার) হলো অবজেক্ট-অরিয়েন্টেড প্রোগ্রামিং (OOP)-এর একটি মৌলিক ধারণা। এর মাধ্যমে একটি ক্লাস (child class) 
# অন্য একটি ক্লাস (parent class) থেকে বৈশিষ্ট্য (attributes) এবং আচরণ (methods) উত্তরাধিকার সূত্রে লাভ করতে পারে। এটি কোড পুনঃব্যবহার 
# (code reusability) এবং একটি নির্দিষ্ট শ্রেণিবিন্যাস (hierarchical structure) তৈরিতে সহায়তা করে।

# Inheritance কিভাবে কাজ করে?
# যখন একটি ক্লাস অন্য ক্লাস থেকে উত্তরাধিকার লাভ করে, তখন সে parent class-এর সমস্ত পাবলিক (public) এবং প্রোটেক্টেড (protected) 
# অ্যাট্রিবিউট ও মেথড ব্যবহার করতে পারে। Child class চাইলে parent class-এর বৈশিষ্ট্যগুলোকে নতুন বৈশিষ্ট্য যুক্ত করে বা বিদ্যমান বৈশিষ্ট্যগুলোকে 
# পরিবর্তন (override) করে প্রসারিত করতে পারে।

# This is *parent class*
class Student:
    def __init__(self, name, grade, percentage): # This is fun/method
        self.name = name # attribute, self.name = property(name)
        self.grade = grade # attribute, self.name = property(grade)
        self.percentage = percentage # attribute, self.name = property(grade) # double underscore, limits access (private kore rakha)
    def student_details(self): 
        print(f"{self.name} is in class {self.grade} and the percentage is {self.percentage}%")


# object - instances of class
student1 = Student("Mizanur", 11, 89)
# print(student1.name, student1.grade)
student1.student_details() # object.method - it call the method my passing class parameters abd print the method

student2 = Student("Rahman", 12, 67)
# print(student2.name, student2.grade)
student2.student_details() # object.method - it call the method my passing class parameters abd print the method


# child Class
class GraduateStudent(Student): # GraduateStudent is a child class, who inherit property and methods from student parent class
    def __init__(self, name, grade, percentage, stream): # Passes all parameters from parent class and added new parameter in child class(it include for our work)
        super().__init__(name, grade, percentage) # it calling parent class __init__ (initializer)
        self.stream = stream 

    def grad_student_details(self): # method - abstraction and polymorphism
        print(f'{self.name} is in {self.grade} class and got avg {self.percentage} and stream is {self.stream}')

    def student_details(self): # method - inheritance 
        super().student_details() # (It has a another name: method overriding Feature: Child class-এ parent class-এর মেথডের signature (নাম ও প্যারামিটার) একই রেখে নতুন implementation যোগ করা।)
        print(f'Stream is {self.stream}')

# object
Grad_stu1 = GraduateStudent('Adnan', 12, 96, 'PCM')
# print(Grad_student1.stream)
Grad_stu1.grad_student_details() # by calling abstraction function
Grad_stu1.student_details() # by calling inheritance function

