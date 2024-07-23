class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def printInfo(self):
        #f-string : 문자열을 포맷 스트링 python 3.6부터 지원
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

# 테스트 코드
def test():
    # 테스트 1: Person 클래스 인스턴스 생성 및 printInfo 확인
    person1 = Person(1, "Alice")
    person1.printInfo()

    # 테스트 2: Manager 클래스 인스턴스 생성 및 printInfo 확인
    manager1 = Manager(2, "Bob", "Project Manager")
    manager1.printInfo()

    # 테스트 3: Employee 클래스 인스턴스 생성 및 printInfo 확인
    employee1 = Employee(3, "Charlie", "Python")
    employee1.printInfo()

    # 테스트 4: Manager 클래스 인스턴스 생성 및 printInfo 확인
    manager2 = Manager(4, "David", "Product Manager")
    manager2.printInfo()

    # 테스트 5: Employee 클래스 인스턴스 생성 및 printInfo 확인
    employee2 = Employee(5, "Eve", "JavaScript")
    employee2.printInfo()

    # 테스트 6: Person 클래스 여러 인스턴스 생성 및 printInfo 확인
    person2 = Person(6, "Frank")
    person2.printInfo()

    # 테스트 7: Manager 클래스 여러 인스턴스 생성 및 printInfo 확인
    manager3 = Manager(7, "Grace", "Team Lead")
    manager3.printInfo()

    # 테스트 8: Employee 클래스 여러 인스턴스 생성 및 printInfo 확인
    employee3 = Employee(8, "Heidi", "Java")
    employee3.printInfo()

    # 테스트 9: Manager 클래스 다른 title 확인
    manager4 = Manager(9, "Ivan", "CEO")
    manager4.printInfo()

    # 테스트 10: Employee 클래스 다른 skill 확인
    employee4 = Employee(10, "Judy", "C++")
    employee4.printInfo()

# 테스트 실행
test()
