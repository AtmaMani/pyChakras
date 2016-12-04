
# Number system

### Tests of divisibility
With digital calculators and programs, this is trivial or even mundane. However, the Arabic and decimal numbering system exhibits this interesting feature where you can use shortcuts to test divisibility and find a number's factors.

|Number|Divisibility rule|
|----|------------------------------------------------------------------|
| 2 | Divisible, if number is even |
| 3 | Divisible, if sum of all digits is divisible by 3 |
| 4 | Divisible, if sum of last two digits is divisible by 4 |
| 5 | Divisible if last digit is either 0 or 5 |
| 6 | Divisible, if divisible by 2 and 3 |
| 7 | Remove the last digit, double it and subtract it from now truncated number. Repeat this and if you are left with either 0 or 7, then divisible.|
| 8 | Divisible, if the number formed by last 3 digits is divisible by 8 |
| 9 | Divisible, if sum of digits is divisible by 9 |
| 10 | Divisible if last digit is 0 |
| 11 | Divisible if difference between sum of odd and alternate digits is 0 or 11 |

**7**

Remove the last digit, double it and subtract it from now truncated number. Repeat this and if you are left with either 0 or 7, then divisible.
Example:
    
    1603:
        160 - 6 = 154
        15 - 8 = 7
        
        Reminder is 7, hence divisible

This is interesting, lets build the multiples of seven here and observe how the lineup looks like


```python
for n in range(200, 240):
    print(7*n, end= " ")
```

    1400 1407 1414 1421 1428 1435 1442 1449 1456 1463 1470 1477 1484 1491 1498 1505 1512 1519 1526 1533 1540 1547 1554 1561 1568 1575 1582 1589 1596 1603 1610 1617 1624 1631 1638 1645 1652 1659 1666 1673 

Lets take higher numbers like 1610 or 1631, you dont have to iterate until you are left with 0 or 7, if you land on a multiple of 7 early on, you know for user it would end with either 0 or 7. For instance,

    1631:
        163 - 2 = 161
        16 - 2 = 14
        
        You can stop with 14 and call 1631 as a multiple.
