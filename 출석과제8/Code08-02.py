inStr, outStr = "", ""
count, i = 0, 0
inStr = input("문자열을 입력하세요 : ")
count = len(inStr)
for i in range(0, count) :
     outStr += inStr[count - (i + 1)]
print("내용을 거꾸로 출력 --> %s" % outStr)
