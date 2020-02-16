import time
import random
from math import gcd
from queue import Queue
from resources.Common import Common


class Factorization(Common):

    def __rabin_miller(self, p):
        if(p < 2):
            return False
        if(p != 2 and p % 2 == 0):
            return False
        s = p - 1
        while(s % 2 == 0):
            s >>= 1
        for i in range(10):
            a = random.randrange(p - 1) + 1
            temp = s
            mod = pow(a, temp, p)
            while(temp != p - 1 and mod != 1 and mod != p - 1):
                mod = (mod * mod) % p
                temp = temp * 2
            if(mod != p - 1 and temp % 2 == 0):
                return False
        return True

    def __brent(self, n):
        if(n % 2 == 0):
            return 2
        x = random.randrange(0, n)
        c = random.randrange(1, n)
        m = random.randrange(1, n)
        y, r, q = x, 1, 1
        g, ys = 0, 0
        while(True):
            x = y
            for i in range(r):
                y, k = (y * y + c) % n, 0
            while(True):
                ys = y
                for i in range(min(m, r - k)):
                    y, q = (y * y + c) % n, q * abs(x - y) % n
                g, k = gcd(q, n), k + m
                if(k >= r or g > 1):
                    break
            r = 2 * r
            if(g > 1):
                break
        if(g == n):
            while(True):
                ys, g = (x * x + c) % n, gcd(abs(x - ys), n)
                if(g > 1):
                    break
        return g

    def __pollard(self, n):
        if(n % 2 == 0):
            return 2
        x = random.randrange(2, 1000000)
        c = random.randrange(2, 1000000)
        y = x
        d = 1
        while(d == 1):
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd(x - y, n)
            if(d == n):
                break
        return d

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

                # Base-10 numeral system or decimal:
                lf.Factorization(10).factorization('41612')
                # Returns [4, 101, 103]

                # Base-16 numeral system or hexadecimal:
                lf.Factorization(16).factorization('A28C'))
                # Returns ['0x4', '0x65', '0x67']
        """
        start_time = time.time()
        n = int(n, self.base)
        q1 = Queue()
        q2 = []
        q1.put(n)
        factors = []

        while(not q1.empty()):
            x = q1.get()
            if(self.__rabin_miller(x)):
                q2.append(x)
                continue
            d = self.__pollard(x)
            if(d == x):
                q1.put(x)
            else:
                q1.put(d)
                q1.put(x//d)

        time_exec.set(f'(time: {time.time() - start_time})')

        for f in sorted(q2):
            factors.append(self.baseTransform(f))

        return factors
