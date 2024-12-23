from abstract_person import Person


class Actor(Person):
    def __init__(self, name, age, film):
        # 부모 클래스의 초기화 함수 실행
        # 부모 클래스의 init 함수 실행
        super().__init__(name, age, job="actor")
        self.film = film
    # 추상클래스(Person)를 상속받은 클래스의 경우에는 추상메서드를 직접 구현해줘야 한다.
    def introduce(self):
        # 부모 클래스(Person) 의 hello() 메서드 실행행
        super().hello()
        print(f"저의 대표작은 {self.film} 입니다.")