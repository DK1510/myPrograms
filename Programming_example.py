a = int(input())    #typecasting
if a>0:
    print('the given number is positive')
elif a<0:   #0<0
    print('the given number is negative')
else:
    print('the given number is zero')

a = int(input('Enter a: '))
b = int(input('Enter b: '))
if a>b: #10>15
    print('a is greater than b')
elif b>a:   #a<b 15>10
    print('b is greater than a')
else:
    print('both are equal')


s1 = input('Enter string1: ')
s2 = input('Enter string2: ')
if s1.casefold()==s2.casefold():    #if s1.lower() == s2.lower()
    print('s1 and s2 are equal')
else:
    print('s1 and s2 are not equal')


char = input('Enter a charater: ')
char = char.lower()
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
    print('its vowel')
else:
    print('its not vowel')


char = input('Enter a charater: ')
char = char.lower()
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
    print('its vowel')
else:
    print('its not vowel')

char = input('Enter a charater: ')
char = char.lower()
vowels = 'aeiou'    # vowels = ['a','e','i','u','o']
if char in vowels:
    print(char,'its vowel')
else:
    print(char,'its not vowel')

