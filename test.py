import unittest
import resources.Addition as la
import resources.Substraction as ls
import resources.Multiplication as lm
import resources.Division as ld
import resources.SquareRoot as lsr
import resources.PrimitiveRoot as lpr
import resources.XOR as lxor
import resources.ModInverse as lmi
import resources.Exponentiation as le
import resources.Module as lmod
import resources.GCD as lgcd
import resources.LCM as llcm
import resources.Primality as lp
import resources.Factorization as lf
import resources.DiscreteLogarithm as ldl

class StringVar(): 
    def set(self,_): pass

class MASCryptTest(unittest.TestCase):

    time_exec = StringVar()

    def test_addition_bin(self):
        """ Test binary addition operation. """
        a = '1000100001100000001111010011101000110110100001100000001100001010\
101'
        b = '100011111001101000101010011110010111001101110'
        res = '0b1000100001100000001111110111100010011111001011111110100011011\
000011'
        self.assertEqual(
            res,
            la.Addition(2).integerAddition(self.time_exec, a, b)
        )

    def test_addition_dec(self):
        """ Test decimal addition operation. """
        a = '78615373657236576341'
        b = '19736537542254'
        res = 78615393393774118595
        self.assertEqual(
            res,
            la.Addition(10).integerAddition(self.time_exec, a, b)
        )

    def test_addition_hex(self):
        """ Test hexadecimal addition operation. """
        a = '44301E9D1B4301855'
        b = '11F3454F2E6E'
        res = '0x44301FBC4F97F46C3'.lower()
        self.assertEqual(
            res,
            la.Addition(16).integerAddition(self.time_exec, a, b)
        )

    def test_addition_mod_bin(self):
        """ Test binary modular addition operation. """
        a = '1000100001100000001111010011101000110110100001100000001100001010\
101'
        b = '100011111001101000101010011110010111001101110'
        n = '11000001100001001100100110101011011010111101101001001010100'
        res = '0b1001110111000011010110000010111010110100110110001110110011'
        self.assertEqual(
            res,
            la.Addition(2).modularAddition(self.time_exec, a, b, n)
        )

    def test_addition_mod_dec(self):
        """ Test decimal modular addition operation. """
        a = '78615373657236576341'
        b = '19736537542254'
        n = '435765377635373652'
        res = 177625419406861235
        self.assertEqual(
            res,
            la.Addition(10).modularAddition(self.time_exec, a, b, n)
        )

    def test_addition_mod_hex(self):
        """ Test hexadecimal modular addition operation. """
        a = '44301E9D1B4301855'
        b = '11F3454F2E6E'
        n = '60C264D5B5ED254'
        res = '0x2770D60BAD363B3'.lower()
        self.assertEqual(
            res,
            la.Addition(16).modularAddition(self.time_exec, a, b, n)
        )

    def test_substraction_bin(self):
        """ Test binary substraction operation. """
        a = '1110111001001011110000001101011110010100111001111011101011010000\
10111100'
        b = '1110001101000010110000100101110000111100001010101101100110011011'
        res = '0b111011010110100001111110000101010011100010101011100011111111\
011100100001'
        self.assertEqual(
            res,
            ls.Substraction(2).integerSubtraction(self.time_exec, a, b)
        )

    def test_substraction_dec(self):
        """ Test decimal substraction operation. """
        a = '4395783689325789237436'
        b = '16375864896474765723'
        res = 4379407824429314471713
        self.assertEqual(
            res,
            ls.Substraction(10).integerSubtraction(self.time_exec, a, b)
        )

    def test_substraction_hex(self):
        """ Test hexadecimal substraction operation. """
        a = 'EE4BC0D794E7BAD0BC'
        b = 'E342C25C3C2AD99B'
        res = '0xED687E1538AB8FF721'.lower()
        self.assertEqual(
            res,
            ls.Substraction(16).integerSubtraction(self.time_exec, a, b)
        )

    def test_substraction_mod_bin(self):
        """ Test binary modular substraction operation. """
        a = '1110111001001011110000001101011110010100111001111011101011010000\
10111100'
        b = '1110001101000010110000100101110000111100001010101101100110011011'
        n = '1100101100111100101010110011011001100011111111100110010010110011\
001011'
        res = '0b100010001010111101001011011110110101001010110100101011010000\
1111110101'
        self.assertEqual(
            res,
            ls.Substraction(2).modularSubstraction(self.time_exec, a, b, n)
        )

    def test_substraction_mod_dec(self):
        """ Test decimal modular substraction operation. """
        a = '4395783689325789237436'
        b = '16375864896474765723'
        n = '937265173657357462731'
        res = 630347129799884620789
        self.assertEqual(
            res,
            ls.Substraction(10).modularSubstraction(self.time_exec, a, b, n)
        )

    def test_substraction_mod_hex(self):
        """ Test hexadecimal modular substraction operation. """
        a = 'EE4BC0D794E7BAD0BC'
        b = 'E342C25C3C2AD99B'
        n = '32CF2ACD98FF992CCB'
        res = '0x222BD2DED4AD2B43F5'.lower()
        self.assertEqual(
            res,
            ls.Substraction(16).modularSubstraction(self.time_exec, a, b, n)
        )

    def test_multiplication_bin(self):
        """ Test binary multiplication operation. """
        a = '10000101100110011000110100010111111111110101010011100010110111011'
        b = '1010101001011101000011001011101111010100100111011101011'
        res = '0b101100011101000100001110001111101101010000000101101100010101\
11011000010001101111000110000101100000001010111110010101001'
        self.assertEqual(
            res,
            lm.Multiplication(2).integerMultiplication(self.time_exec, a, b)
        )

    def test_multiplication_dec(self):
        """ Test decimal multiplication operation. """
        a = '19253761625377326523'
        b = '23976527656537835'
        res = 461638348103246327697836634498497705
        self.assertEqual(
            res,
            lm.Multiplication(10).integerMultiplication(self.time_exec, a, b)
        )

    def test_multiplication_hex(self):
        """ Test hexadecimal multiplication operation. """
        a = '10B331A2FFEA9C5BB'
        b = '552E865DEA4EEB'
        res = '0x58E8871F6A02D8AEC2378C2C057CA9'.lower()
        self.assertEqual(
            res,
            lm.Multiplication(16).integerMultiplication(self.time_exec, a, b)
        )

    def test_multiplication_mod_bin(self):
        """ Test binary modular multiplication operation. """
        a = '10000101100110011000110100010111111111110101010011100010110111011'
        b = '1010101001011101000011001011101111010100100111011101011'
        n = '1001011111000110110011011110101110110001010011010110101101010001\
0101000001111111101010'
        res = '0b111110101111111110001111110010101011011101010001101110010110\
0100100001101110100011'
        self.assertEqual(
            res,
            lm.Multiplication(2).modularMultiplication(self.time_exec, a, b, n)
        )

    def test_multiplication_mod_dec(self):
        """ Test decimal modular multiplication operation. """
        a = '19253761625377326523'
        b = '23976527656537835'
        n = '45871656472848274675736554'
        res = 4741223607006646355762083
        self.assertEqual(
            res,
            lm.Multiplication(10).modularMultiplication(
                self.time_exec, a, b, n
            )
        )

    def test_multiplication_mod_hex(self):
        """ Test hexadecimal modular multiplication operation. """
        a = '10B331A2FFEA9C5BB'
        b = '552E865DEA4EEB'
        n = '25F1B37AEC535AD4541FEA'
        res = '0x3EBFE3F2ADD46E5921BA3'.lower()
        self.assertEqual(
            res,
            lm.Multiplication(16).modularMultiplication(
                self.time_exec, a, b, n
            )
        )

    def test_division_bin(self):
        """ Test binary division operation. """
        a = '1100000011100100001110000010101110110101110101000111001110111011\
01010100001100011101001100'
        b = '1000011101001111111101111111100011101001001100001111100011001000\
0110100001001100101111110'
        res = '0b010000000000011011001110111101011010101011000111110011010000\
1010'
        self.assertEqual(
            res,
            ld.Division(2).integerDivision(self.time_exec, a, b)
        )

    def test_division_dec(self):
        """ Test decimal division operation. """
        a = '932765972365713265327654732'
        b = '327165253763657365736954238'
        res = 2.851054510328713
        self.assertEqual(
            res,
            ld.Division(10).integerDivision(self.time_exec, a, b)
        )

    def test_division_hex(self):
        """ Test hexadecimal division operation. """
        a = '30390E0AED751CEED50C74C'
        b = '10E9FEFF1D261F190D0997E'
        res = '0x403677AD'.lower()
        self.assertEqual(
            res,
            ld.Division(16).integerDivision(self.time_exec, a, b)
        )

    def test_square_root_bin(self):
        """ Test binary square root operation. """
        a = '1000110111000101000111011001010011011101100001010110000110001000\
110111010100010010'
        res = '0b10111110100000011110110011100101001110101'
        self.assertEqual(
            res,
            lsr.SquareRoot(2).integerSquareRoot(self.time_exec, a)
        )

    def test_square_root_dec(self):
        """ Test decimal square root operation. """
        a = '2677959256956917386540306'
        res = 1636447144565
        self.assertEqual(
            res,
            lsr.SquareRoot(10).integerSquareRoot(self.time_exec, a)
        )

    def test_square_root_dec_float_precision_limit(self):
        """ Test decimal square root operation in float precision limit. """
        a = '263836759585588630746'
        res = 16243052655 # 16243052655.99999927384339325
        self.assertEqual(
            res,
            lsr.SquareRoot(10).integerSquareRoot(self.time_exec, a)
        )

    def test_square_root_hex(self):
        """ Test hexadecimal square root operation. """
        a = '237147653761586237512'
        res = '0x17D03D9CA75'.lower()
        self.assertEqual(
            res,
            lsr.SquareRoot(16).integerSquareRoot(self.time_exec, a)
        )

    def test_primitive_root_bin(self):
        """ Test binary primitive root operation. """
        a = '10000011'
        res = ['0b10000000', '0b1111111', '0b1111110', '0b1111100',
               '0b1111010', '0b1111000', '0b1110111', '0b1110110',
               '0b1110100', '0b1110011', '0b1101111', '0b1101110',
               '0b1101010', '0b1101000', '0b1100111', '0b1100010',
               '0b1100001', '0b1100000', '0b1011111', '0b1011101',
               '0b1011010', '0b1011000', '0b1010111', '0b1010101',
               '0b1010011', '0b1010010', '0b1001100', '0b1001000',
               '0b1000011', '0b1000010', '0b111001', '0b111000',
               '0b110110', '0b110010', '0b101000', '0b100101',
               '0b11111', '0b11110', '0b11101', '0b11010', '0b10111',
               '0b10110', '0b10001', '0b1110', '0b1010', '0b1000',
               '0b110', '0b10']
        self.assertEqual(
            res,
            lpr.PrimitiveRoot(2).integerPrimitiveRoot(self.time_exec, a)
        )

    def test_primitive_root_dec(self):
        """ Test decimal primitive root operation. """
        a = '131'
        res = [128, 127, 126, 124, 122, 120, 119, 118, 116, 115, 111, 110, 106,
               104, 103, 98, 97, 96, 95, 93, 90, 88, 87, 85, 83, 82, 76, 72,
               67, 66, 57, 56, 54, 50, 40, 37, 31, 30, 29, 26, 23, 22, 17, 14,
               10, 8, 6, 2]
        self.assertEqual(
            res,
            lpr.PrimitiveRoot(10).integerPrimitiveRoot(self.time_exec, a)
        )

    def test_primitive_root_hex(self):
        """ Test hexadecimal primitive root operation. """
        a = '83'
        res = ['0x80', '0x7f', '0x7e', '0x7c', '0x7a', '0x78', '0x77', '0x76',
               '0x74', '0x73', '0x6f', '0x6e', '0x6a', '0x68', '0x67', '0x62',
               '0x61', '0x60', '0x5f', '0x5d', '0x5a', '0x58', '0x57', '0x55',
               '0x53', '0x52', '0x4c', '0x48', '0x43', '0x42', '0x39', '0x38',
               '0x36', '0x32', '0x28', '0x25', '0x1f', '0x1e', '0x1d', '0x1a',
               '0x17', '0x16', '0x11', '0xe', '0xa', '0x8', '0x6', '0x2']
        self.assertEqual(
            res,
            lpr.PrimitiveRoot(16).integerPrimitiveRoot(self.time_exec, a)
        )

    def test_xor_bin(self):
        """ Test binary XOR operation. """
        a = '0011101011100010001001010001000110011100001111010000101111010001\
101110100100011000110110111110101100'
        b = '1011100110000101010001111010100001011101101101100111010101101100\
000000110110000010110101100011011111'
        res = '0b100000110110011101100010101110011100000110001011011111101011\
1101101110010010011010000011011101110011'
        self.assertEqual(
            res,
            lxor.XOR(2).xor(self.time_exec, a, b)
        )

    def test_xor_dec(self):
        """ Test decimal XOR operation. """
        a = '291576365716537651973656375212'
        b = '918653637516537365126359767263'
        res = 650680349832413851101474338675
        self.assertEqual(
            res,
            lxor.XOR(10).xor(self.time_exec, a, b)
        )

    def test_xor_hex(self):
        """ Test hexadecimal XOR operation. """
        a = '3AE225119C3D0BD1BA4636FAC'
        b = 'B98547A85DB6756C0360B58DF'
        res = '0x836762B9C18B7EBDB92683773'.lower()
        self.assertEqual(
            res,
            lxor.XOR(16).xor(self.time_exec, a, b)
        )

    def test_mod_inverse_bin(self):
        """ Test binary modular inverse operation. """
        a = '11001011001010011011101100011010101110110001101011001000101100101'
        n = '1101010111100001001001100000000011011001111001011001000101001000\
11100001010111100000110100'
        res = '0b111010001001001011011000000100101001000110101001101101011011\
101111001110010010101101001'
        self.assertEqual(
            res,
            lmi.ModInverse(2).modInverse(self.time_exec, a, n)
        )

    def test_mod_inverse_dec(self):
        """ Test decimal modular inverse operation. """
        a = '29278875574454292837'
        n = '1034257732296675869801674804'
        res = 140582120745925010153481577
        self.assertEqual(
            res,
            lmi.ModInverse(10).modInverse(self.time_exec, a, n)
        )

    def test_mod_inverse_hex(self):
        """ Test hexadecimal modular inverse operation. """
        a = '19653763576359165'
        n = '35784980367964523857834'
        res = '0x74496C0948D4DADDE72569'.lower()
        self.assertEqual(
            res,
            lmi.ModInverse(16).modInverse(self.time_exec, a, n)
        )

    def test_exponentiation_bin(self):
        """ Test binary exponentiation operation. """
        a = '10000101011010000010'
        b = '1100'
        res = '0b110100100100101011011001000110110000001110000110000101111000\
01101100000011001111110100100110100101110011001110011010001011011010100100100\
00000001110010000001000110011011000101111100111111110111101000110010011100000\
001000000000000'
        self.assertEqual(
            res,
            le.Exponentiation(2).integerExponentiation(self.time_exec, a, b)
        )

    def test_exponentiation_dec(self):
        """ Test decimal exponentiation operation. """
        a = '546434'
        b = '12'
        res = 708683902714598586017688360818973029566221804465707871043196587872256
        self.assertEqual(
            res,
            le.Exponentiation(10).integerExponentiation(self.time_exec, a, b)
        )

    def test_exponentiation_hex(self):
        """ Test hexadecimal exponentiation operation. """
        a = '85682'
        b = 'C'
        res = '0x1A495B236070C2F0D819FA4D2E67345B52401C8119B17CFF7A327010\
00'.lower()
        self.assertEqual(
            res,
            le.Exponentiation(16).integerExponentiation(self.time_exec, a, b)
        )

    def test_exponentiation_mod_bin(self):
        """ Test binary modular exponentiation operation. """
        a = '10000101011010000010'
        b = '1100'
        n = '1000100110000001100101000101100101101101101101101111011010001101\
001101010000000'
        res = '0b100100111011001011000001000101111111111000000101101000010001\
010010010000000'
        self.assertEqual(
            res,
            le.Exponentiation(2).modularExponentiation(self.time_exec, a, b, n)
        )

    def test_exponentiation_mod_dec(self):
        """ Test decimal modular exponentiation operation. """
        a = '546434'
        b = '12'
        n = '324677263917236527471232'
        res = 21796415852994751931520
        self.assertEqual(
            res,
            le.Exponentiation(10).modularExponentiation(
                self.time_exec, a, b, n
            )
        )

    def test_exponentiation_mod_hex(self):
        """ Test hexadecimal modular exponentiation operation. """
        a = '85682'
        b = 'C'
        n = '44C0CA2CB6DB7B469A80'
        res = '0x49D9608BFF02D08A480'.lower()
        self.assertEqual(
            res,
            le.Exponentiation(16).modularExponentiation(
                self.time_exec, a, b, n
            )
        )

    def test_mod_bin(self):
        """ Test binary modular operation. """
        a = '1101100011000101010100111001001110011110011000100100001111101001\
0101110000110000100000010011000111001111000000110'
        n = '1001001111000001010010111110101110000110110101111011001110111101\
101010011010100010111101111100000111'
        res = '0b100001000010100010111001110110000001110010010010010110110111\
111010111001000000101111000011101101000'
        self.assertEqual(
            res,
            lmod.Module(2).module(self.time_exec, a, n)
        )

    def test_mod_dec(self):
        """ Test decimal modular operation. """
        a = '8793268576239856239652376529837574'
        n = '731647642385773654826375962375'
        res = 327210047628455948990214014824
        self.assertEqual(
            res,
            lmod.Module(10).module(self.time_exec, a, n)
        )

    def test_mod_hex(self):
        """ Test hexadecimal modular operation. """
        a = '1B18AA7273CC487D2B86102639E06'
        n = '93C14BEB86D7B3BDA9A8BDF07'
        res = '0x42145CEC0E492DBF5C8178768'.lower()
        self.assertEqual(
            res,
            lmod.Module(16).module(self.time_exec, a, n)
        )

    def test_gcd_2_bin(self):
        """ Test binary Greatest Common Divisor with two numbers. """
        a = '1010101110110100011011101110010011110101001001001011011100101011\
00001001001110000110'
        b = '1100001110011000100010000010111111000100010100100000001011001111\
0110011101010000'
        res = '0b10'
        self.assertEqual(
            res,
            lgcd.GCD(2).greatestCommonDivisor(self.time_exec, a, b)
        )

    def test_gcd_2_dec(self):
        """ Test decimal Greatest Common Divisor with two numbers. """
        a = '12973649172562463257826182'
        b = '923675182536754245625680'
        res = 2
        self.assertEqual(
            res,
            lgcd.GCD(10).greatestCommonDivisor(self.time_exec, a, b)
        )

    def test_gcd_2_hex(self):
        """ Test hexadecimal Greatest Common Divisor with two numbers. """
        a = 'ABB46EE4F524B72B09386'
        b = 'C398882FC45202CF6750'
        res = '0x2'.lower()
        self.assertEqual(
            res,
            lgcd.GCD(16).greatestCommonDivisor(self.time_exec, a, b)
        )

    def test_gcd_3_bin(self):
        """ Test binary Greatest Common Divisor with three numbers. """
        a = '1010101110110100011011101110010011110101001001001011011100101011\
00001001001110000110'
        b = '1100001110011000100010000010111111000100010100100000001011001111\
0110011101010000'
        c = '1111011010010101011000100010111101110100100001010111000100100011\
0110100101100111101'
        res = '0b1'
        self.assertEqual(
            res,
            lgcd.GCD(2).greatestCommonDivisor(self.time_exec, a, b, c)
        )

    def test_gcd_3_dec(self):
        """ Test decimal Greatest Common Divisor with three numbers. """
        a = '12973649172562463257826182'
        b = '923675182536754245625680'
        c = '9315662357236572365736765'
        res = 1
        self.assertEqual(
            res,
            lgcd.GCD(10).greatestCommonDivisor(self.time_exec, a, b, c)
        )

    def test_gcd_3_hex(self):
        """ Test hexadecimal Greatest Common Divisor with three numbers. """
        a = 'ABB46EE4F524B72B09386'
        b = 'C398882FC45202CF6750'
        c = '7B4AB117BA42B891B4B3D'
        res = '0x1'.lower()
        self.assertEqual(
            res,
            lgcd.GCD(16).greatestCommonDivisor(self.time_exec, a, b, c)
        )

    def test_lcm_2_bin(self):
        """ Test binary Least Common Multiple with two numbers. """
        a = '110111001111110101100100111111000011001110'
        b = '11110101011010101111110001000100001011'
        res = '0b110100111101101011011100010101010111011001101001011101100000\
10110000011011011010'
        self.assertEqual(
            res,
            llcm.LCM(2).leastCommonMultiple(self.time_exec, a, b)
        )

    def test_lcm_2_dec(self):
        """ Test decimal Least Common Multiple with two numbers. """
        a = '3796576235726'
        b = '263515476235'
        res = 1000456594819820510971610
        self.assertEqual(
            res,
            llcm.LCM(10).leastCommonMultiple(self.time_exec, a, b)
        )

    def test_lcm_2_hex(self):
        """ Test hexadecimal Least Common Multiple with two numbers. """
        a = '373F593F0CE'
        b = '3D5ABF110B'
        res = '0xD3DADC557669760B06DA'.lower()
        self.assertEqual(
            res,
            llcm.LCM(16).leastCommonMultiple(self.time_exec, a, b)
        )

    def test_lcm_3_bin(self):
        """ Test binary Least Common Multiple with three numbers. """
        a = '110111001111110101100100111111000011001110'
        b = '11110101011010101111110001000100001011'
        c = '1110110111011110111110010011000110000010111010'
        res = '0b110001001101101000100011111111110000101001000100110000000111\
11111110010001111100111100100101011011101101001100101110100110010'
        self.assertEqual(
            res,
            llcm.LCM(2).leastCommonMultiple(self.time_exec, a, b, c)
        )

    def test_lcm_3_dec(self):
        """ Test decimal Least Common Multiple with three numbers. """
        a = '3796576235726'
        b = '263515476235'
        c = '65385479823546'
        res = 32707667247462454820693688889907764530
        self.assertEqual(
            res,
            llcm.LCM(10).leastCommonMultiple(self.time_exec, a, b, c)
        )

    def test_lcm_3_hex(self):
        """ Test hexadecimal Least Common Multiple with three numbers. """
        a = '373F593F0CE'
        b = '3D5ABF110B'
        c = '3B77BE4C60BA'
        res = '0x189B447FE148980FFC8F9E4ADDA65D32'.lower()
        self.assertEqual(
            res,
            llcm.LCM(16).leastCommonMultiple(self.time_exec, a, b, c)
        )

    def test_primality_ok_bin(self):
        """ Test binary primality. """
        a = '1010101001110001110110100000110010100110011100110010111011101111\
1011000000011010101000011100101000010001111110100000001'
        self.assertTrue(
            lp.Primality(2).is_prime(self.time_exec, a)
        )

    def test_primality_ok_dec(self):
        """ Test decimal primality. """
        a = '442499826945303593556473164314770689'
        self.assertTrue(
            lp.Primality(10).is_prime(self.time_exec, a)
        )

    def test_primality_ok_hex(self):
        """ Test hexadecimal primality. """
        a = '5538ED0653399777D80D50E508FD01'
        self.assertTrue(
            lp.Primality(16).is_prime(self.time_exec, a)
        )

    def test_primality_ko_bin(self):
        """ Test binary primality. """
        a = '1010111000110111101101101000010010011100110110100101010011101101\
1000010010000100001010000101110000100'
        self.assertFalse(
            lp.Primality(2).is_prime(self.time_exec, a)
        )

    def test_primality_ko_dec(self):
        """ Test decimal primality. """
        a = '1725367825470892357176235723652'
        self.assertFalse(
            lp.Primality(10).is_prime(self.time_exec, a)
        )

    def test_primality_ko_hex(self):
        """ Test hexadecimal primality. """
        a = '15C6F6D0939B4A9DB090850B84'
        self.assertFalse(
            lp.Primality(16).is_prime(self.time_exec, a)
        )

    def test_factorization_bin(self):
        """ Test binary factorization. """
        a = '1001100110000110100110100011110110100001111011111110111101000010\
0011011010110010011101111010010'
        res = ['0b10', '0b11', '0b11', '0b111011111', '0b10110010011111',
               '0b10001110010000010101',
               '0b1011110001000001000111101001011110011011100011101']
        self.assertEqual(
            res,
            lf.Factorization(2).factorization(self.time_exec, a)
        )

    def test_factorization_dec(self):
        """ Test decimal factorization. """
        a = '23756965471926357236576238546'
        res = [2, 3, 3, 479, 11423, 582677, 413975744296733]
        self.assertEqual(
            res,
            lf.Factorization(10).factorization(self.time_exec, a)
        )

    def test_factorization_hex(self):
        """ Test hexadecimal factorization. """
        a = '4CC34D1ED0F7F7A11B593BD2'
        res = ['0x2', '0x3', '0x3', '0x1df', '0x2c9f',
               '0x8e415', '0x178823d2f371d']
        self.assertEqual(
            res,
            lf.Factorization(16).factorization(self.time_exec, a)
        )

    def test_dlp_bin(self):
        """ Test binary Discrete Logarithmic Problem. """
        a = '10'
        y = '10001000100110010011110101010011110101010011'
        n = '10111111101010011010000111011011010000101010100101'
        res = '0b1111011'
        self.assertEqual(
            res,
            ldl.DiscreteLogarithm(2).discreteLogarithm(self.time_exec, a, y, n)
        )

    def test_dlp_dec(self):
        """ Test decimal Discrete Logarithmic Problem. """
        a = '2'
        y = '9386983767379'
        n = '842941143517861'
        res = 123
        self.assertEqual(
            res,
            ldl.DiscreteLogarithm(10).discreteLogarithm(
                self.time_exec, a, y, n
            )
        )

    def test_dlp_hex(self):
        """ Test hexadecimal Discrete Logarithmic Problem. """
        a = '2'
        y = '88993D53D53'
        n = '2FEA6876D0AA5'
        res = '0x7B'.lower()
        self.assertEqual(
            res,
            ldl.DiscreteLogarithm(16).discreteLogarithm(
                self.time_exec, a, y, n
            )
        )

if __name__ == '__main__':
    unittest.main()
