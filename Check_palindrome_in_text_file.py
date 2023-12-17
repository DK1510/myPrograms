def check_palindrome(word):
    start = 0
    end = len(word)-1
    while(start < end):
        if word[start] != word[end]:
            return 0
        start+=1
        end-=1
    return 1

f = open('D://Logic_360//test.txt','r')
string = f.read()   #string
l = string.split()
print(l)
p = []
f1 = open('D:/Logic_360/test101.txt','a')
for word in l:
    s = ''  #empty string
    for letter in word:
        if letter.isalnum():
            s+=letter
        print(s)
    if  len(s)>=2 and check_palindrome(s):
            f1.write(s+'\n')
print(p)
f.close()
f1.close()