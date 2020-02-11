import time
from resources.Common import Common


class ModInverse(Common):

    def modInverse(self, time_exec, a, n):
        """ This method returns modulo inverse of a with respect to m using
        extended Euclid. Algorithm Assumption: a and m are coprimes, i.e.,
        gcd(a, m) = 1. The result can be returned in base 2 (binary), 10
        (decimal) or 16 (hexadecimal), depending on the self.base value.

        Attributes:
            :time_exec: Variable to control execution time.
            :a: First number.
            :n: Module number.

        Examples:
            :a x ≡ 1 (mod n):

                # Standard form:
                lmi.ModInverse(base).modInverse(n)

                # Base-2 numeral system or binary:
                lmi.ModInverse(2).modInverse('00000011', '00001011')
                # Returns 0b100

                # Base-10 numeral system or ecimal:
                lmi.ModInverse(10).modInverse('3', '11')
                # Returns 4

                # Base-16 numeral system or hexadecimal:
                lmi.ModInverse(16).modInverse('3', 'B'))
                # Returns 0x4
        """
        start_time = time.time()
        a = int(a, self.base)
        n = int(n, self.base)

        n0 = n
        y = 0
        x = 1

        if (n == 1):
            res = self.baseTransform(0)
            time_exec.set(f'\n(time: {time.time() - start_time})\n\n')

            return res

        while (a > 1):
            q = a // n
            t = n
            n = a % n
            a = t
            t = y
            y = x - q * y
            x = t

        if (x < 0):
            x = x + n0

        res = self.baseTransform(x)
        time_exec.set(f'\n(time: {time.time() - start_time})\n\n')

        return res
