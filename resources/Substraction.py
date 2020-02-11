import time
from resources.Common import Common


class Substraction(Common):

    def integerSubtraction(self, time_exec, a, b):
        """ This method substract two integers. The result can be returned in
        base 2 (binary), 10 (decimal) or 16 (hexadecimal), depending on the
        self.base value.

        Attributes:
            :time_exec: Variable to control execution time.
            :a: First integer.
            :b: Second integer.

        Examples:
            :a - b:

                # Standard form:
                ls.Substraction(base).integerSubtraction(a, b)

                # Base-2 numeral system or binary:
                ls.Substraction(2).integerSubtraction('10011111', '01001101')
                # Returns 0b1010010

                # Base-10 numeral system or ecimal:
                ls.Substraction(10).integerSubtraction('159', '77')
                # Returns 82

                # Base-16 numeral system or hexadecimal:
                ls.Substraction(16).integerSubtraction('9F', '4D')
                # Returns 0x52
        """
        start_time = time.time()
        res = self.baseTransform(
            int(a, self.base)-int(b, self.base)
        )
        time_exec.set(f'\n(time: {time.time() - start_time})\n\n')

        return res

    def modularSubstraction(self, time_exec, a, b, n):
        """ Method that performs the modular substraction of two integers.
        The result can be returned in base 2 (binary), 10 (decimal) or 16
        (hexadecimal), depending on the self.base value.

        Attributes:
            :time_exec: Variable to control execution time.
            :a: First integer.
            :b: Second integer.
            :n: Module number.

        Examples:
            :a - b mod n:

                # Standard form:
                ls.Substraction(base).modularSubstraction(a, b, n)

                # Base-2 numeral system or binary:
                ls.Substraction(2).modularSubstraction('01010011', '10010110',
                '100001')
                # Returns 0b10000

                # Base-10 numeral system or decimal:
                ls.Substraction(10).modularSubstraction('83', '150', '33')
                # Returns 16

                # Base-16 numeral system or hexadecimal:
                ls.Substraction(16).modularSubstraction('53', '96', '21')
                # Returns 0x10
        """
        start_time = time.time()
        res = self.baseTransform(
            (int(a, self.base)-int(b, self.base)) % int(n, self.base)
        )
        time_exec.set(f'\n(time: {time.time() - start_time})\n\n')

        return res
