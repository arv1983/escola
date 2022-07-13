import re

class Masks:

    def cpf_clean(cpf: str):
        
        return "".join(re.findall(r"\d", str(cpf)))

    
    def phone(phone: str):
        return '({}) {}-{}'.format(phone[0:2],
                            phone[2:7], phone[7:])

