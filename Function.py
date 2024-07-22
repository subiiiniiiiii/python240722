#Function.py

def setValue(newvalue):
    x = newvalue
    print("지역변수",x)


retValue = setValue(5)
print(retValue)

def swap(x,y):
    return y,x

print(swap(3,4))

def times(a=10,b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

def connectURI(server,port):
    strURL = "https://"+server+":"+port
    return strURL

print(connectURI("multi.com","80"))
print(connectURI(port = "8080",server="multi.com"))


# 이름해석 : LGB 이론 해석 규칙

x= 5
def func(a):
    return a+x

#호출
print(func(1))

def func2(a):
    x =1
    return a+x

print(func2(1))

#가변인자
def union(*ar):
    #지역변수 리스트 초기화
    result = []
    for item in ar:
        for x in item :
            if x not in result:
                result.append(x)
    return result


# 호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

#람다함수
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))

print((lambda x:x*x)(3))
print(globals())


