class Job:
    def __init__(self, name: str, salary: float, hoursWorked: int):
        self.name = name
        self.salary = salary
        self.hoursWorked = hoursWorked

    def printPretty(self):
        print("--- JOB ---")
        print(f"{self.name}")
        print(f"{self.salary}")
        print(f"{self.hoursWorked}")

class Doctor(Job):
    def __init__(self, name: str, salary: float, hoursWorked: int, experience: int, speciality: str):
        super().__init__(
            name, salary, hoursWorked
        )
        self.experience = experience
        self.speciality = speciality

    def printPrettydoc(self):
        print(f"{self.experience}")
        print(f"{self.speciality}")

class Teacher(Job):
    def __init__(self, name: str, salary: float, hoursWorked: int, subject: str, position: str):
        super().__init__(
            name, salary, hoursWorked
        )
        self.subject = subject
        self.position = position

    def printPrettytech(self):
        print(f"{self.subject}")
        print(f"{self.position}")

print()
lawyer = Job("David", 1500, 8)
lawyer.printPretty()

print()
doctor = Doctor("Carlos", 2800, 6, 16, "Pediatric")
doctor.printPretty()
doctor.printPrettydoc()

print()
teacher = Teacher("Luis", 800, 16, "Computer Science", "Director")
teacher.printPretty()
teacher.printPrettytech()
