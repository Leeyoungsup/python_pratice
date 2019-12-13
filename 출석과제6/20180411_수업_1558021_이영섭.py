import random
import pdb
a,b,c=0,'',''
ca,cb=[(1,2,3),(4,5,6),(7,8,9)],['1','2','3','4','5','6','7','8','9']
ox=['o','x']
qwer=0
h=0
count1,count2,count3,count4,count5,count6,count7,count8,count9=0,0,0,0,0,0,0,0,0
b=input('o와x중 하나를 입력하시오:')
ox.remove(b)

def inputNo(a,b):
    a=int(input('1~9숫자를 입력하시오'))
    global count1,count2,count3,count4,count5,count6,count7,count8,count9  
    if b=='o':
        if a==1:
            count1+=1
            if count1==2:
                print('중복된수입니다')
                count1=1
                inputNo(0,'o')
            else:
                del(cb[0])
                cb.insert(0,'o')
        elif a==2:
            count2+=1
            if count2==2:
                print('중복된수입니다')
                count2=1
                inputNo(0,'o')
            else:
                del(cb[1])
                cb.insert(1,'o')
            
        elif a==3:
            count3+=1
            if count3==2:
                print('중복된수입니다')
                count3=1
                inputNo(0,'o')
            else:
                del(cb[2])
                cb.insert(2,'o')
            
        elif a==4:
            count4+=1
            if count4==2:
                print('중복된수입니다')
                count4=1
                inputNo(0,'o')
            else:
                del(cb[3])
                cb.insert(3,'o')
            
        elif a==5:
            count5+=1
            if count5==2:
                print('중복된수입니다')
                count5=1
                inputNo(0,'o')
            else:
                del(cb[4])
                cb.insert(4,'o')
           
        elif a==6:
            count6+=1
            if count6==2:
                print('중복된수입니다')
                count6=1
                inputNo(0,'o')
            else:
                del(cb[5])
                cb.insert(5,'o')
            
        elif a==7:
            count7+=1
            if count7==2:
                print('중복된수입니다')
                count7=1
                inputNo(0,'o')
            else:
                del(cb[6])
                cb.insert(6,'o')
            
        elif a==8:
            count8+=1
            if count8==2:
                print('중복된수입니다')
                count8=1
                inputNo(0,'o')
            else:
                del(cb[7])
                cb.insert(7,'o')
            
        elif a==9:
            count9+=1
            if count9==2:
                print('중복된수입니다')
                count9=1
                inputNo(0,'o')
            else:
                del(cb[8])
                cb.insert(8,'o')
            
    else:
        if a==1:
            count1+=1
            if count1==2:
                print('중복된수입니다')
                count1=1
                inputNo(0,'x')
            else:
                del(cb[0])
                cb.insert(0,'x')
        elif a==2:
            count2+=1
            if count2==2:
                print('중복된수입니다')
                count2=1
                inputNo(0,'x')
            else:
                del(cb[1])
                cb.insert(1,'x')
            
        elif a==3:
            count3+=1
            if count3==2:
                print('중복된수입니다')
                count3=1
                inputNo(0,'x')
            else:
                del(cb[2])
                cb.insert(2,'x')
            
        elif a==4:
            count4+=1
            if count4==2:
                print('중복된수입니다')
                count4=1
                inputNo(0,'x')
            else:
                del(cb[3])
                cb.insert(3,'x')
            
        elif a==5:
            count5+=1
            if count5==2:
                print('중복된수입니다')
                count5=1
                inputNo(0,'x')
            else:
                del(cb[4])
                cb.insert(4,'x')
           
        elif a==6:
            count6+=1
            if count6==2:
                print('중복된수입니다')
                count6=1
                inputNo(0,'x')
            else:
                del(cb[5])
                cb.insert(5,'x')
            
        elif a==7:
            count7+=1
            if count7==2:
                print('중복된수입니다')
                count7=1
                inputNo(0,'x')
            else:
                del(cb[6])
                cb.insert(6,'x')
            
        elif a==8:
            count8+=1
            if count8==2:
                print('중복된수입니다')
                count8=1
                inputNo(0,'x')
            else:
                del(cb[7])
                cb.insert(7,'x')
            
        elif a==9:
            count9+=1
            if count9==2:
                print('중복된수입니다')
                count9=1
                inputNo(0,'x')
            else:
                del(cb[8])
                cb.insert(8,'x')
def recordDisplay(cq,cw):
    for i in range(0, 9) :
        print("%3s" % cb[i],end='')
        if i==2 or i==5 or i==8:
            print("")
    print('')
