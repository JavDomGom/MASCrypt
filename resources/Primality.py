import time
from resources.Common import Common


class Primality(Common):

    def is_prime(self, time_exec, n):
        """ Miller-Rabin primality test. A return value of False means n is
        certainly not prime. A return value of True means n is very likely a
        prime. The result can be returned in base 2 (binary), 10 (decimal) or
        16 (hexadecimal), depending on the self.base value.

        Attributes:
            :time_exec: Variable to control execution time.
            :n: Number to test primality.

        Examples:
            :is_prime(n):

                # Standard form:
                lp.Primality(base).is_prime(n)

                # Base-2 numeral system or binary:
                lp.Primality(2).is_prime('10111', '111001')
                # Returns 0b101110

                # Base-10 numeral system or ecimal:
                lp.Primality(10).is_prime('23', '57')
                # Returns 46

                # Base-16 numeral system or hexadecimal:
                lp.Primality(16).is_prime('17', '39'))
                # Returns 0x2e
        """
        import random

        start_time = time.time()
        n = int(n, self.base)

        if n != int(n):
            time_exec.set(f'(time: {time.time() - start_time})')

            return False

        n = int(n)

        # Miller-Rabin test for prime
        if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
            time_exec.set(f'(time: {time.time() - start_time})')

            return False

        if n == 2 or n == 3 or n == 5 or n == 7:
            time_exec.set(f'(time: {time.time() - start_time})')

            return True

        s = 0
        d = n-1

        while d % 2 == 0:
            d >>= 1
            s += 1

        assert(2 ** s * d == n - 1)

        def trial_composite(a):
            if pow(a, d, n) == 1:
                time_exec.set(f'(time: {time.time() - start_time})')

                return False

            for i in range(s):
                if pow(a, 2 ** i * d, n) == n - 1:
                    time_exec.set(f'(time: {time.time() - start_time})')

                    return False

            time_exec.set(f'(time: {time.time() - start_time})')

            return True

        for i in range(8):  # Number of trials
            a = random.randrange(2, n)
            if trial_composite(a):
                time_exec.set(f'(time: {time.time() - start_time})')

                return False

        time_exec.set(f'(time: {time.time() - start_time})')

        return True
