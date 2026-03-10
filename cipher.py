"""
------------------------------
Cipher Representations
------------------------------

Author: Daniel Winter
Version: 1.0

Implementation of three classical encryption algorithms:
    - Caesar Cipher
    - Vigenere Cipher
    - Affine Cipher

These ciphers were studied as part of a Computer Science course.
The project uses Python classes, with a base Cipher class containing
abstract encrypt and decrypt methods to ensure consistency across ciphers.

Future ciphers must implement both methods to maintain this structure.
"""

###########################################################################

from abc import ABC, abstractmethod
import string
import math

###########################################################################

class Cipher(ABC):
    """
    Base class for all cipher implementations.

    Defines the required encrypt and decrypt methods that every cipher must
    implement.
    """
    # Specifying the alphabet for the ciphers
    alphabet = string.ascii_lowercase

    # Abstract methods enforcing each cipher has a encrypt and decrypt function
    @abstractmethod
    def encrypt(self, text: str):
        pass

    @abstractmethod
    def decrypt(self, text: str):
        pass

###########################################################################

class CaesarCipher(Cipher):
    def __init__(self, shift: int):
        # Ensure shift is an integer
        if not isinstance(shift, int):
            raise ValueError("Shift must be an integer")
        
        self.shift = shift
    

    def encrypt(self, text: str):
        # Ensure text is a string
        if not isinstance(text, str):
            raise ValueError("Text must be a string")

        text = text.lower()

        # Empty list to add each character to
        result = []

        for char in text:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                new_index = (index + self.shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                # Character not in alphabet
                result.append(char)
        
        # Returns the list formatted as a string with no
        # seperating characters
        return ''.join(result)

    
    def decrypt(self, text: str):
        # Ensure text is a string
        if not isinstance(text, str):
            raise ValueError("Text must be a string")

        text = text.lower()

        # Empty list to add each character to
        result = []

        for char in text:
            if char in self.alphabet:
                index = self.alphabet.index(char)
                new_index = (index - self.shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                # Character not in alphabet
                result.append(char)
        
        # Returns the list formatted as a string with no
        # seperating characters
        return ''.join(result)

###########################################################################

class VigenereCipher(Cipher):
    def __init__(self, key: str):
        # Ensure key is a string
        if not isinstance(key, str):
            raise ValueError("Key must be a string")

        key = key.lower()

        # Ensure key isn't blank
        if not key:
            raise ValueError("Key cannot be blank")

        # Make sure all characters in key are in the allowed alphabet
        for char in key:
            if char not in self.alphabet:
                raise ValueError("Only keys specified in the alphabet are allowed")
        
        self.key = key
    

    def encrypt(self, text: str):
        # Ensure text is a string
        if not isinstance(text, str):
            raise ValueError("Text must be a string")

        text = text.lower()

        # Empty list to add each character to
        result = []

        key_length = len(self.key)
        key_index = 0

        for char in text:
            if char in self.alphabet:
                text_pos = self.alphabet.index(char)
                key_pos = self.alphabet.index(self.key[key_index % key_length])
                new_pos = (text_pos + key_pos) % len(self.alphabet)
                result.append(self.alphabet[new_pos])
                key_index += 1
            else:
                # Character not in alphabet
                result.append(char)

        # Returns the list formatted as a string with no
        # seperating characters
        return ''.join(result)


    def decrypt(self, text: str):
        # Ensure text is a string
        if not isinstance(text, str):
            raise ValueError("Text must be a string")

        text = text.lower()

        # Empty list to add each character to
        result = []
        
        key_length = len(self.key)
        key_index = 0

        for char in text:
            if char in self.alphabet:
                text_pos = self.alphabet.index(char)
                key_pos = self.alphabet.index(self.key[key_index % key_length])
                new_pos = (text_pos - key_pos) % len(self.alphabet)
                result.append(self.alphabet[new_pos])
                key_index += 1
            else:
                # Character not in alphabet
                result.append(char)
        
        # Returns the list formatted as a string with no
        # seperating characters
        return ''.join(result)

###########################################################################

class AffineCipher(Cipher):
    def __init__(self, shift: int, multiplier: int):
        if not isinstance(shift, int) or not isinstance(multiplier, int):
            raise ValueError("Shift and multiplier must be integers")
        
        # Ensure multiplier is a coprime with alphabet length
        if math.gcd(multiplier, len(self.alphabet)) != 1:
            raise ValueError("Multiplier must be a coprime with alphabet length")
        
        self.shift = shift
        self.multiplier = multiplier


    def encrypt(self, text: str):
        # Ensure text is a string
        if not isinstance(text, str):
            raise ValueError("Text must be a string")
        
        text = text.lower()

        # Empty list to add each character to
        result = []

        for char in text:
            if char in self.alphabet:
                char_index = self.alphabet.index(char)
                new_index = ((char_index * self.multiplier) + self.shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                # Character not in alphabet
                result.append(char)

        # Returns the list formatted as a string with no
        # separating characters
        return ''.join(result)
    

    def decrypt(self, text: str):
        # Ensure text is a string
        if not isinstance(text, str):
            raise ValueError("Text must be a string")
        
        text = text.lower()

        # Empty list to add each character to
        result = []

        # Get the inverse of the multiplier
        mul_inversed = pow(self.multiplier, -1, len(self.alphabet))

        for char in text:
            if char in self.alphabet:
                char_index = self.alphabet.index(char)
                new_index = (mul_inversed * (char_index - self.shift)) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                # Character not in alphabet
                result.append(char)

        # Returns the list formatted as a string with no
        # seperating characters
        return ''.join(result)
