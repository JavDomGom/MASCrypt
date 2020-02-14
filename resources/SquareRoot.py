import time
from resources.Common import Common


class SquareRoot(Common):

    def integerSquareRoot(self, time_exec, x):
        """ This method method returns the square root of x for x > 0. The
        result can be returned in base 2 (binary), 10 (decimal) or 16
        (hexadecimal), depending on the self.base value.

        Attributes:
            :time_exec: Variable to control execution time.
            :x: Numeric expression.

        Examples:
            :√x:

                # Standard form:
                lsr.SquareRoot(base).integerSquareRoot(a)

                # Base-2 numeral system or binary:
                lsr.SquareRoot(2).integerSquareRoot('110110011001')
                # Returns 0b111011

                # Base-10 numeral system or ecimal:
                lsr.SquareRoot(10).integerSquareRoot('3481')
                # Returns 59

                # Base-16 numeral system or hexadecimal:
                lsr.SquareRoot(16).integerSquareRoot('D99')
                # Returns 0x3b
        """
        import math

        start_time = time.time()
        res = self.baseTransform(
            int(math.sqrt(int(x, self.base)))
        )
        time_exec.set(f'(time: {time.time() - start_time})')

        return res
