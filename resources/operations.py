def addition(res, time_exec, base, op1, op2, module=None):
    import resources.Addition as la

    if module is None:
        res.set(
            la.Addition(base.get())
              .integerAddition(time_exec, op1.get(), op2.get())
        )
    else:
        res.set(
            la.Addition(base.get())
              .modularAddition(time_exec, op1.get(), op2.get(), module.get())
        )


def substraction(res, base, op1, op2, module=None):
    import resources.Substraction as ls

    if module is None:
        res.set(
            ls.Substraction(base.get())
              .integerSubtraction(op1.get(), op2.get())
        )
    else:
        res.set(
            ls.Substraction(base.get())
              .modularSubstraction(op1.get(), op2.get(), module.get())
        )


def multiplication(res, base, op1, op2, module=None):
    import resources.Multiplication as lm

    if module is None:
        res.set(
            lm.Multiplication(base.get())
              .integerMultiplication(op1.get(), op2.get())
        )
    else:
        res.set(
            lm.Multiplication(base.get())
              .modularMultiplication(op1.get(), op2.get(), module.get())
        )


def division(res, base, op1, op2):
    import resources.Division as ld

    res.set(
        ld.Division(base.get())
          .integerDivision(op1.get(), op2.get())
    )


def square_root(res, base, op1):
    import resources.SquareRoot as lsr

    res.set(
        lsr.SquareRoot(base.get())
           .integerSquareRoot(op1.get())
    )


def primitive_root(res, base, op1):
    import resources.PrimitiveRoot as lpr

    res.set(
        lpr.PrimitiveRoot(base.get())
           .integerPrimitiveRoot(op1.get())
    )


def xor(res, base, op1, op2):
    import resources.XOR as lxor

    res.set(
        lxor.XOR(base.get())
            .xor(op1.get(), op2.get())
    )


def mod_inverse(res, base, op1, module):
    import resources.ModInverse as lmi

    res.set(
        lmi.ModInverse(base.get())
           .modInverse(op1.get(), module.get())
    )


def exponentation(res, base, op1, op2, module=None):
    import resources.Exponentiation as le

    if module is None:
        res.set(
            le.Exponentiation(base.get())
              .integerExponentiation(op1.get(), op2.get())
        )
    else:
        res.set(
            le.Exponentiation(base.get())
              .modularExponentiation(op1.get(), op2.get(), module.get())
        )


def module(res, base, op1, module):
    import resources.Module as lmod

    res.set(
        lmod.Module(base.get())
            .module(op1.get(), module.get())
    )


def gcd(res, base, op1, op2, op3=None):
    import resources.GCD as lgcd

    if op3 is None:
        res.set(
            lgcd.GCD(base.get())
                .greatestCommonDivisor(op1.get(), op2.get())
        )
    else:
        res.set(
            lgcd.GCD(base.get())
                .greatestCommonDivisor(op1.get(), op2.get(), op3.get())
        )


def lcm(res, base, op1, op2, op3=None):
    import resources.LCM as llcm

    if op3 is None:
        res.set(
            llcm.LCM(base.get())
                .leastCommonMultiple(op1.get(), op2.get())
        )
    else:
        res.set(
            llcm.LCM(base.get())
                .leastCommonMultiple(op1.get(), op2.get(), op3.get())
        )


def primality(res, base, op1):
    import resources.Primality as lp
    if lp.Primality(base.get()).is_prime(op1.get()):
        res.set('It\'s prime')
    else:
        res.set('It\'s not prime')


def factorization(res, time_exec, base, op1):
    import resources.Factorization as lf

    res.set(
        lf.Factorization(base.get())
          .factorization(time_exec, op1.get())
    )


def discreteLogarithm(res, time_exec, base, b, y, module):
    import resources.DiscreteLogarithm as ldl

    res.set(
        ldl.DiscreteLogarithm(base.get())
           .discreteLogarithm(time_exec, b.get(), y.get(), module.get())
    )
