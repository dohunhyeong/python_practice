from person import Person


class Actor(Person):
    def __init__(self, name, age, film):
        # 부모 클래스의 초기화 함수 실행
        # 부모 클래스의 init 함수 실행
        super().__init__(name, age, job="actor")
        self.film = film

    def introduce(self):
        # 부모 클래스(Person) 의 hello() 메서드 실행행
        super().hello()
        print(f"저의 대표작은 {self.film} 입니다.")