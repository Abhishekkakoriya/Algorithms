# SUM OF DIGIT IN A RANGE
# num = int(input("enter start:"))
# end = int(input("enter end:"))
# sum = 0
# for i in range(num,end):
#     sum+=i
# print(sum)

# CHECK FOR LEAP YEAR
# year = 2004
# if (year%4 == 0 and year%100!=0) or (year%400 == 0):
#     print("Leap year")
# else:
#     print("Not Leap Year")

# CHECK PRIME NUMBER

# low = 2
# high = 10
# prime = []
# for i in range(low, high+1):
#     flag = 0
#     if i < 2:
#         continue
#     if i == 2:
#         prime.append(2)
#         continue
#     for x in range(2, i):
#         if i % x == 0:
#             flag = 1
#             break
#
#     if flag == 0:
#         prime.append(i)
#
# print(prime)

# EASY METHOD

# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=" ")

# SUM OF DIGITS OF NUMBER

# num = input("Enter a number: ")
# sum = 0
# for i in num:
#     sum+=int(i)
# print(sum)

# SUM OF DIGITS IN A NUMBER ANOTHER METHOD

# num = 12345
# sum = 0
# while num !=0:
#     digit = int(num%10)
#     sum += digit
#     num = num/10
# print(sum)

# REVERSE OF A NUMBER

# num = 23466
# reverse = 0
# while num != 0:
#     remainder = num % 10
#     reverse = (reverse * 10) + remainder
#     num = num // 10
# print(reverse)

# PALINDROME

# num = 121
# temp = num
# reverse = 0
# while num!=0:
#     remainder = num % 10
#     reverse = (reverse * 10) + remainder
#     num = num // 10
#
# if temp == reverse:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# USING STRING
# string = "radar"
# reverse = string[::-1]
# print(reverse)
# if reverse == string:
#     print("palindrome")
# else:
#     print("not palindrome")

# FIND A NUMBER ARMSTRONG OR NOT

# number = 371
# temp = number
# digit, sum = 0, 0
# length = len(str(number))
#
# while temp != 0:
#     digit = temp % 10
#     temp = temp//10
#     sum += pow(digit,length)
#
# if sum == number:
#     print("Armstrong")
# else:
#     print("Not")

# FIBONNACI SERIES

# num = int(input("Enter a number: "))
# n1,n2 = 0,1
# print("Fibonnaci series: ", n1, n2, end=" ")
# for i in range(2, num):
#     n3 = n1 + n2
#     n1 = n2
#     n2 = n3
#     print(n3, end=" ")
# print()

# FIND the Nth term of fibonnaci series

# def fibonnaci(n):
#     if n < 2:
#         return n
#     fs = [0, 1]
#     for i in range(1, n):
#         fs.append(fs[i] + fs[i-1])
#
#     return fs[n]
#
#
# n = 10
# print(fibonnaci(n-1))

# FACTORIAL OF A NUMBER

# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(6))

# Perfect number

# n = int(input("Enter any number: "))
# sum = 0
# for i in range(1,n):
#     if n % i == 0:
#         sum+=i
# 
# if sum == n:
#     print("perfect number")
# else:
#     print("Not a perfect number")


# Check for perfect square in python
# import math
#
# def checkforperfectsquare(x):
#     if math.ceil(math.sqrt(n)) == math.floor(math.sqrt(n)):
#         return True
#     else:
#         return False
#
# n = 49
# print(checkforperfectsquare(n))


# TO CHECK AUTOMORPHIC NUMBER

# num = int(input("enter a no : "))
# square = pow(num, 2)
# mod = pow(10, len(str(num)))
#
# if square % mod == num:
#     print("automorphic")
# else:
#     print("not an automorphic")


# TO CHECK HARSHAD NUMBER

# num = 81
# temp = num
# digit = 0
# sum = 0
#
# while num != 0:
#     digit = num % 10
#     sum+=digit
#     num=num//10
#
# if temp % sum == 0:
#     print("Harshad number")
# else:
#     print("not a harshad number")

# HCF OF TWO NUMBERS

# num1 = 36
# num2 = 60
# hcf = 1
# for i in range(1, min(num1, num2)):
#     if num1 % i == 0 and num2 % i ==0:
#         hcf = i
#
# print(hcf)

# LCM OF TWO NUMBERS

# num1 = 12
# num2 = 14
#
# for i in range(max(num1, num2), (num1*num2) + 1):
#     if i % num1 == i % num2 == 0:
#         lcf = i
#         break
# print(lcf)

# Binary to decimal conversion

# num = 10
# binary = num
# decimal = 0
# base = 1
#
# while num!=0:
#     rem = num % 10
#     decimal = decimal + rem * base
#     num = num//10
#     base = base * 2
#
# print("Binary number is {}\nDecimal no. is {}".format(binary,decimal))

# OCTAL TO DECIMAL

# num = 512
# binary = num
# decimal = 0
# base = 1
#
# while num != 0:
#     rem = num % 10
#     decimal = decimal + rem * base
#     num = num//10
#     base = base * 8
#
# print("octal number is {}\nDecimal no. is {}".format(binary, decimal))

