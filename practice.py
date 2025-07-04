class students:
    def __init__(self, n , o):
        self.name = n
        self.studying_class = o
        # self.age = "default3"
        # self.grades = "default4"

    def info(self):
        print(f"{self.name} studying in class {self.studying_class}")

rahul = students("rahul", 9)
kartik = students("kartik", 10)
parth = students("parth", 11)
rahul.info()
kartik.info()
parth.info()


