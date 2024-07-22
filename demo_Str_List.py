# demo_Str_List.py

strA = "python is very powerful"
strB = "파이썬은 강력해"
x = 100
y = 3.14

print(len(strA))
print(len(strB))

#슬라이드 연습
print(strA[0])
print(strA[0:6])
print(strA[:6])
print(strA[-3:])

#리스트 형식
colors = ["red","blue","green"]
print(colors)
print(type(colors))
colors.append("yellow")
colors.insert(1,"pink")
print(colors)
colors.remove("blue")
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)

#tuple은 읽기 전용 (검색전용)
#list는 추가 가능 a.insert(1,b)

print("id %s, name: %s"%("kim","김유신"))

#형식 변환
a = set((1,2,3))
print(a)
print(type(a))
b = list(a)
b.append(4)
print(b)

#tuple
tp =(10,20,30)
print(type(tp))
print(len(tp))

#fucntion definition
def clac(a,b):
    return a+b, a*b

#호출
result = clac(3,4)
print(result)
print("id %s, name:%s" % ("kim","김유신") )

#dictionary
device = {"아이폰":5,"아이패드":10}
print(type(device))
device["맥북"] = 15
device["아이폰"] = 6
del device["아이패드"]

print(device)
print(device["맥북"])

for item in device.items():
    print(item)


