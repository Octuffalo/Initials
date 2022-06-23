letter_dictionary = {"A" : """
    A  
  A   A 
A       A
A A A A A
A       A
A       A
A       A
""",

"B" : """
B B B B 
B       B
B       B
B B B B 
B       B
B       B
B B B B 
""",

"C" : """
  C C C
C       C
C
C
C
C       C
  C C C 
""",

"D" : """
D D D D
D       D
D       D
D       D
D       D
D       D
D D D D
""",

"E" : """
E E E E E
E
E
E E E
E
E
E E E E E
""",

"F" : """
F F F F F
F
F
F F F
F
F
F
""",

"G" : """
  G G G
G       G
G
G G G G G
G       G
G       G
  G G G 
""",

"H" : """
H       H
H       H
H       H
H H H H H
H       H
H       H
H       H
""",

"I" : """
I I I I I
    I
    I
    I
    I
    I
I I I I I
""",

"J" : """
J J J J J
    J
    J
    J
J   J
J   J
  J J
""",

"K" : """
K       K
K     K
K   K
K K
K   K
K     K
K       K
""",

"L" : """
L
L
L
L
L
L
L L L L L
""",

"M" : """
M       M
M M   M M
M M   M M
M   M   M
M   M   M
M   M   M
M   M   M
""",

"N" : """
N       N
N N     N
N   N   N
N     N N
N       N
N       N
N       N
""",

"O" : """
  O O O 
O       O
O       O
O       O
O       O
O       O
  O O O
""",

"P" : """
P P P P
P       P
P       P
P P P P
P
P
P
""",

"Q" : """
  Q Q Q
Q       Q
Q       Q
Q       Q
Q       Q
Q     Q
  Q Q   Q
""",

"R" : """
R R R R
R       R
R       R
R R R R
R   R
R     R
R       R
""",

"S" : """
  S S S
S       S
S
  S S S
        S
S       S
  S S S
""",

"T" : """
T T T T T
    T
    T
    T
    T
    T
    T
""",

"U" : """
U       U
U       U
U       U
U       U
U       U
U       U
  U U U
""",

"V" : """
V       V
V       V
V       V
V       V
V       V
  V   V
    V
""",

"W" : """
W       W
W       W
W       W
W   W   W
W W   W W
W W   W W
W       W
""",

"X" : """
X       X
X       X
  X   X
    X
  X   X
X       X
X       X
""",

"Y" : """
Y       Y
  Y   Y
    Y
    Y
    Y
    Y
    Y
""",

"Z" : """
Z Z Z Z Z
        Z
      Z
    Z
  Z
Z
Z Z Z Z Z
"""}

first_initial = input("Please enter your first initial: ")
first_initial = first_initial.upper()

last_initial = input("Please enter your last initial: ")
last_initial = last_initial.upper()

print(letter_dictionary[first_initial])
print(letter_dictionary[last_initial])