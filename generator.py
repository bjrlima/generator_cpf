import random
from tkinter import *

class validation():
    
    def validate(cpf: str) -> bool:
        clean_cpf = validation.clean_cpf(cpf)
        
        if not validation.lenth_cpf(clean_cpf):
            return False
        
        if validation.is_sequence(clean_cpf):
            return False
        
        if not validation.validate_digit_one(clean_cpf):
            return False
        
        if not validation.validate_digit_two(clean_cpf):
            return False
        
        return True
    
    def clean_cpf (cpf: str) -> str:
        clean_cpf = ''
        for digit in cpf:
            if digit.isdigit():
                clean_cpf += digit
        return clean_cpf
    
    def lenth_cpf (cpf: str) -> bool:
        return len(cpf) == 11
    
    def is_sequence(cpf: str) -> bool:
        return (cpf[0]*len(cpf)) == cpf

    def validate_digits(cpf: str, digit_verication: int) -> int:
        sum_total = 0
        mutiplier = digit_verication
        cpf_numbers = cpf[:mutiplier-1]

        for digit in cpf_numbers:
            sum_total += (int(digit)*mutiplier)
            mutiplier -= 1
        
        if sum_total % 11 < 2:
            return 0
        else:
            return 11 - (sum_total % 11)
    
    def validate_digit_one(cpf: str) -> bool:
        digit_one = 10
        return validation.validate_digits(cpf, digit_one) == int(cpf[9])
    
    def validate_digit_two(cpf: str) -> bool:
        digit_two = 11
        return validation.validate_digits(cpf, digit_two) == int(cpf[10])
          
class generation():
    
    def generate():
        new_cpf = generation.random_numbers()
        digit_one = generation.validate_digits(new_cpf, 10)
        new_cpf += str(digit_one)
        digit_two = generation.validate_digits(new_cpf, 11)
        new_cpf += str(digit_two)
        return f'{new_cpf[:3]}.{new_cpf[3:6]}.{new_cpf[6:9]}-{digit_one}{digit_two}'
    
    def random_numbers() -> str:
        random_cpf = ''
        for digit in range(9):
            random_cpf += str(random.randint(0,9))
        return random_cpf
    
    def validate_digits(cpf: str, digit_verication: int) -> int:
        sum_total = 0
        mutiplier = digit_verication

        for digit in cpf:
            sum_total += (int(digit)*mutiplier)
            mutiplier -= 1
        
        if sum_total % 11 < 2:
            return 0
        else:
            return 11 - (sum_total % 11)