# InBuilt Function

# octal_num = 21
# decimal = int(str(octal_num), 10)
# print(decimal)


# DECIMAL TO BINARY CONVERSION

# num = 21
# binary = num
# decimal = 0
# base = 1
#
# while num!=0:
#     rem = num % 2
#     decimal = decimal + rem * base
#     num = num//2
#     base = base * 10
#
# print("Decimal number is {}\nBinary no. is {}".format(binary,decimal))

# DECIMAL TO OCTAL CONVERSION

# num = 148
# binary = num
# decimal = 0
# base = 1
#
# while num!=0:
#     rem = num % 8
#     decimal = decimal + rem * base
#     num = num//8
#     base = base * 10
#
# print("Decimal number is {}\nOCtal no. is {}".format(binary,decimal))

# PERMUTATION IN WHICH N PEOPLE CAN OCCUPY R SEAT IN A CLASSROOM

# def fact(num):
#     if num == 0:
#         return 1
#     else:
#         return num * fact(num-1)
#
# n = int(input("Enter number of people: "))
# r = int(input("Enter number of seats: "))
#
# p = fact(n) // fact(n-r)
#
# print("Total possible arrangement: ", p)

# MAXIMUM POSSIBLE HANDSHAKE IN A ROOM

# N = 30
# handshakes = int(N * ((N-1) / 2))
# print("Maximum possible handshake is:", handshakes)


# ADDITION OF TWO FRACTIONS

# g1nume, g1deno = map(int, (input("Enter any number: ").split(" ")))
# g2nume, g2deno = map(int, (input("Enter any number: ").split(" ")))
# n = g1deno*g2deno
# o = g2deno*g1nume
# h = g1deno*g2nume
# k = o + h
# print(k,"/",n)

# REPLACE ALL 0's WITH 1 IN GIVEN INTEGER

# n = int(input("Enter number: "))
# s = str(n)
# l = []
#
# for i in s:
#     if i == '0':
#         l.append('1')
#     else:
#         l.append(i)
#
# ns = ""
#
# for i in l:
#     ns += i
#
# print(int(ns))

# SECOND METHOD

# n = int(input("Enter a number: "))
# string = str(n)
# replace = string.replace("0","1")
# print(int(replace))


# EXPRESSING SUM OF TWO PRIME NUMBERS

# num = int(input("Enter the number"))
# count = 0
#
# def is_prime(n):
#     fact = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             fact += 1
#     if fact == 2:
#         return True
#     else:
#         return False
#
#
# for j in range(2, num//2+1):
#     if is_prime(j) and is_prime(num-j):
#         count += 1
#         print(j, "+", num-j, "=", num)
#     if count == 0:
#         print(num, "can’t be represented as a sum of two prime numbers")

# COUNT POSSIBLE DECODING OF A GIVEN DIGIT SEQUENCE

# def cnt_decoding_digits(dig, a):
#     cnt = [0] * (a + 1)
#     cnt[0], cnt[1] = 1, 1
#
#     for k in range(2, a + 1):
#         cnt[k] = 0
#         cnt[k] = cnt[k - 1]
#
#         if dig[k - 2] == '1' or (dig[k - 2] == '2' and dig[k - 1] < '7'):
#             cnt[k] += cnt[k - 2]
#
#     return cnt[a]
#
#
# dig = "141"
# print("Possible count of decoding of the sequence :", cnt_decoding_digits(dig, len(dig)))

# PRINT PRIME NUMBER IN A RANGE

# for i in range(2, 100):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=" ")

# CALCULATE NO. ofDIGIT IN A NUMBER

# num = 234589
# count = 0
# while num != 0:
#     num = num // 10
#     count+=1
#
# print(count)

# Convert digit/number to words

# from num2words import num2words
#
# print(num2words(101))
# print(num2words(11098,  to="ordinal"))


# Python Program to count the number of days in a given month of a year

# month = 12
# year = 2012
#
# if ((month == 2) and ((year % 4 == 0) or ((year % 100 == 0) and (year % 400 == 0)))):
#     print("Number of days is 29");
#
# elif (month == 2):
#     print("Number of days is 28");
#
# elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
#     print("Number of days is 31");
#
# else:
#     print("Number of days is 30");

# FINDING ROOTS OF QUADRATIC EQUATION

# import math
#
# def findroots(a, b, c):
#     if a == 0:
#         print("Inavlid")
#         return -1
#
#     d = b * b - 4 * a * c
#     sqrt_val = math.sqrt(abs(d))
#
#     if d > 0:
#         print("Roots are real and different ")
#         print((-b + sqrt_val)/(2 * a))
#         print((-b - sqrt_val)/(2 * a))
#     elif d == 0:
#         print("Roots are real and same")
#         print(-b / (2*a))
#     else:
#         print("Roots are complex")
#         print(- b / (2*a), "+ i", sqrt_val)
#         print(- b / (2*a), "- i",sqrt_val)
#
# a = 1
# b = 4
# c = 4
# findroots(a, b, c)

