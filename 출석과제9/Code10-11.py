from tkinter import * #tkinter모듈의 모든 것을 임포트한다
btnList = [""] * 9 #리스트변수 생성
fnameList = ["froyo.gif", "gingerbread.gif", "honeycomb.gif", "icecream.gif", "jellybean.gif", "kitkat.gif", "lollipop.gif", "marshmallow.gif", "nougat.gif"] #리스트 생성
photoList=[None] * 9 #리스트 생성
i, k = 0, 0 #변수 생성
xPos, yPos = 0, 0#변수 생성
num = 0#변수 생성
window = Tk()#화면에 윈도창 출력
window.geometry("210x210") #창크기 설정
for i in range(0, 9) : #for문(0부터 9까지)
    photoList[i] = PhotoImage(file = "gif/" + fnameList[i])#사진들을 리스트에 저장
    btnList[i] = Button(window, image = photoList[i])  #버튼생성
for i in range(0, 3) : #for문(0부터3까지)
    for k in range(0, 3) :#for문(0부터3까지)
        btnList[num].place(x = xPos, y = yPos) #사진출력 (x,y크기만큼)
        num += 1 #num=num+1
        xPos += 70 #xpos=xpos+70
    xPos = 0#초기값선언
    yPos += 70#ypos=ypos+70
window.mainloop()#mainloo
