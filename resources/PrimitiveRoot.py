from resources.Common import Common


class PrimitiveRoot(Common):

    def gcd(self, a, b):
        ''' Return the greatest common divisor of the integers a and b. If
        either a or b is nonzero, then the value of gcd(a, b) is the largest
        positive integer that divides both a and b. gcd(0, 0) returns 0.

        Attributes:
            :a: First integer.
            :b: Second integer.
        '''
        while b != 0:
            a, b = b, a % b
        return a

    def integerPrimitiveRoot(self, n):
        ''' This method method returns the primitive root of x. The result can
        be returned in base 2 (binary), 10 (decimal) or 16 (hexadecimal),
        depending on the self.base value.

        Attributes:
            :n: Module number.

        Examples:
            :primitive root mod n:

                # Standard form:
                lpr.PrimitiveRoot(base).integerPrimitiveRoot(n)

                # Base-2 numeral system or binary:
                lpr.PrimitiveRoot(2).integerPrimitiveRoot('10000011')
                # Returns ['0b10000000', '0b1111111', ..., '0b110', '0b10']

                # Base-10 numeral system or ecimal:
                lpr.PrimitiveRoot(10).integerPrimitiveRoot('131')
                # Returns [128, 127, ..., 6, 2]

                # Base-16 numeral system or hexadecimal:
                lpr.PrimitiveRoot(16).integerPrimitiveRoot('83'))
                # Returns ['0x80', '0x7f', ..., '0x6', '0x2']
        '''
        m = int(n, self.base)
        roots = []
        required_set = set(num for num in range(1, m) if self.gcd(num, m) == 1)

        for g in range(1, m):
            actual_set = set(pow(g, powers) % m for powers in range(1, m))
            if required_set == actual_set:
                roots.append(self.baseTransform(g))

        return roots[::-1]
