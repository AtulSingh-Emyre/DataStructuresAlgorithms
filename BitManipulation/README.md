# Bit Manipulation
### Introduction

Bit Manipulation is a set of operations that involve working on individual bits in a binary representation of data. In python, we apply the same over integers.

### Bitwise Operators in Python:

- AND (&): This operator compares each bit of two numbers. If both bits are 1, the result is 1; otherwise, it’s 0.
- OR (|): This operator compares each bit of two numbers. If at least one of the bits is 1, the result is 1; otherwise, it’s 0.
- XOR (^): This operator compares each bit of two numbers. If the bits are different, the result is 1; if they are the same, the result is 0.
- NOT (~): This operator flips all the bits in a number. All 0s become 1s, and all 1s become 0s. Note that this operation can also depend on the size of the integer (due to two’s complement representation).
- Shift Left (<<): This operator shifts the bits of a number to the left by a specified number of positions, effectively multiplying the number by 2 raised to the power of the shift amount.
- Shift Right (>>): This operator shifts the bits of a number to the right by a specified number of positions, effectively dividing the number by 2 raised to the power of the shift amount (integer division).

##### Define two numbers in binary
a = 0b1010  # 10 in decimal
b = 0b1100  # 12 in decimal

###### Bitwise AND
result_and = a & b  # 0b1000 (8 in decimal)
print("Bitwise AND:", bin(result_and))

###### Bitwise OR
result_or = a | b  # 0b1110 (14 in decimal)
print("Bitwise OR:", bin(result_or))

###### Bitwise XOR
result_xor = a ^ b  # 0b0110 (6 in decimal)
print("Bitwise XOR:", bin(result_xor))

###### Bitwise NOT
result_not_a = ~a  # -11 in decimal (depends on size of integer)
print("Bitwise NOT of a:", bin(result_not_a))

###### Left shift
result_left_shift = a << 2  # 0b101000 (40 in decimal)
print("Left Shift of a:", bin(result_left_shift))

###### Right shift
result_right_shift = b >> 1  # 0b110 (6 in decimal)
print("Right Shift of b:", bin(result_right_shift))

