import overrides
from plots import ComplexFunction

class F1(ComplexFunction):
    @staticmethod
    @overrides.overrides
    def f(s: complex) -> complex:
        return (s*s - 1)/(2*s*s*s + 3*s*s - 4*s -3)

class F2(ComplexFunction):
    @staticmethod
    @overrides.overrides
    def f(s: complex) -> complex:
        return (s + 2*s**-1)/(220*s**2 + 10*s + 480 -38*s**-1 + 80*s**-2)

class Test(ComplexFunction):
    @staticmethod
    @overrides.overrides
    def f(s: complex) -> complex:
        return s

if __name__ == "__main__":

    f1 = F2()
    f1.plot_bode()
    f1.plot_laplace()
