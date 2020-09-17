str1 = str(input())
str2 = str(input())
str3 = ''

length = len(str1)

for i in range(0, length):
    if str1[i] != str2[i]:
        str3 = str2[0:i+1] + str1[i+1:length]
        print(str3)