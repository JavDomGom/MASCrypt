import time
from resources.Common import Common


class Multiplication(Common):

    def integerMultiplication(self, time_exec, a, b):
        """ This method multiplies two integers. The result can be returned in
        base 2 (binary), 10 (decimal) or 16 (hexadecimal), depending on the
        self.base value.

        Attributes:
            :time_exec: Variable to control execution time.
            :a: First integer.
            :b: Second integer.

        Examples:
            :a * b:

                # Standard form:
                lm.Multiplication(base).integerMultiplication(a, b)

                # Base-2 numeral system or binary:
                lm.Multiplication(2).integerMultiplication('01011001',
                '01000011')
                # Returns 0b1011101001011

                # Base-10 numeral system or decimal:
                lm.Multiplication(10).integerMultiplication('89', '67')
                # Returns 5963

                # Base-16 numeral system or hexadecimal:
                lm.Multiplication(16).integerMultiplication('59', '43')
                # Returns 0x174b
        """
        start_time = time.time()
        res = self.baseTransform(
            int(a, self.base)*int(b, self.base)
        )
        time_exec.set(f'(time: {time.time() - start_time})')

        return res

    def modularMultiplication(self, time_exec, a, b, n):
        """ Method that performs the modular multiplication of two integers.
        The result can be returned in base 2 (binary), 10 (decimal) or 16
        (hexadecimal), depending on the self.base value.

        Attributes:
            :time_exec: Variable to control execution time.
            :a: First integer.
            :b: Second integer.
            :n: Module number.

        Examples:
            :a * b mod n:

                # Standard form:
                lm.Multiplication(base).modularMultiplication(a, b, n)

                # Base-2 numeral system or binary:
                lm.Multiplication(2).modularMultiplication('01011001',
                '01000011', '01111001')
                # Returns 0b100010

                # Base-10 numeral system or decimal:
                lm.Multiplication(10).modularMultiplication('89', '67', '121')
                # Returns 34

                # Base-16 numeral system or hexadecimal:
                lm.Multiplication(16).modularMultiplication('59', '43', '79')
                # Returns 0x22
        """
        start_time = time.time()
        res = self.baseTransform(
            (int(a, self.base)*int(b, self.base)) % int(n, self.base)
        )
        time_exec.set(f'(time: {time.time() - start_time})')

        return res
