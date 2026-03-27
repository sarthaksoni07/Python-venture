| Operator | Meaning        | Example   |
| -------- | -------------- | --------- |
| +        | Addition       | 5+2 = 7   |
| -        | Subtraction    | 5-2 = 3   |
| *        | Multiply       | 5*2 = 10  |
| /        | Divide         | 5/2 = 2.5 |
| //       | Floor division | 5//2 = 2  |
| %        | Modulus        | 5%2 = 1   |
| **       | Power          | 5**2 = 25 |

===================================================

| Operator | Meaning           |
| -------- | ----------------- |
| and      | Both must be true |
| or       | One must be true  |
| not      | Reverse           |

===================================================


most operators operate from left to right > and the exponential (**) operates from right to left <


Level,Operator,Description
1 (Highest),(),Parentheses (always happens first)
2,**,Exponentiation (Power)
3,"+x, -x, ~x","Unary plus, minus, and bitwise NOT"
4,"*, /, //, %","Multiplication, Division, Floor Div, Modulo"
5,"+, -",Addition and Subtraction
6,"<<, >>",Bitwise shifts
7,&,Bitwise AND
8,^,Bitwise XOR
9,|,Bitwise OR
10,"==, !=, >, <, etc.","Comparisons and Identity (is), Membership (in)"
11,not,Logical NOT
12,and,Logical AND
13 (Lowest),or,Logical OR