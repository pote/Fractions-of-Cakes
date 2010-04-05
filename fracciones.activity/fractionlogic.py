# -*- coding: utf-8 -*-
"""
Contains the logic of fractions and comparations of fractions.

"""
import random
DENOMINATOR_MIN = 4
DENOMINATOR_MAX = 10


class Fraction(object):

    def __init__(self,numerator=None,denominator=None):
        self.numerator = numerator
        self.denominator = denominator
            
    def __eq__(self,other_fraction):
        if (self.numerator * other_fraction.denominator == self.denominator * other_fraction.numerator) and type(other_fraction) is Fraction:
            return True 
        else:
            return False
            
    def __ne__(self,other_fraction):
        if (self.numerator * other_fraction.denominator != self.denominator * other_fraction.numerator):
            return True 
        else:
            return False        

    def __add__(self,other_fraction):
        if not (type(other_fraction) is Fraction):
            raise Exception("Fraction Objects only allow addition with other Fraction objects")
        else:
            return calculate(self,other_fraction,"+")
                   
                     
                
class FractionLogic(object):

    def __init__(self):
        self.fraction = Fraction()
        

    def generate(self):
        """Generate new fraction"""
        if DENOMINATOR_MIN < 1:
            raise Exception("DENOMINATOR_MIN need be greather than 0")
        self.fraction.denominator = random.randrange(DENOMINATOR_MIN, DENOMINATOR_MAX)
        self.fraction.numerator = random.randrange(0, self.fraction.denominator+1)


    def get_current(self):
        """Return the current fraction, raise an exception if generate_fraction
        hasn't called before"""
        if self.fraction.denominator is None:
            raise Exception("generate_fraction must be called before get_current_fraction")
        return (self.fraction.numerator, self.fraction.denominator)
        
        
    def get_current_cake(self):
        """Return the current fraction, raise an exception if generate_fraction
        hasn't called before"""
        if self.fraction.denominator is None:
            raise Exception("generate_fraction must be called before get_current_fraction")
        return (self.fraction)


    def is_equal(self, fraction):
        """DEPRECATED: Check if fraction is equal that the internal"""
        if not(type(fraction) is Fraction and self.fraction.denominator is not None):
            raise Exception("fraction must be a tuple of length 2")
        if self.fraction.denominator is None:
            raise Exception("generate_fraction must be called before is_equal")
        return fraction.numerator * self.fraction.denominator == fraction.denominator * self.fraction.numerator


    def __repr__(self):
        if self.fraction.denominator is None:
            return "<FractionLogic(Undefined)>"
        return "<FractionLogic(%i,%i)>"%(self.fraction.numerator,self.fraction.denominator)



#<--Math methods for the Fraction object begin here-->

def calculate(fraction_1,fraction_2,operator,reduced_output=False):
    """Calls appropiate method depending on the operator received as an argument""" 
    """Requires 2 fraction objects and a one character string with the operator (+,-,*,/)"""
    result = Fraction()
    if operator == "+" : 
        result = add(fraction_1,fraction_2)
    elif operator == "-" : 
        result = substract(fraction_1,fraction_2) 
    elif operator == "*" : 
        result = multiply(fraction_1,fraction_2)
    elif operator == "/" :
        result = divide(fraction_1,fraction_2)
    if reduced_output == False:
        return result
    else:
        return reduce(result)

def add(fraction_1,fraction_2):
    result = Fraction()
    if fraction_1.denominator == fraction_2.denominator : 
        result.numerator = fraction_1.numerator + fraction_2.numerator
        result.denominator = fraction_1.denominator
        return result
    else:
        mcm = lcm(fraction_1.denominator,fraction_2.numerator)
        result.denominator = mcm
        alt_fraction_1 = fraction_1.numerator * (fraction_1.denominator / mcm)
        alt_fraction_2 = fraction_2.numerator * (fraction_2.denominator / mcm)
        result.numerator = alt_fraction_1 + alt_fraction_2                 
        return result
               

def substract(fraction_1,fraction_2):
    result_fraction = Fraction()
    if fraction_1.denominator == fraction_2.denominator : 
        result.numerator = fraction_1.numerator - fraction_2.numerator
        result.denominator = fraction_1.denominator
        return result
    else:
        mcm = lcm(fraction_1.denominator,fraction_2.numerator)
        result.denominator = mcm
        alt_fraction_1 = fraction_1.numerator * (fraction_1.denominator / mcm)
        alt_fraction_2 = fraction_2.numerator * (fraction_2.denominator / mcm)
        result.numerator = alt_fraction_1 - alt_fraction_2                 
        return result

def multiply(fraction_1,fraction_2):
    result = Fraction()
    result.numerator = fraction_1.numerator * fraction_2.numerator
    result.denominator = fraction_1.denominator * fraction_2.denominator
    return result

def divide(fraction_1,fraction_2):
    inverse_fraction = Fraction()
    inverse_fraction.numerator = fraction_2.denominator
    inverse_fraction.denominator = fraction_2.numerator
    return multiply(fraction_1,fraction_2) 
        
def reduce(fraction):
    same_fraction = False
    while not same_fraction:
        same_fraction = True
        for i in range(2,10):
            if (fraction.numerator % i == 0 and fraction.denominator % i == 0):
                fraction.numerator = fraction.numerator / i
                fraction.denominator = fraction.denominator / i
                same_fraction = False 
                i = 2
    return fraction
    
# Function to calculate the GCD
def gcd(num1, num2):
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result

    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result

    else:
        result = num1*num2/num1
        return result

# Function to calculate the LCM
def lcm(num1, num2):
    result = num1*num2/gcd(num1,num2)
    return result                                  