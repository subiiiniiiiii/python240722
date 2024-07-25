#DemoForm2.py
#DeomForm2.ui(화면단)+DemoForm2.py(로직)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests
from bs4 import BeautifulSoup


# 디자인 파일을 로딩
form_class = uic.loadUiType("C:\\work\\DemoForm2.ui")[0]

class DemoForm(QMainWindow, form_class):
    #초기화매서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯메서드 추가
    def firstClick(self):
        
        url = "https://www.daangn.com/fleamarket/"
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.find_all("div",attrs={"class":"card-desc"}) 
        f = open("dangn.txt","a+",encoding="utf-8")
        for post in posts:
            titleElem = post.find("h2",attrs={"class":"card-title"})
            priceElem = post.find("div",attrs={"class":"card-price"})
            addrElem = post.find("div",attrs={"class":"card-region-name"})
            title = titleElem.text.strip()
            price = priceElem.text.strip()
            addr = addrElem.text.strip()
            print(f"{title}, {price} ,{addr}")
            f.write(f"{title}, {price} ,{addr}\n")
        f.close()
        self.label.setText("당근마켓 크롤링 완료")

    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")   
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭") 

#해당 모듈을 직접 실행했는지 여부를 체크
# Java, C언어 main() 함수가 진입점 (Entry Point)
if __name__ == "__main__":
    #실행프로세스 생성
    app = QApplication(sys.argv)
    #인스턴스 생성
    demoForm = DemoForm()
    #화면 보여주기
    demoForm.show()
    #이벤트 처리 대기 
    app.exec_()
