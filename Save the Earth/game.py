import turtle,random
ss=random.randint(1,5)
t=turtle.Turtle()
t.up()
t.goto(-340,-200)
t.down()
t.goto(340,-200)
t.up()
t.goto(0,-210)
t.left(90)
t.speed(0)
n=turtle.Turtle()
n.up()
n.setposition(random.randint(-200,200),250)
n.left(90)
n.resizemode("user")
n.shapesize(ss,ss,0)
n.shape("circle")
s=turtle.Screen()
c=turtle.getcanvas()
t1=t.clone()
t1.color("yellow")
t1.resizemode("user")
t1.shapesize(.2,1,0)
s.bgpic("space.png")
jet="jet.gif"
s.addshape(jet)
t.shape(jet)
t1.speed(0)
nt=True
ac=False
fire=False
score=0
i=0
ff=1
tt=2000
def color():
    global ss
    if ss==5:
        n.color("red")
    elif ss==4:
        n.color("orange")
    elif ss==3:
        n.color("blue")
    elif ss==2:
        n.color("cyan")
    else:
        n.color("green")
def mm():
    global i
    color()
    if i==1:
        n.setheading(random.randint(0, 360))
        i=random.randint(1,3)
    elif i==2:
        n.setheading(random.randint(0, 360))
        i=random.randint(1,3)
    else:
        n.setheading(n.towards(t1.xcor(), t1.ycor()))
        i=random.randint(1,3)
    s.ontimer(mm, int(tt))
mm()
def m():
    global nt,ac,fire,score,ss,tt,ff
    color()
    n.fd(.1*(score+1))
    if fire==True:
        t1.fd(10*ff)
        if n.distance(t1.xcor(),t1.ycor())<20*ss/2 and nt==True:
            ss-=ff
            score += 1
            if ss<=1 or score>25:
                ss=random.randint(1,5)
                n.hideturtle()
                n.setposition(random.randint(-200, 200), 250)
                n.showturtle()
            s.update()
            n.resizemode("user")
            n.shapesize(ss,ss,0)
            t1.setposition(t.xcor(),t.ycor()-5)
            t1.setheading(90)
            ac=False
            fire=False
        if   t1.ycor()>=280 or t1.xcor()>=330 or t1.xcor()<=-330or t1.ycor()<=-280:
            t1.setposition(t.xcor(),t.ycor()-5)
            t1.setheading(90)
            ac = False
            fire=False
    if score>80:
        tt=50
    elif score>70:
        tt=100
    elif score>60:
        tt=250
    elif score>50:
        tt=500
        ff=2
    elif score>25:
        tt=1000
    elif score>10:
        tt=1500
    else:
        tt=2000
    if n.ycor()<-(200-(20*ss/2)):
        xx=turtle.Turtle()
        xx.hideturtle()
        xx.up()
        xx.right(180)
        xx.fd(150)
        xx.color("white")
        xx.write("Game Over  Score : "+str(score),font=("Arial",20))
        return
    if n.xcor() > 340 or n.ycor() > 290 or n.xcor() < -340:
        n.setheading(n.towards(t.xcor(), t.ycor()))
        i = 3
    s.title("Save The Earth        Score : "+str(score))
    s.ontimer(m,1)
def a(x,y):
    global ac,fire
    if ac==False:
        t1.setposition(t.xcor(),t.ycor()-5)
        t1.setheading(90)
        t1.setheading(t1.towards(x, y))
        fire=True
        ac=True
m()
def aa(event):
    if t.xcor()>=-100:
        t.goto(t.xcor()-100,t.ycor())
        if ac==False:
            t1.goto(t1.xcor()-100,t1.ycor())
        s.update()
def dd(event):
    if t.xcor()<=100:
        t.goto(t.xcor()+100,t.ycor())
        if ac==False:
            t1.goto(t1.xcor()+100,t1.ycor())
        s.update()
def xx(evnt):
    global score
    score+=10
s.onclick(a,1)
c.bind("<a>", aa)
c.bind("<d>", dd)
c.bind("<Right>",dd)
c.bind("<Left>",aa)
c.bind("<x>",xx)
s.listen()
s.mainloop()
