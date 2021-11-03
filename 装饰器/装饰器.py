class Cl:
    @property
    def attr(self):
        print("ok")


c = Cl()
c.attr


class Student():
    @property
    def score1(self):
        print(self._score)

    @score1.setter
    def score(self, value):
        self._score = value


s = Student()
s.score = 10
s.score
