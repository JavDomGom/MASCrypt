from resources.Common import Common


class XOR(Common):

    def xor(self, a, b):
        ''' This method execute a XOR operation between two numbers. The result
        can be returned in base 2 (binary), 10 (decimal) or 16 (hexadecimal),
        depending on the self.base value.

        Attributes:
            :a: First numerical expresion.
            :b: Second numerical expresion.

        Examples:
            :a XOR b:

                # Standard form:
                lpr.XOR(base).xor(n)

                # Base-2 numeral system or binary:
                lpr.XOR(2).xor('10111', '111001')
                # Returns 0b101110

                # Base-10 numeral system or ecimal:
                lpr.XOR(10).xor('23', '57')
                # Returns 46

                # Base-16 numeral system or hexadecimal:
                lpr.XOR(16).xor('17', '39'))
                # Returns 0x2e
        '''
        return self.baseTransform(
            int(a, self.base) ^ int(b, self.base)
        )
