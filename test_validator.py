import random
import unittest

from validator import Validator

class TestValidatorCases(unittest.TestCase):
    """Test the credit card validator."""
    
    test_cards = {
        "Visa": "4242 4242 4242 4242",
        "Mastercard": "5555 5555 5555 4444",
    }

    def test_validates_known_good_number(self):
        for issuer, number in self.test_cards.items():
            validator = Validator(number)
            self.assertTrue(validator.is_valid_number())

    def test_validates_without_spaces(self):
        for issuer, number in self.test_cards.items():
            number = number.replace(" ", "")
            validator = Validator(number)
            self.assertTrue(validator.is_valid_number())

    def test_validates_with_any_number_of_spaces(self):
        for issuer, number in self.test_cards.items():
            number = list(number)
            for i in range(10):
                idx = random.randrange(len(number))
                number.insert(idx, " ")
            number = "".join(number)
            validator = Validator(number)
            self.assertTrue(validator.is_valid_number())

    def test_does_not_validate_when_length_too_long(self):
        for issuer, number in self.test_cards.items():
            number = number + "1"
            validator = Validator(number)
            self.assertFalse(validator.is_valid_number())

    def test_raises_exception_when_length_too_short(self):
        for issuer, number in self.test_cards.items():
            number = number[:-1]
            validator = Validator(number)
            self.assertFalse(validator.is_valid_number())

    def test_does_not_validate_non_creditcard_mii(self):
        for issuer, number in self.test_cards.items():
            number = "9" + number[1:]
            validator = Validator(number)
            self.assertFalse(validator.is_valid_number())

    def test_does_not_validate_non_invalid_checksum(self):
        for issuer, number in self.test_cards.items():
            correct_checksum_value = number[-1]
            test_checksums = list(range(10))
            test_checksums.remove(int(correct_checksum_value))
            
            for checksum in test_checksums:
                number = number[:-1] + str(checksum)
                validator = Validator(number)
                self.assertFalse(validator.is_valid_number())


if __name__ == "__main__":
    unittest.main()