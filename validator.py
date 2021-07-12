import logging
import re

class Validator:

    # Source: https://gist.github.com/michaelkeevildown/9096cd3aac9029c4e6e05588448a8841
    ACCEPTED_CARD_REGEXES = {
        "Mastercard": r"^5[1-5][0-9]{14}$",#|^2(?:2(?:2[1-9]\|[3-9][0-9])|[3-6][0-9][0-9]|7(?:[01][0-9]|20))[0-9]{12}$",
        "American Express": r"^3[47][0-9]{13}$",
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
    }
    
    def __init__(self, number: str):
        self.number = number.replace(" ", "")

    def is_valid_number(self):      
        return self.check_issuer() and self.checksum()

    def check_issuer(self):
        for _, regex in self.ACCEPTED_CARD_REGEXES.items():
            if re.match(regex, self.number):
                return True
        return False

    def checksum(self):
        # Source: https://medium.com/hootsuite-engineering/a-comprehensive-guide-to-validating-and-formatting-credit-cards-b9fa63ec7863
        reversed_digits = [int(x) for x in self.number]
        plain_digits = reversed_digits[1::2]

        manipulate = lambda x: x*2 if x*2 < 10 else (x*2) -9
        manipulated_digits = [manipulate(x) for x in reversed_digits[0::2]]

        return sum(plain_digits + manipulated_digits) % 10 == 0  