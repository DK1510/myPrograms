s = 'malayalom'
start = 0
end = len(s)-1
palindrome= 1
while start < end:
    if s[start]!=s[end]:
        palindrome = 0
        break
    start+=1    #start = start+1
    end-=1      #end = end-1

if palindrome==1:
    print(s,'is palindrome')
else:
    print(s, 'is not a palindrome')
