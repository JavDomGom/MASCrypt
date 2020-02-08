from resources.Common import Common


class Module(Common):

    def module(self, a, b):
        ''' This method execute a modular operation between two numbers. The
        result can be returned in base 2 (binary), 10 (decimal) or 16
        (hexadecimal), depending on the self.base value.

        Attributes:
            :a: First numerical expresion.
            :b: Second numerical expresion.

        Examples:
            :a mod b:

                # Standard form:
                lmod.Module(base).module(n)

                # Base-2 numeral system or binary:
                lmod.Module(2).module('10111', '111001')
                # Returns 0b10111

                # Base-10 numeral system or ecimal:
                lmod.Module(10).module('23', '57')
                # Returns 23

                # Base-16 numeral system or hexadecimal:
                lmod.Module(16).module('17', '39'))
                # Returns 0x17
        '''
        return self.baseTransform(
            int(a, self.base) % int(b, self.base)
        )
