import pygame
import random
import sys

# 파라미터로 받은 객체(entitry)를 화면에 그리기
def paintEntiry(entity , x, y): 
   monitor.blit(entity, (x, y))

# 점수를 화면에 쓴다.
def writeScore(score) :
    myfont =   pygame.font.Font('NanumGothic.ttf' , 20) # 한글 폰트
    txt = myfont.render(u'파괴한 우주괴물 숫자 : ' + str(score), True, (255-r,255-g,255-b))
    monitor.blit(txt, (10, sheight-40))   

### 함수 선언 부분 ###
def playGame() :
    global ship, monster, missile

    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256) 
    
    # 우주선 초기 위치
    shipX = swidth / 2  # 우주선 위치
    shipY = sheight * 0.8
    dx, dy = 0, 0  # 키보드를 누를때 우주선의 이동량
    fireCount = 0 # 맞힌 우주괴물 숫자

    # 우주괴물 준비 (랜덤한 이미지)
    monster= pygame.image.load(random.choice(monsterImage))
    monsterSize = monster.get_rect().size # 우주괴물 크기
    monsterX = 0 
    monsterY =random.randrange (0, int(swidth * 0.3)) # 상위 30% 위치까지만.
    monsterSpeed = random.randrange(1,5)

    # 미사일 준비
    missileX, missileY = None, None  # None은 미사일을 쏘지 않음
    
    while  True :
        (pygame.time.Clock()).tick(50)  # 게임 진행을 늦춰 줌(10~100 정도가 적당)
        monitor.fill( (r, g, b) ) # 화면 배경 칠하기
        
        for e in pygame.event.get() :
            if e.type in [pygame.QUIT]  :
                pygame.quit()
                sys.exit()

            # 키보드 누르면 우주선 이동 (누르고 있으면 계속 이동)
            if e.type in [pygame.KEYDOWN] :
                if e.key == pygame.K_LEFT:                 dx =  - 5
                elif e.key == pygame.K_RIGHT:             dx =  + 5
                elif e.key == pygame.K_UP:                 dy =   - 5
                elif e.key == pygame.K_DOWN:            dy =  + 5
                elif e.key == pygame.K_SPACE :  # 스페이스는 미사일 발사.
                    if missileX == None : # 기존에 총알이 나가고 있으면, 안쏴짐..
                        missileX = shipX + shipSize[0]/2 # 비행기 위치에서 미사일 발사.
                        missileY = shipY

            # 키보드를 떼면 우주선의 이동 멈춤
            if e.type in [pygame.KEYUP] :
                 if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT \
                    or e.key == pygame.K_UP or e.key == pygame.K_DOWN :
                     dx, dy = 0, 0

        # 우주선이 화면 안에서만 움직이게 하기
        if  (0 < shipX+dx and shipX+dx <= swidth-shipSize[0]) \
            and ( sheight/2 < shipY+dy and shipY+dy <= sheight-shipSize[1] ): # 화면의 중앙 까지만
            shipX += dx
            shipY += dy
        paintEntiry(ship, shipX, shipY) # 우주선 그리기

        # 우주괴물이 왼쪽에서 오른쪽으로 이동함.
        monsterX += monsterSpeed
        if monsterX > swidth :
            monsterX = 0
            monsterY =random.randrange (0, int(swidth * 0.3))
            # 우주괴물 이미지를 랜덤하게..
            monster= pygame.image.load(random.choice(monsterImage))
            monsterSize = monster.get_rect().size
            monsterSpeed = random.randrange(1,5)
           
        paintEntiry(monster, monsterX, monsterY)
        
        # 미사일 화면에 표시
        if missileX != None  : # 총알을 쏘면 위로 좌표 변경됨.
            missileY -= 10
            if missileY  < 0 :
                  missileX, missileY= None, None  # 총알 없어짐
                  
        if missileX != None : # 미사일을 쏜 적이 있으면 미사일 그리기
            paintEntiry(missile, missileX, missileY)
            # 우주괴물이 미사일에 맞은 것 체크 = 미사일이 우주괴물 범위 안에 있으면....
            if   ( monsterX < missileX  and  missileX < monsterX + monsterSize[0]) and \
                  ( monsterY < missileY  and  missileY < monsterY + monsterSize[1]) :
                fireCount += 1

                # 우주괴물 이미지를 랜덤하게..
                monster= pygame.image.load(random.choice(monsterImage))
                monsterSize = monster.get_rect().size
                monsterX = 0
                monsterY =random.randrange (0, int(swidth * 0.3))
                monsterSpeed = random.randrange(1,5)
                # 미사일 초기화
                missileX, missileY= None, None  # 총알 없어짐

        writeScore(fireCount) # 점수를 화면 쓴다.
        pygame.display.update() # 화면 업데이트하기.
        
### 전역 변수 선언 부분 ###
r, g, b = [0] * 3  # 게임 배경색
swidth, sheight = 500, 700 # 화면 크기
monitor = None # 게임 화면
ship, shipSize = None, 0 # 우주선과 크기

monsterImage = ['monster01.png', 'monster02.png', 'monster03.png', 'monster04.png', \
                'monster05.png', 'monster06.png', 'monster07.png', 'monster08.png' \
                , 'monster09.png', 'monster10.png']
monster = None #  우주괴물
missile = None # 미사일

### 메인 코드 부분 ###
pygame.init()
monitor = pygame.display.set_mode( (swidth, sheight) )
pygame.display.set_caption('우주괴물 무찌르기')

# 우주선 준비
ship = pygame.image.load('ship02.png')
shipSize = ship.get_rect().size
missile = pygame.image.load('missile.png') # 미사일

playGame()
