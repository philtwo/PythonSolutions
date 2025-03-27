
def isPalindrome(s: str) -> bool:
    # newStr = "" #this is the string that will have all the ignored characters removed

    # for c in s:
    #     if c.isalnum():
    #         newStr += c.lower()
    # return newStr == newStr[::-1] #this reverses the string
    l, r = 0, len(s) - 1 #two pointers
    while l < r:
        while l < r and not alphaNum(s[l]): #ignore non-alphanumeric characters
            l += 1 #move the left pointer to the right a space
        while r > l and not alphaNum(s[r]): #ignore non-alphanumeric characters
            r -= 1 #move the right pointer to the left a space
        if s[l].lower() != s[r].lower():
            return False
        l = l + 1
        r = r - 1
    return True #if the string is a palindrome, return True

def alphaNum(c):
    return ((ord('A') <= ord(c) <= ord('Z')) or 
            (ord('a') <= ord(c) <= ord('z')) or 
            (ord('0') <= ord(c) <= ord('9')))


def isIntPalindrome(x: int) -> bool:
    if x < 0:
        return False
    reverse = 0
    x_copy = x #make a copy of the original number
    while x > 0:
        reverse = (reverse * 10) + (x % 10) #reverse the number
        x //= 10 #remove the last digit of the number
    return reverse == x_copy #compare the reversed number with the original number

print("is \033[33mA_man,_a_plan,_a_canal: Panama\033[0m a palindrome: ", isPalindrome("A_man,_a_plan,_a_canal: Panama")) # True
print("is \033[33m121\033[0m a palindrome: ",  isIntPalindrome(121)) # True