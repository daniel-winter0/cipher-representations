# Cipher Representations (V1.0)

This project demonstrates object-oriented design principles by implementing classical substitution ciphers in Python. It focuses on abstraction, code reusability, and clean interface design.

This project implements three well-known encryption algorithms in Python:
- **Caesar Cipher**
- **Vigenere Cipher**
- **Affine Cipher**

These ciphers were studied as part of a Computer Science course at University and are implemented here using object-oriented programming principles, including abstract base classes.

> [!CAUTION]
> This project is for educational use only, and **IS NOT** secure enough for modern cryptographic use.

---

## Overview
The project is structured around a base abstract class:
```python
class Cipher(ABC):
    @abstractmethod
    def encrypt(self, text: str):
        pass

    @abstractmethod
    def decrypt(self, text: str):
        pass
```

This ensures that:
    - Every cipher must implement both `encrypt` and `decrypt`.
    - Future cipher implementations will follow a consistent interface.
    - The design follows proper abstraction and polymorphism principles.

---

## Usage

### 1. Clone the Repository
First, clone the repository from GitHub:

```bash
git clone https://github.com/daniel-winter0/cipher-representations.git
```

Navigate into the project directory:

```bash
cd cipher-representations
```

---

### 2. Import the Cipher Classes
You can now import and use the cipher implementations in your Python scripts.

Example:

```python
from cipher import CaesarCipher
```

---

### Notes
- Only lowercase English alphabet characters (`a-z`) are encrypted.
- Input text is automatically converted to lowercase.
- Spaces and punctuation are preserved.
- No external libraries are required.

---

## Caesar Cipher
The Caesar Cipher shifts each letter in the plaintext by a fixed number of positions in the alphabet.

**Example Usage**
```python
from cipher import CaesarCipher

cipher = CaesarCipher(shift=3)

encrypted = cipher.encrypt("hello world")
print(encrypted)  # khoor zruog

decrypted = cipher.decrypt(encrypted)
print(decrypted)  # hello world
```

**How it works**
- Each character is shifted forwards by `shift` positions.
- Decryption shifts backward by the same amount.
- Non-alphabet characters (spaces, punctuation) remain unchanged.
- All text is converted to lowercase before processing.

---

## Vigenere Cipher
The Vigenere Cipher uses a keyword to determine shifting values for each character.

**Example Usage**
```python
from cipher import VigenereCipher

cipher = VigenereCipher(key="key")

encrypted = cipher.encrypt("hello world")
print(encrypted) # rijvs uyvjn

decrypted = cipher.decrypt(encrypted)
print(decrypted) # hello world
```

**How it works**
- Each letter of the key determines the shift for the corresponding letter in the plaintext.
- The key repeats as necessary.
- Only alphabetic characters are allowed in the key, and are converted to lowercase.
- Non-alphabet characters in the text are preserved.
- All text is converted to lowercase before processing.

---

## Affine Cipher
The Affine Cipher uses a shift and multiplier, and multiplies the index by the multiplier, and adds the shift.

**Example Usage**
```python
from cipher import AffineCipher

cipher = AffineCipher(shift=3, multiplier=5)

encrypted = cipher.encrypt("hello world")
print(encrypted) # mxggv jvkgs

decrypted = cipher.decrypt(encrypted)
print(decrypted) # hello world
```

---

## Design Decisions
### 1. Abstract Base Class
The `Cipher` class enforces implementation of:
- `encrypt()`
- `decrypt()`

This ensures:
- Consistency across cipher implementations.
- Extensibility for future cipher types.
- Clean object-oriented structure.

### 2. Alphabet Handling
The alphabet is defined using `string.ascii_lowercase`.
- Only lowercase English letters are supported.
- Input text is normalized to lowercase.
- Characters not in the alphabet are left unchanged.

---

## Extending the Project
To add a new cipher:
1. Inherit from the `Cipher` class.
2. Implement:
    - `encrypt(self, text: str)`
    - `decrypt(self, text: str)`

**Example**
```python
class MyNewCipher(Cipher):
    def __init__(self, ...):
        ...
    
    def encrypt(self, text: str):
        ...

    def decrypt(self, text: str):
        ...
```

---
## Requirements
- Python 3.8+
- No external dependencies (uses only standard libraries)
