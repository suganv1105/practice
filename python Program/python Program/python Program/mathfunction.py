import math

Tup = (10.98, 20.26, 30.05, -40.95 , 50.45) # Tuple Declaration
Lis = [-10.98, 32.65, -39.59, -42.15 , 35.97] # List Declaration
ceilLis2=[]
floorLis2=[]
copysigLis=[]
roundLis2=[]
print('Ceiling value of Positive Number = %.2f' %math.ceil(10))
print('Ceiling value of Negative Number = %.2f' %math.ceil(-15))
print('Ceiling value of Tuple Item = %.2f' %math.ceil(Tup[2]))
print('Ceiling value of List Item = %.2f' %math.ceil(Lis[2]))
print("The Value of 'PI' after the Ceil function is: ", math.ceil(math.pi))
print('Ceiling value of Multiple Number = %.2f' %math.ceil(10 + 20 - 40.65))
print('Ceiling value of Positive Number = %.2f' %math.floor(10))
print('Ceiling value of Negative Number = %.2f' %math.floor(-15))
print('Ceiling value of Tuple Item = %.2f' %math.floor(Tup[2]))
print('Ceiling value of List Item = %.2f' %math.floor(Lis[2]))
print("The Value of 'PI' after the Ceil function is: ", math.floor(math.pi))
print('Ceiling value of Multiple Number = %.2f' %math.floor(10 + 20 - 40.65))
#print('Ceiling value of String Number = ', math.ceil('Python'))
print('Calculating CopySign of Positive Number = %.2f' %math.copysign(2, 3))
print('Calculating CopySign of Negative Number = %.2f' %math.copysign(-2, 3))
print('Calculating CopySign of Positive Decimal = %.2f' %math.copysign(5.63, -3.0))
print('Calculating CopySign of Negative Decimal = %.2f' %math.copysign(-2.48, 1.15))
print('Calculating Power of of Tuple Item = %.2f' %math.copysign(Tup[2], 2.25))
print('Calculating Power of of Tuple Item = %.2f' %math.copysign(Tup[2], -2.25))
print('Calculating Power of List Item = %.2f' %math.copysign(Lis[4], 4.5))
print('Calculating Power of List Item = %.2f' %math.copysign(Lis[4], -4.5))
print('Calculating CopySign of Multiple Number = %.2f' %math.copysign(1 + 2 - 12.65, 2))
print('round() Function on Positive Decimal = %.2f' %round(10.98763))
print('round() Function on Negative Decimal = %.2f' %round(-15.48476))
print('round() Function with Second argument = %.3f' %round(10.98763, 3))
print('round() Function with Second argument = %.3f' %round(-15.48476, 3))
print('round() Function on Tuple Item = %d' %round(Tup[2]))
print('round() Function on Tuple Item = %d' %round(Tup[4]))
print('round() Function on List Item = %d' %round(Lis[2]))
print('round() Function on List Item = %d' %round(Lis[4]))
print('round() Function on Multiple Number = %.2f' %round(10 + 20 - 40.6578, 2))


for i in range(0,len(Lis)):
    print('Before ceiling ',Lis[i])
    print('after ceiling ', math.ceil(Lis[i]))
    print('Before floor ',Lis[i])
    print('after floor ', math.floor(Lis[i]))
    print('after round', Lis[i])
    print('after round',round(Lis[i],3))
    ceilLis2.append(math.ceil(Lis[i]))
    floorLis2.append(math.floor(Lis[i]))
    copysigLis.append(math.copysign(Lis[i],-1))
    roundLis2.append(round(Lis[i],3))

print(ceilLis2)
print(copysigLis)
print(floorLis2)
print(roundLis2)

Str1 = 'learn Python at tutorial gateway'
Str2 = 'a'
Str3 = Str1.count(Str2)
print("Total Number of a's in String1 = ", Str3)
Str4 = Str1.count(Str2, 6, 25)
print("Total Number of a's in Sliced String1 = ", Str4)
Str5 = Str1.count(Str2, 6, len(Str1))
print("Total Number of a's in Sliced String1 = ", Str5)
# Performing Count function directly
Str6 = 'learn Python at tutorial python'.count('a', 0, 60)
print("Total Number of a's in String1 = ", Str6)

Str1 = 'learn Python at tutorial'
Str2 = 'a'
count = 0
for char in Str1:
           if char == Str2:
                      count = count + 1
print("Total Number of a's in String1 = ", count)


Tup = (1, 2, 3, 4 , 5) # Tuple Declaration
factLis = [6, 7, 8, 5 , 9] # List Declaration
factlista=[]
print('Factoial() Function on Positive Number = %.2f' %math.factorial(3))
print('Factoial() Function on Positive Decimal = %.2f' %math.factorial(6))
print('Factoial() Function on Tuple Item = %.2f' %math.factorial(Tup[2]))
print('Factoial() Function on List Item = %.2f' %math.factorial(factLis[4]))

for i in range(0,len(factLis)):
    print('Before factorial ',factLis[i])
    print('after factorial ', math.factorial(factLis[i]))
    factlista.append(math.factorial(factLis[i]))


