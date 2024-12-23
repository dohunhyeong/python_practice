from abstract_person import Person

class Farmer(Person):
    def __init__(self, name, age, fruit):
        super().__init__(name, age, job='Farmer')
        self.fruit = fruit
    
    def introduce(self):
        super().hello()
        print(f"저는 {self.fruit}를 키웁니다!")