def computer(a,b):
    global count1,count2,count3,count4,count5,count6,count7,count8,count9
    a=random.randrange(1,10)
    b=random.choice(ox)
    global cb
    if b=='o':
        if a==1:
            count1+=1
            if count1==2:

                count1=1
                computer(0,'o')
            else:
                del(cb[0])
                cb.insert(0,'o')
        elif a==2:
            count2+=1
            if count2==2:
                count2=1
                computer(0,'o')
            else:
                del(cb[1])
                cb.insert(1,'o')
            
        elif a==3:
            count3+=1
            if count3==2:
                count3=1
                computer(0,'o')
            else:
                del(cb[2])
                cb.insert(2,'o')                
        elif a==4:
            count4+=1
            if count4==2:
                count4=1
                computer(0,'o')
            else:
                del(cb[3])
                cb.insert(3,'o')
        elif a==5:
            count5+=1
            if count5==2:
                count5=1
                computer(0,'o')
            else:
                del(cb[4])
                cb.insert(4,'o')
        elif a==6:
            count6+=1
            if count6==2:
                count6=1
                computer(0,'o')
            else:
                del(cb[5])
                cb.insert(5,'o')
        elif a==7:
            count7+=1
            if count7==2:
                count7=1
                computer(0,'o')
            else:
                del(cb[6])
                cb.insert(6,'o')
        elif a==8:
            count8+=1
            if count8==2:

                count8=1
                computer(0,'o')
            else:
                del(cb[7])
                cb.insert(7,'o')
            
        elif a==9:
            count9+=1
            if count9==2:

                count9=1
                computer(0,'o')
            else:
                del(cb[8])
                cb.insert(8,'o')
            
    else:
        if a==1:
            count1+=1
            if count1==2:

                count1=1
                computer(0,'x')
            else:
                del(cb[0])
                cb.insert(0,'x')
        elif a==2:
            count2+=1
            if count2==2:
                count2=1
                computer(0,'x')
            else:
                del(cb[1])
                cb.insert(1,'x')
            
        elif a==3:
            count3+=1
            if count3==2:

                count3=1
                computer(0,'x')
            else:
                del(cb[2])
                cb.insert(2,'x')
            
        elif a==4:
            count4+=1
            if count4==2:

                count4=1
                computer(0,'x')
            else:
                del(cb[3])
                cb.insert(3,'x')
            
        elif a==5:
            count5+=1
            if count5==2:

                count5=1
                computer(0,'x')
            else:
                del(cb[4])
                cb.insert(4,'x')
           
        elif a==6:
            count6+=1
            if count6==2:

                count6=1
                computer(0,'x')
            else:
                del(cb[5])
                cb.insert(5,'x')
            
        elif a==7:
            count7+=1
            if count7==2:

                count7=1
                computer(0,'x')
            else:
                del(cb[6])
                cb.insert(6,'x')
            
        elif a==8:
            count8+=1
            if count8==2:

                count8=1
                computer(0,'x')
            else:
                del(cb[7])
                cb.insert(7,'x')
            
        elif a==9:
            count9+=1
            if count9==2:

                count9=1
                computer(0,'x')
            else:
                del(cb[8])
                cb.insert(8,'x')
def judge1(cd):
    if cd[0]==cd[3]==cd[6] or cd[1]==cd[4]==cd[7] or cd[2]==cd[5]==cd[8] or cd[0]==cd[1]==cd[2] or cd[3]==cd[4]==cd[5] or cd[6]==cd[7]==cd[8] or cd[0]==cd[4]==cd[8] or cd[2]==cd[4]==cd[6]:
        global qwer
        print("승리")
        qwer=1
        gameover(0)
def judge2(cd):
    if cd[0]==cd[3]==cd[6] or cd[1]==cd[4]==cd[7] or cd[2]==cd[5]==cd[8] or cd[0]==cd[1]==cd[2] or cd[3]==cd[4]==cd[5] or cd[6]==cd[7]==cd[8] or cd[0]==cd[4]==cd[8] or cd[2]==cd[4]==cd[6]:
        global qwer
        print("패배")
        gameover(0)
        qwer=1
def gameover(qwer):
    print("끝났습니다")
    
while True:
    
    inputNo(0,b)
    print('자신')
    recordDisplay(ca,cb)
    h+=1
    judge1(cb)
    if qwer==1:
        break
    if h==5:
        print('무승부')
        gameover(0)
        break
    computer(0,'')
    print("컴퓨터")
    recordDisplay(ca,cb)
    judge2(cb)
    if qwer==1:
        break
