import time
from resources.Common import Common


class GCD(Common):

    def greatestCommonDivisor(self, time_exec, *args):
        """ This method returns the greatest common divisor of all the numbers
        that you pass as argument.

        Attributes:
            :time_exec: Variable to control execution time.
            :*args: 2 or more numbers.

        Examples:
            :gdc(a, b, c, ..., n):

                # Standard form:
                lgcd.GCD(base).greatestCommonDivisor(a, b)

                # Base-2 numeral system or binary:
                lgcd.GCD(2).greatestCommonDivisor('110100011011', '1111011001')
                # Returns 0b101

                # Base-10 numeral system or ecimal:
                lgcd.GCD(10).greatestCommonDivisor('3355', '985')
                # Returns 5

                # Base-16 numeral system or hexadecimal:
                lgcd.GCD(16).greatestCommonDivisor('D1B', '3D9'))
                # Returns 0x5
        """
        from math import gcd
        from functools import reduce

        start_time = time.time()
        res = self.baseTransform(
            reduce(gcd, map(lambda n: int(n, self.base), args))
        )
        time_exec.set(f'\n(time: {time.time() - start_time})\n\n')

        return res
