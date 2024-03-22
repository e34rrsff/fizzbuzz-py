# functions.py
#
# Copyright 2024 e34rrsff
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE X CONSORTIUM BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Except as contained in this notice, the name(s) of the above copyright
# holders shall not be used in advertising or otherwise to promote the sale,
# use or other dealings in this Software without prior written
# authorization.

countTo         = 100   # Number to count up to
fizzDivisor     = 3     # To say Fizz if divisible by this
buzzDivisor     = 5     # To say Buzz if divisible by this
fizzBuzzDivisor = 15    # To say FizzBuzz if divisible by this

def sPF(CurrNum, FizzDiv):

    if CurrNum   % FizzDiv == 0:
        return True

    elif CurrNum % FizzDiv != 0:
        return False

def sPB(CurrNum, BuzzDiv):

    if CurrNum   % BuzzDiv == 0:
        return True

    elif CurrNum % BuzzDiv != 0:
        return False

def sPFB(CurrNum, FizzBuzzDiv):

    if CurrNum   % FizzBuzzDiv == 0:
        return True

    elif CurrNum % FizzBuzzDiv != 0:
        return False

shouldPrint = {
    "fizz"      : sPF,
    "buzz"      : sPB,
    "fizzbuzz"  : sPFB
}

def determineResult(i):

    if shouldPrint["fizzbuzz"](i, fizzBuzzDivisor) == True:
        return "FizzBuzz"

    elif shouldPrint["fizz"](i,fizzDivisor) == True:
        return "Fizz"

    elif shouldPrint["buzz"](i,buzzDivisor) == True:
        return "Buzz"

    else:
        return str(i)
