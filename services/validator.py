from validate_docbr import CPF
import re

class Validator:
    def base(requered: dict, data: dict):
        requered = [req for req in requered if req not in data]
        
        if requered:
            response = {
                "erro": "Faltam campos obrigatórios",
                "recebido": [inf for inf in data],
                "faltantes": {
                    "Campos": requered,
                },
            },
            
            return response      
  
    def register_validator(data: dict):
        REGISTER = ["name", "cpf", "email", "phone_number"]
        return Validator.base(REGISTER, data)

    def search_validator(data: dict):
        REGISTER = ["name"]
        return Validator.base(REGISTER, data)        

    def check_cpf_is_true(cpf: str):
        return CPF().validate(cpf)

    def check_phone_11_digits(phone: str):
        return True if len(phone) == 11 else False

    def check_phone_only_numbers(phone: str):
        return all(char.isnumeric() for char in phone)

    def check_if_email_is_valid(email: str):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if(re.fullmatch(regex, email)):
            return True
        else:
            return False