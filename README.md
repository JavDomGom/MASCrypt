<p align="center"><img src="https://github.com/JavierDominguezGomez/MASCrypt/blob/master/img/logo.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-brightgreen.svg)](https://www.gnu.org/licenses/gpl-3.0)
![GitHub top language](https://img.shields.io/github/languages/top/JavierDominguezGomez/MASCrypt)
![Python](https://img.shields.io/badge/python-v3.6+-blue)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/JavierDominguezGomez/MASCrypt)
[![Build Status](https://travis-ci.org/JavierDominguezGomez/MASCrypt.svg?branch=master)](https://travis-ci.org/JavierDominguezGomez/MASCrypt)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-yellow.svg)

## Basic Overview
MASCrypt (*Modular Arithmetic Software for Cryptography*) is a calculating tool on basic arithmetic operations and also modular arithmetic operations commonly used in cryptography. It is intended both for the study and learning of cryptography, but also for crypto professionals. Calculations can be made in Base-2 (binary), Base-10 (decimal) and Base-16 (hexadecimal) using very large integers.

<p align="center"><img src="https://github.com/JavierDominguezGomez/MASCrypt/blob/master/img/mascrypt_screenshot_00.png"></p>
<br>

## List of available operations
* [Addition](https://en.wikipedia.org/wiki/Addition)
* [Substraction](https://en.wikipedia.org/wiki/Subtraction)
* [Multiplication](https://en.wikipedia.org/wiki/Multiplication)
* [Division](https://en.wikipedia.org/wiki/Division_(mathematics))
* [Square root](https://en.wikipedia.org/wiki/Square_root)
* [Primitive root](https://en.wikipedia.org/wiki/Primitive_root_modulo_n)
* [XOR](https://en.wikipedia.org/wiki/Exclusive_or) (*Exclusive OR*)
* [Module inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)
* [Exponentation](https://en.wikipedia.org/wiki/Exponentiation)
* [Module](https://en.wikipedia.org/wiki/Module_(mathematics))
* [GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor) (*Greatest Common Divisor*)
* [LCM](https://en.wikipedia.org/wiki/Least_common_multiple) (*Least Common Multiple*)
* [Primality](https://en.wikipedia.org/wiki/Prime_number)
* [Factorization](https://en.wikipedia.org/wiki/Factorization)
* [Discrete Logarithm](https://en.wikipedia.org/wiki/Discrete_logarithm)

## Calculation time
I have calculated through 5 different executions the time it takes to perform some complex operations such as [Primitive root](https://en.wikipedia.org/wiki/Primitive_root_modulo_n), [Factorization](https://en.wikipedia.org/wiki/Factorization) or [Discrete Logarithm](https://en.wikipedia.org/wiki/Discrete_logarithm), and the result has been compared with the same operations in [SAMCript 1.0](http://www.criptored.upm.es/software/sw_m001t.htm). This is the percentage difference:
```
Primitive root
===================================
SAMCrypt = 3.8520000000000003s
MASCrypt = 0.01757216453552246s
Time reduced by 99.54381712005393%

Factorization
===================================
SAMCrypt = 0.015400000000000002s
MASCrypt = 0.006932878494262695s
Time reduced by 54.98130847881367%

Discrete Logarithm
===================================
SAMCrypt = 23.733600000000003s
MASCrypt = 14.647553300857544s
Time reduced by 38.283474479819574%
```
More details in [percentage_difference.py](https://github.com/JavierDominguezGomez/MASCrypt/blob/master/percentage_difference.py) file.

## Latest Development Changes
```bash
~$ git clone https://github.com/JavierDominguezGomez/MASCrypt.git
```

## How to launch
* **GNU/Linux**, **Unix** and **Mac**:
  ```bash
  ~/MASCrypt$ python3 main.py
  ```
* **Windows**: In Windows systems just double click on `main.py` file from downloaded repository.

## How to test
```
~$ pytest -v test.py
================================== test session starts ==================================
platform linux -- Python 3.6.9, pytest-4.5.0, py-1.8.0, pluggy-0.13.1 -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: ~/MASCrypt
collected 66 items                                                                      

test.py::MASCryptTest::test_addition_bin PASSED                                   [  1%]
test.py::MASCryptTest::test_addition_dec PASSED                                   [  3%]
test.py::MASCryptTest::test_addition_hex PASSED                                   [  4%]
test.py::MASCryptTest::test_addition_mod_bin PASSED                               [  6%]
test.py::MASCryptTest::test_addition_mod_dec PASSED                               [  7%]
test.py::MASCryptTest::test_addition_mod_hex PASSED                               [  9%]
test.py::MASCryptTest::test_division_bin PASSED                                   [ 10%]
test.py::MASCryptTest::test_division_dec PASSED                                   [ 12%]
test.py::MASCryptTest::test_division_hex PASSED                                   [ 13%]
test.py::MASCryptTest::test_dlp_bin PASSED                                        [ 15%]
test.py::MASCryptTest::test_dlp_dec PASSED                                        [ 16%]
test.py::MASCryptTest::test_dlp_hex PASSED                                        [ 18%]
test.py::MASCryptTest::test_exponentiation_bin PASSED                             [ 19%]
test.py::MASCryptTest::test_exponentiation_dec PASSED                             [ 21%]
test.py::MASCryptTest::test_exponentiation_hex PASSED                             [ 22%]
test.py::MASCryptTest::test_exponentiation_mod_bin PASSED                         [ 24%]
test.py::MASCryptTest::test_exponentiation_mod_dec PASSED                         [ 25%]
test.py::MASCryptTest::test_exponentiation_mod_hex PASSED                         [ 27%]
test.py::MASCryptTest::test_factorization_bin PASSED                              [ 28%]
test.py::MASCryptTest::test_factorization_dec PASSED                              [ 30%]
test.py::MASCryptTest::test_factorization_hex PASSED                              [ 31%]
test.py::MASCryptTest::test_gcd_2_bin PASSED                                      [ 33%]
test.py::MASCryptTest::test_gcd_2_dec PASSED                                      [ 34%]
test.py::MASCryptTest::test_gcd_2_hex PASSED                                      [ 36%]
test.py::MASCryptTest::test_gcd_3_bin PASSED                                      [ 37%]
test.py::MASCryptTest::test_gcd_3_dec PASSED                                      [ 39%]
test.py::MASCryptTest::test_gcd_3_hex PASSED                                      [ 40%]
test.py::MASCryptTest::test_lcm_2_bin PASSED                                      [ 42%]
test.py::MASCryptTest::test_lcm_2_dec PASSED                                      [ 43%]
test.py::MASCryptTest::test_lcm_2_hex PASSED                                      [ 45%]
test.py::MASCryptTest::test_lcm_3_bin PASSED                                      [ 46%]
test.py::MASCryptTest::test_lcm_3_dec PASSED                                      [ 48%]
test.py::MASCryptTest::test_lcm_3_hex PASSED                                      [ 50%]
test.py::MASCryptTest::test_mod_bin PASSED                                        [ 51%]
test.py::MASCryptTest::test_mod_dec PASSED                                        [ 53%]
test.py::MASCryptTest::test_mod_hex PASSED                                        [ 54%]
test.py::MASCryptTest::test_mod_inverse_bin PASSED                                [ 56%]
test.py::MASCryptTest::test_mod_inverse_dec PASSED                                [ 57%]
test.py::MASCryptTest::test_mod_inverse_hex PASSED                                [ 59%]
test.py::MASCryptTest::test_multiplication_bin PASSED                             [ 60%]
test.py::MASCryptTest::test_multiplication_dec PASSED                             [ 62%]
test.py::MASCryptTest::test_multiplication_hex PASSED                             [ 63%]
test.py::MASCryptTest::test_multiplication_mod_bin PASSED                         [ 65%]
test.py::MASCryptTest::test_multiplication_mod_dec PASSED                         [ 66%]
test.py::MASCryptTest::test_multiplication_mod_hex PASSED                         [ 68%]
test.py::MASCryptTest::test_primality_ko_bin PASSED                               [ 69%]
test.py::MASCryptTest::test_primality_ko_dec PASSED                               [ 71%]
test.py::MASCryptTest::test_primality_ko_hex PASSED                               [ 72%]
test.py::MASCryptTest::test_primality_ok_bin PASSED                               [ 74%]
test.py::MASCryptTest::test_primality_ok_dec PASSED                               [ 75%]
test.py::MASCryptTest::test_primality_ok_hex PASSED                               [ 77%]
test.py::MASCryptTest::test_primitive_root_bin PASSED                             [ 78%]
test.py::MASCryptTest::test_primitive_root_dec PASSED                             [ 80%]
test.py::MASCryptTest::test_primitive_root_hex PASSED                             [ 81%]
test.py::MASCryptTest::test_square_root_bin PASSED                                [ 83%]
test.py::MASCryptTest::test_square_root_dec PASSED                                [ 84%]
test.py::MASCryptTest::test_square_root_hex PASSED                                [ 86%]
test.py::MASCryptTest::test_substraction_bin PASSED                               [ 87%]
test.py::MASCryptTest::test_substraction_dec PASSED                               [ 89%]
test.py::MASCryptTest::test_substraction_hex PASSED                               [ 90%]
test.py::MASCryptTest::test_substraction_mod_bin PASSED                           [ 92%]
test.py::MASCryptTest::test_substraction_mod_dec PASSED                           [ 93%]
test.py::MASCryptTest::test_substraction_mod_hex PASSED                           [ 95%]
test.py::MASCryptTest::test_xor_bin PASSED                                        [ 96%]
test.py::MASCryptTest::test_xor_dec PASSED                                        [ 98%]
test.py::MASCryptTest::test_xor_hex PASSED                                        [100%]

============================== 66 passed in 46.79 seconds ===============================
```

## Credits
Created by Javier Domínguez Gómez \<jdg@member.fsf.org\>, based on [SAMCript 1.0](http://www.criptored.upm.es/software/sw_m001t.htm)
