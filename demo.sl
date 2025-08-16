[Sample program demonstrating even/odd check in simplelang]

L 10 DEFINE howToDefineVariable "this is how you define a variable!"
L 20 DEFINE a 10
L 30 DEFINE b 100
L 40 INIT c
L 50 + a b c
L 60 PRINT "c is" " "
L 70 PRINTL c

L 80 INIT mod
L 90 % c 2 mod

L 100 JE mod 0 200
L 110 JE mod 1 300

L 200 PRINTL "c is even"
L 210 J 400

L 300 PRINTL "c is odd"
L 310 J 400

L 400 PRINTL "END!"
