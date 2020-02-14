import time
from resources.Common import Common


class LCM(Common):

    def lcm(self, a, b):
        from math import gcd

        return a * b // gcd(a, b)

    def leastCommonMultiple(self, time_exec, *args):
        """ This method returns the least common multiple of all the numbers
        that you pass as argument.

        Attributes:
            :time_exec: Variable to control execution time.
            :*args: 2 or more numbers.

        Examples:
            :lcm(a, b):

                # Standard form:
                llcm.LCM(base).leastCommonMultiple(a, b)

                # Base-2 numeral system or binary:
                llcm.LCM(2).leastCommonMultiple('110100011011', '1111011001')
                # Returns 0b10100001010111000111

                # Base-10 numeral system or ecimal:
                llcm.LCM(10).leastCommonMultiple('3355', '985')
                # Returns 660935

                # Base-16 numeral system or hexadecimal:
                llcm.LCM(16).leastCommonMultiple('D1B', '3D9'))
                # Returns 0xa15c7
        """
        from functools import reduce

        start_time = time.time()
        res = self.baseTransform(
            reduce(self.lcm, map(lambda n: int(n, self.base), args))
        )
        time_exec.set(f'(time: {time.time() - start_time})')

        return res
