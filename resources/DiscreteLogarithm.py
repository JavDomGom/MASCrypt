from resources.Common import Common


class DiscreteLogarithm(Common):

    def discreteLogarithm(self, a, y, n, N=None):
        ''' This method executes the discrete logarithm problem and returns the
        value of X. The result can be returned in base 2 (binary), 10 (decimal)
        or 16 (hexadecimal), depending on the self.base value.

        Attributes:
            :a: Base.
            :y: Power.
            :n: Module.

        Examples:
            :discreteLogarithm(a, y, n):

                # Standard form:
                ldl.DiscreteLogarithm(base).discreteLogarithm(a, y, n)

                # Base-2 numeral system or binary:
                ldl.DiscreteLogarithm(2).discreteLogarithm('10', '111001',
                '1111010111')
                # Returns 0b10000010

                # Base-10 numeral system or ecimal:
                ldl.DiscreteLogarithm(10).discreteLogarithm('2', '57', '983')
                # Returns 130

                # Base-16 numeral system or hexadecimal:
                ldl.DiscreteLogarithm(16).discreteLogarithm('2', '39', '3D7'))
                # Returns 0x82
        '''
        from math import sqrt

        a = int(a, self.base)
        y = int(y, self.base)
        n = int(n, self.base)

        if not N:
            N = 1 + int(sqrt(n))

        baby_steps = {}
        baby_step = 1
        for r in range(N+1):
            baby_steps[baby_step] = r
            baby_step = baby_step * a % n

        giant_stride = pow(a, (n-2)*N, n)
        giant_step = y
        for q in range(N+1):
            if giant_step in baby_steps:
                return self.baseTransform(
                    q*N + baby_steps[giant_step]
                )
            else:
                giant_step = giant_step * giant_stride % n

        return 'No Match'
