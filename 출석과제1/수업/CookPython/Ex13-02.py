from tkinter import *
import sqlite3

## 함수 선언 부분 ## 
def loadImage(fname) :  # raw --> DB
    global inImage, XSIZE, YSIZE
    con, cur = None, None
    row, col, data, sql = 0, 0, 0, ''
    con = sqlite3.connect("C:/CookPython/RAW")  # DB가 저장된 폴더까지 지정
    cur = con.cursor()
    fp = open(fname, 'rb')
    for row in range(0, XSIZE) :
        for col in range(0, YSIZE) :
            data = int(ord(fp.read(1)))
            sql = "INSERT INTO rawTable VALUES(" + str(row) + "," + str(col) + "," + str(data) + ")"
            cur.execute(sql)

    fp.close()
    con.commit()
    con.close()

def loadDatabase() :  # DB --> 메모리
    global inImage, XSIZE, YSIZE
    con, cur = None, None
    row, col, data = 0, 0, 0
    record = None # 테이블에서 읽어온 한 행
    con = sqlite3.connect("C:/CookPython/rawDB")
    cur = con.cursor()  
    cur.execute("SELECT * FROM rawTable")
    # 빈 inImage 생성
    for i in range(0, XSIZE) :
        tmpList = []
        for k in range(0, YSIZE) :
            data = 0
            tmpList.append(data)
        inImage.append(tmpList)

    # 테이블 --> inImage
    while (True) :
        record = cur.fetchone()
        if record== None :
            break;
        row = record[0]; col = record[1]; data = record[2]
        inImage[row][col] = data
    
    con.close()

def displayImage(image) :
    global XSIZE, YSIZE
    for i in range(0, XSIZE) :
        for k in range(0, YSIZE) :
            data = image[i][k]
            paper.put("#%02x%02x%02x" % (data, data, data), (k, i))

## 전역 변수 선언 부분
window, canvas, XSIZE, YSIZE = None, None, 256, 256
inImage = [] # 2차원 리스트 (메모리)

## 메인 코드 부분 ##
if __name__ == "__main__" :
    window = Tk()
    window.title("RAW-->DB")
    canvas = Canvas(window, height = XSIZE, width = YSIZE)
    paper = PhotoImage(width = XSIZE, height = YSIZE)
    canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal")

    # 테이블 초기화
    con = sqlite3.connect("C:/CookPython/rawDB")  # 소스코드가 저장된 폴더에 생성됨
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS rawTable")
    cur.execute("CREATE TABLE rawTable(row  int , col int, data int)") # 행,열,픽셀값
    con.commit()
    con.close()
    
    filename = 'RAW/tree3.raw'  # C:/CookPython/RAW/tree.raw
    loadImage(filename) # 파일 --> 데이터베이스
    loadDatabase() # 데이터베이스 --> 메모리
    displayImage(inImage) # 메모리 --> 화면 

    canvas.pack()
    window.mainloop()
