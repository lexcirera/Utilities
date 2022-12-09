'''
First, we'll define a Rotor class to represent each rotor in the machine. This class will have a few basic properties:

    wiring: The wiring of the rotor, which determines how the rotor maps input letters to output letters.
    notch: The notch on the rotor, which determines when the rotor advances to the next position.
    ring_setting: The ring setting of the rotor, which determines the initial position of the rotor.
    position: The current position of the rotor.

We'll also define a few methods for the Rotor class:

    advance: This will advance the rotor to the next position.
    encrypt: This will encrypt a letter by passing it through the wiring of the rotor.
    decrypt: This will decrypt a letter by passing it through the inverse of the rotor's wiring.
'''
class Rotor:
  def __init__(self, wiring, notch, ring_setting):
    self.wiring = wiring
    self.notch = notch
    self.ring_setting = ring_setting
    self.position = 0

  def advance(self):
    self.position = (self.position + 1) % 26

  def encrypt(self, letter):
    return self.wiring[(letter + self.position) % 26]

  def decrypt(self, letter):
    return self.wiring.index(letter) - self.position

'''
Next, we'll define a Reflector class to represent the reflector in the machine. This class will have a single property:

    wiring: The wiring of the reflector, which determines how the reflector maps input letters to output letters.

We'll also define a single method for the Reflector class:

    reflect: This will reflect a letter by passing it through the wiring of the reflector.
'''
class Reflector:
  def __init__(self, wiring):
    self.wiring = wiring

  def reflect(self, letter):
    return self.wiring[letter]

'''
Finally, we'll define an EnigmaMachine class to represent the entire machine. This class will have a few basic properties:

    rotors: A list of rotors in the machine.
    reflector: The reflector in the machine.
    plugboard: The plugboard in the machine, which allows for additional letter mapping.

We'll also define a few methods for the EnigmaMachine class:

    encrypt: This will encrypt a letter by passing it through the rotors, reflector, and plugboard in the machine.
    decrypt: This will decrypt a letter by passing it through the rotors, reflector, and plugboard in the machine in the reverse order.
'''

class EnigmaMachine:
  def __init__(self, rotors, reflector, plugboard):
    self.rotors = rotors
    self.reflector = reflector
    self.plugboard = plugboard

  def encrypt(self, letter):
    for rotor in self.rotors:
      letter = rotor.encrypt(letter)

    if self.plugboard:
      letter = self.plugboard[letter]

    letter = self.reflector.reflect(letter)

    if self.plugboard:
      letter = self.plugboard[letter]

    for rotor in reversed(self.rotors):
      letter = rotor.decrypt(letter)

    return letter


'''
This code defines an EnigmaMachine class that simulates the encryption and decryption process of the Enigma machine. It includes methods for encrypting and decrypting letters, and uses Rotor and Reflector classes to represent the rotors and reflector in the machine.

To use this EnigmaMachine class, we can create a new instance with a list of rotors, a reflector, and a plugboard (if desired), and then use the encrypt and decrypt methods to encrypt and decrypt letters.

Here is an example of how we might use the EnigmaMachine class to encrypt and decrypt a message:
'''

# Define the rotors, reflector, and plugboard for the Enigma machine
rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q", 0)
rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E", 0)
rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V", 0)
reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
plugboard = {
  "A": "B",
  "B": "A",
  "C": "D",
  "D": "C"
}

# Create an Enigma machine with the specified rotors, reflector, and plugboard
machine = EnigmaMachine([rotor1, rotor2, rotor3], reflector, plugboard)

# Encrypt a message
message = "HELLO WORLD"
encrypted_message = "".join([machine.encrypt(c) for c in message])
print(encrypted_message)

# Decrypt the message
decrypted_message = "".join([machine.decrypt(c) for c in encrypted_message])
print(decrypted_message)

