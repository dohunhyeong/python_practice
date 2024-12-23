# 추상화 클래스 구현용 라이브러리


class Person():
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job
        
    def introduce(self):
        pass

    def hello(self):
        print(f"Hello I'm {self.name}")

    def update_age(self, age):
        if age < 0:
            raise ValueError("age should be more than ZERO")
        else:
            self.age = age
