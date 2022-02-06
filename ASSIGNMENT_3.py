def anagram_check(str1,str2):
    if sorted(str1)==sorted(str2):
        print("Yes")
    else:
        print("No")
anagram_check(input("Enter a string : ").lower(),input("Enter a string : ").lower())