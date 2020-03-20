#!/usr/bin/env python3
a, b = 0, 1
while b < 100:
    print(b, end = " ")#print() have a acquiescent /n. end replace the /n to the " "
    a, b = b, a + b
print()# if not the "end = "" ", we don't need the fifth row and the result will add a extra % in the end