print(factlista)


Tup = (10, 20, 12, -40 , 50) # Tuple Declaration
Lis = [-98, 32, -39, -42 , 15] # List Declaration

print('Calculating MOD of Positive Number = %.2f' %math.fmod(2, 3))
print('Calculating MOD of Negative Number = %.2f' %math.fmod(-14, 3))
print('Calculating MOD of Positive Decimal = %.2f' %math.fmod(22.45, 4.5))
print('Calculating MOD of Negative Decimal = %.2f' %math.fmod(-110, 14.78))
print('Calculating MOD of Tuple Item = %.2f' %math.fmod(Tup[2], 5))
print('Calculating MOD of Tuple Item = %.2f' %math.fmod(Tup[2], -5))
print('Calculating MOD of List Item = %.2f' %math.fmod(Lis[4], 4))
print('Calculating MOD of List Item = %.2f' %math.fmod(Lis[0], -15))
print('Calculating MOD of Multiple Number = %.2f' %math.fmod(10 + 20 - 12, 40))

print('Calculating Power of Positive Number = %.2f' %math.pow(2, 3))
print('Calculating Power of Negative Number = %.2f' %math.pow(-2, 3))
print('Calculating Power of String Number = ', math.pow(2, -3))
print('Calculating Power of of Tuple Item = %.2f' %math.pow(Tup[2], 2))
print('Calculating Power of List Item = %.2f' %math.pow(Lis[4], 4))
print('Calculating Power of Multiple Number = %.2f' %math.pow(1 + 2 - 12.65, 2))

print('TRUNC() Function on Positive Decimal = %d' %math.trunc(10.98763))
print('TRUNC() Function on Negative Decimal = %d' %math.trunc(-15.48476))
print('TRUNC() Function on Tuple Item = %d' %math.trunc(Tup[2]))
print('TRUNC() Function on Tuple Item = %d' %math.trunc(Tup[4]))
print('TRUNC() Function on List Item = %d' %math.trunc(Lis[2]))
print('TRUNC() Function on List Item = %d' %math.trunc(Lis[4]))
print('TRUNC() Function on Multiple Number = %d' %math.trunc(10 + 20 - 40.6578))

print('Square Root of Positive Number = %.2f' %math.sqrt(10))
print('Square Root of Negative Number = %.2f' %math.sqrt(25))
print('Square Root of Tuple Item = %.2f' %math.sqrt(Tup[2]))
print('Square Root of List Item = %.2f' %math.sqrt(Lis[4]))
print('Square Root of Multiple Number = %.2f' %math.sqrt(10 + 45 - 10))

print('EXP() Function on Positive Number = %.2f' %math.exp(1))
print('EXP() Function on Negative Number = %.2f' %math.exp(-1))
print('EXP() Function on Tuple Item = %.2f' %math.exp(Tup[2]))
print('EXP() Function on List Item = %.4f' %math.exp(Lis[2]))
print('EXP() Function on Multiple Number = %.4f' %math.exp(10 + 20 - 15.65))

print('Calculating GCD of Positive Number = %d' %math.gcd(2, 3))
print('Calculating GCD of Negative Number = %d' %math.gcd(-2, 3))

print('Calculating GCD of Zero = %d' %math.gcd(0, 0))
print('Calculating GCD of Zero & Non-Zero element = %d' %math.gcd(2, 0))
print('Calculating GCD of Non-Zero & Zero element = %d' %math.gcd(0, 4))
print('Calculating GCD of of Tuple Item = %d' %math.gcd(Tup[2], 4))
print('Calculating GCD of of Tuple Item = %d' %math.gcd(Tup[2], -6))
print('Calculating GCD of List Item = %d' %math.gcd(Lis[4], 5))
print('Calculating GCD of List Item = %d' %math.gcd(Lis[4], -45))
print('Calculating GCD of Multiple Number = %d' %math.gcd(10 + 20 - 12, 40))

print('Arc Cosine value of Positive Number = %.2f' %math.acos(1))
print('Arc Cosine value of Negative Number = %.2f' %math.acos(-1))
print('Arc Cosine value of Multiple Number = %.2f' %math.acos(0.10 + 0.20 - 0.40))

print('Arc sin value of Positive Number = %.2f' %math.asin(1))
print('Arc sin value of Negative Number = %.2f' %math.asin(-1))
print('Arc sin value of Multiple Number = %.2f' %math.asin(0.10 + 0.20 - 0.40))

print('c = √(a² + b²)')
print('HYPOT value of Positive Number = %.2f' %math.hypot(2, 3))
print('HYPOT value of Negative Number = %.2f' %math.hypot(2, -4))
print('HYPOT value of Tuple Item = %.2f' %math.hypot(Tup[3], Tup[2]))
print('HYPOT value of List Item = %.2f' %math.hypot(Lis[2], Lis[4]))
print('HYPOT value of Multiple Number = %.2f' %math.hypot(2 + 7 - 4, 9 - 5))

