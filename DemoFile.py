#DemoFile.py

#파일 쓰기
f = open("demo.txt","wt",encoding ="utf-8")
f.write("첫번째라인\n두번째라인\n세번째라인\n")
f.close()

f = open("demo.txt","rt",encoding = "utf-8")
result = f.read()
print(result)

#리스트로 받기
f.seek(0)
lst =f.readlines()
print(lst)

f.close()

dir(str)