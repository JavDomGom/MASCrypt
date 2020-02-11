import time
from resources.Common import Common


class Module(Common):

    def module(self, time_exec, a, b):
        """ This method execute a modular operation between two numbers. The
        result can be returned in base 2 (binary), 10 (decimal) or 16
        (hexadecimal), depending on the self.base value.

        Attributes:
            :time_exec: Variable to control execution time.
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
        """
        start_time = time.time()
        res = self.baseTransform(
            int(a, self.base) % int(b, self.base)
        )
        time_exec.set(f'\n(time: {time.time() - start_time})\n\n')

        return res
