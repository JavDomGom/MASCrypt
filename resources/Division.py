from resources.Common import Common


class Division(Common):

    def bin2float(self, b):
        ''' Convert binary string to a float.

        Attributes:
            :b: Binary string to transform.
        '''
        import struct

        f = int(b, 2).to_bytes(8, byteorder='big')

        return struct.unpack('>d', f)[0]

    def float2bin(self, f):
        ''' Convert float to 64-bit binary string.

        Attributes:
            :f: Float number to transform.
        '''
        import struct

        [d] = struct.unpack('>Q', struct.pack('>d', f))

        return f'0b{d:064b}'

    def hex2float(self, h):
        ''' Convert hexadecimal string to a float.

        Attributes:
            :h: Hexadecimal string to transform.
        '''
        import struct

        return struct.unpack('>f', bytes.fromhex(h))[0]

    def float2hex(self, f):
        ''' Convert float to hexadecimal string.

        Attributes:
            :f: Float number to transform.
        '''
        import struct

        return hex(struct.unpack('<I', struct.pack('<f', f))[0])

    def integerDivision(self, a, b):
        ''' This method divides two integers. The result can be returned in
        base 2 (binary), 10 (decimal) or 16 (hexadecimal), depending on the
        self.base value.

        Attributes:
            :a: First integer.
            :b: Second integer.

        Examples:
            :a / b:

                # Standard form:
                ld.Division(base).integerDivision(a, b)

                # Base-2 numeral system or binary:
                ld.Division(2).integerDivision('01011001', '01000011')
                # Returns 0b00111111111101010100000011110100100010011000110101011
                11110000110

                # Base-10 numeral system or decimal:
                ld.Division(10).integerDivision('89', '67')
                # Returns 1.328358208955224

                # Base-16 numeral system or hexadecimal:
                ld.Division(16).integerDivision('59', '43')
                # Returns 0x3faa07a4
        '''
        float_result = int(a, self.base)/int(b, self.base)

        if self.base == 2:
            return self.float2bin(float_result)
        elif self.base == 10:
            return float_result
        elif self.base == 16:
            return self.float2hex(float_result)
