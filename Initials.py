def initial_print(initial_list):

  for i in range(len(initial_list)):
    if initial_list[i] == "A":
      print(A)
    if initial_list[i] == "B":
      print(B)
    if initial_list[i] == "C":
      print(C)
    if initial_list[i] == "D":
      print(D)
    if initial_list[i] == "E":
      print(E)
    if initial_list[i] == "F":
      print(F)
    if initial_list[i] == "G":
      print(G)
    if initial_list[i] == "H":
      print(H)
    if initial_list[i] == "I":
      print(I)
    if initial_list[i] == "J":
      print(J)
    if initial_list[i] == "K":
      print(K)
    if initial_list[i] == "L":
      print(L)
    if initial_list[i] == "M":
      print(M)
    if initial_list[i] == "N":
      print(N)
    if initial_list[i] == "O":
      print(O)
    if initial_list[i] == "P":
      print(P)
    if initial_list[i] == "Q":
      print(Q)
    if initial_list[i] == "R":
      print(R)
    if initial_list[i] == "S":
      print(S)
    if initial_list[i] == "T":
      print(T)
    if initial_list[i] == "U":
      print(U)
    if initial_list[i] == "V":
      print(V)
    if initial_list[i] == "W":
      print(W)
    if initial_list[i] == "X":
      print(X)
    if initial_list[i] == "Y":
      print(Y)
    if initial_list[i] == "Z":
      print(Z)

initial_list = []

A = """
    A  
  A   A 
A       A
A A A A A
A       A
A       A
A       A
"""

B = """
B B B B 
B       B
B       B
B B B B 
B       B
B       B
B B B B 
"""

C = """
  C C C
C       C
C
C
C
C       C
  C C C 
"""

D = """
D D D D
D       D
D       D
D       D
D       D
D       D
D D D D
"""

E = """
E E E E E
E
E
E E E
E
E
E E E E E
"""

F = """
F F F F F
F
F
F F F
F
F
F
"""

G = """
  G G G
G       G
G
G G G G G
G       G
G       G
  G G G 
"""

H = """
H       H
H       H
H       H
H H H H H
H       H
H       H
H       H
"""

I = """
I I I I I
    I
    I
    I
    I
    I
I I I I I
"""

J = """
J J J J J
    J
    J
    J
J   J
J   J
  J J
"""

K = """
K       K
K     K
K   K
K K
K   K
K     K
K       K
"""

L = """
L
L
L
L
L
L
L L L L L
"""

M = """
M       M
M M   M M
M M   M M
M   M   M
M   M   M
M   M   M
M   M   M
"""

N = """
N       N
N N     N
N   N   N
N     N N
N       N
N       N
N       N
"""

O = """
  O O O 
O       O
O       O
O       O
O       O
O       O
  O O O
"""

P = """
P P P P
P       P
P       P
P P P P
P
P
P
"""

Q = """
  Q Q Q
Q       Q
Q       Q
Q       Q
Q       Q
Q     Q
  Q Q   Q
"""

R = """
R R R R
R       R
R       R
R R R R
R   R
R     R
R       R
"""

S = """
  S S S
S       S
S
  S S S
        S
S       S
  S S S
"""

T = """
T T T T T
    T
    T
    T
    T
    T
    T
"""

U = """
U       U
U       U
U       U
U       U
U       U
U       U
  U U U
"""

V = """
V       V
V       V
V       V
V       V
V       V
  V   V
    V
"""

W = """
W       W
W       W
W       W
W   W   W
W W   W W
W W   W W
W       W
"""

X = """
X       X
X       X
  X   X
    X
  X   X
X       X
X       X
"""

Y = """
Y       Y
  Y   Y
    Y
    Y
    Y
    Y
    Y
"""

Z = """
Z Z Z Z Z
        Z
      Z
    Z
  Z
Z
Z Z Z Z Z
"""

first_initial = input("Please enter your first initial: ")
initial_list.append(first_initial)

last_initial = input("Please enter your last initial: ")
initial_list.append(last_initial)

initial_print(initial_list)