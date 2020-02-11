import time
from resources.Common import Common


class Factorization(Common):

    def factorization(self, time_exec, n):
        """ This method uses Pollard's rho integer factorization algorithm and
        returns a list of factors in which a number can be decomposed. The
        result can be returned in base 2 (binary), 10 (decimal) or 16
        (hexadecimal), depending on the self.base value.

        Attributes:
            :time_exec: Variable to control execution time.
            :n: Number to decompose into factors.

        Examples:
            :factorization(n):

                # Standard form:
                lf.Factorization(base).factorization(n)

                # Base-2 numeral system or binary:
                lf.Factorization(2).factorization('1010001010001100')
                # Returns ['0b100', '0b1100101', '0b1100111']

                # Base-10 numeral system or ecimal:
                lf.Factorization(10).factorization('41612')
                # Returns [4, 101, 103]

                # Base-16 numeral system or hexadecimal:
                lf.Factorization(16).factorization('A28C'))
                # Returns ['0x4', '0x65', '0x67']
        """
        from math import gcd

        start_time = time.time()
        n = int(n, self.base)
        factors = []

        def get_factor(n):
            x_fixed = 2
            cycle_size = 2
            x = 2
            factor = 1

            while factor == 1:
                for count in range(cycle_size):
                    if factor > 1:
                        break
                    x = (x * x + 1) % n
                    factor = gcd(x - x_fixed, n)

                cycle_size *= 2
                x_fixed = x

            return factor

        while n > 1:
            next = get_factor(n)
            factors.append(self.baseTransform(next))
            n //= next

        time_exec.set(f'\n(time: {time.time() - start_time})\n\n')

        return factors
