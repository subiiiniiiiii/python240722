# 전역변수
strName = "Not Class Member"

class DemoString:
    def __init__(self):
        #인스턴스 멤버 변수
        self.strName = "" 
    def set(self, msg):
        self.strName = msg
    def print(self):
        print(self.strName) #self.strName 이 아니라 strName이면 전역변수의 strName을 가져옴.


#instance 생성
d = DemoString()
d.set("First Message")
d.print()
