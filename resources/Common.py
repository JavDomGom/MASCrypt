class Common():

    def __init__(self, base):
        ''' Class constructor.

        Attributes:
            :base: The numerical base to be used in class calculations.
        '''
        self.base = base

    def baseTransform(self, x):
        ''' Method that receives a int() number, and depending on the self.base
        value transforms it to bin(), int() or hex().

        Attributes:
            :x: int() number to transform.
        '''
        if self.base == 2:
            return bin(x)
        elif self.base == 10:
            return int(x)
        elif self.base == 16:
            return hex(x)
