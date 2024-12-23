from person import Person


class Actor(Person):
    def __init__(self, name, age, film):
        super().__init__(name, age, job="actor")
        self.film = film

    def introduce(self):
        print(f"저의 대표작은 {self.film} 입니다.")