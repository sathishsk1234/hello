a=str(input())
b='a','e','i','o','u','A','E','I','O','U'
if a in ('!','@','#','$',"%",'^','&','*'):
    print("invalid")
elif a in b:
    print("vowel")
else:
    print('consonant')