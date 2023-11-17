class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.cameraOn = True
        self.spectatorMode = True

        self.hero = loader.loadModel("smiley")

        self.hero.setColor(1, 0.5, 0, 1)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)

        self.hero.reparentTo(render)

        self.CameraBind()

        self.acceptEvents()

    def CameraBind(self):
        base.disableMouse()
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        base.camera.setH(180)

        self.cameraOn = True

    def cameraUnBind(self):
        base.enableMouse()
        base.camera.reparentTo(render)

        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos((-pos[0], -pos[1], -pos[-2]-1))

        self.cameraOn = False
        
    def changeMode(self):
        if self.cameraOn:
            self.cameraUnBind()
        else:
            self.CameraBind()

    def turnLeft(self):
        angle = self.hero.getH()
        angle += 5
        self.hero.setH(angle)
    def turnRight(self):
        angle = self.hero.getH()
        angle -= 5
        self.hero.setH(angle)
    def turnUp(self):
        angle = self.hero.getP()
        angle -= 5
        self.hero.setP(angle)
    def turnDown(self):
        angle = self.hero.getP()
        angle += 5
        self.hero.setP(angle)


    def just_move(self, angle):
        pos = self.lookAt(angle)
        self.hero.setPos(pos)

    def try_move(self, angle):
        ...

    def move_to(self, angle):
        if self.spectatorMode:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def lookAt(self,angle):
        x = round(self.hero.getX())
        y = round(self.hero.getY())
        z = round(self.hero.getZ())

        dx, dy = self.checkDir(angle)

        return(x+dx, y+dy, z)
    

    def checkDir(self, angle):
        ''' повертає заокруглені зміни координат X, Y,
            відповідні переміщенню у бік кута angle.
            Координата Y зменшується, якщо персонаж дивиться на кут 0,
            та збільшується, якщо дивиться на кут 180.
            Координата X збільшується, якщо персонаж дивиться на кут 90,
            та зменшується, якщо дивиться на кут 270.  
            кут 0 (від 0 до 20)      ->        Y - 1
            кут 45 (від 25 до 65)    -> X + 1, Y - 1
            кут 90 (від 70 до 110)   ->  X + 1
            від 115 до 155            -> X + 1, Y + 1
            від 160 до 200            ->        Y + 1
            від 205 до 245            -> X - 1, Y + 1
            від 250 до 290            -> X - 1
            від 290 до 335            -> X - 1, Y - 1
            від 340                   ->        Y - 1  '''
        
        if angle >= 0 and angle <= 20:
            return (0,-1)
        elif angle <= 65:
            return(+1,-1)
        elif angle <= 110:
            return(+1,0)
        elif angle <= 155:
            return(+1,+1)
        elif angle <= 200:
            return(0,+1)
        elif angle <= 245:
            return(-1,+1)
        elif angle <= 290:
            return(-1,0)
        elif angle <= 335:
            return(-1,-1)
        else:
            return(0,-1)

    def forward(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)

    def backward(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)

    def left(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)


    def acceptEvents(self):
        base.accept("c", self.changeMode)

        base.accept(turn_left_key,self.turnLeft)
        base.accept(turn_left_key+"-repeat",self.turnLeft)

        base.accept(turn_right_key,self.turnRight)
        base.accept(turn_right_key+"-repeat",self.turnRight)

        base.accept(turn_up_key,self.turnUp)
        base.accept(turn_up_key+"-repeat",self.turnUp)

        base.accept(turn_down_key,self.turnDown)
        base.accept(turn_down_key+"-repeat",self.turnDown)

        base.accept(forward_key,self.forward)
        base.accept(forward_key+"-repeat",self.forward)

        base.accept(back_key,self.backward)
        base.accept(back_key+"-repeat",self.backward)

        base.accept(left_key,self.left)
        base.accept(left_key+"-repeat",self.left)

        base.accept(right_key,self.right)
        base.accept(right_key+"-repeat",self.right)



change_mode_key = "c"

turn_left_key = "arrow_left"
turn_right_key = "arrow_right"
turn_down_key = "arrow_down"
turn_up_key = "arrow_up"

forward_key = "w"
back_key = "s"
left_key = "a"
right_key = "d"
