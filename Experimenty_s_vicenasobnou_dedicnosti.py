class A:
    def __init__(self, n: str):
        self._nazev = n
        self._a_variable = True

    def test(self):
        return self._nazev + "-A"


class B:
    def __init__(self, n: str):
        self._nazev = n
        self._b_variable = True

    def test(self):
        return self._nazev + "-B"


class C(A, B):
    def __init__(self, n):
        super().__init__(n)


try:
    a = A("ahoj")
    b = B("ahojj")
    print(a.test())
    print(b.test())
    c = C("ahojjj")
    print(c.test())
except Exception as e:
    print(e)
