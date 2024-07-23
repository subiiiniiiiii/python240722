# DemoFilter.py

lst =[10,25,30]
iterl = filter(None,lst)
for item in iterl:
    print("item: {0}".format(item))


#함수 정의
def getBiggerThan20(i):
    return i>20

print("----필터링 함수 사용-----")
iterl = filter(getBiggerThan20, lst)
for item in iterl:
    print("item:{0}".format(item))


print("----람다 함수 사용-----")
iterl = filter(lambda x:x>20, lst)
for item in iterl:
    print("item:{0}".format(item))