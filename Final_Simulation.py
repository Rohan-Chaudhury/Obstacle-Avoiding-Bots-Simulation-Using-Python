import random
from tkinter import *
import math
import time

Width=1000
Height=800
root=Tk()
leftFrame=Frame(root)
leftFrame.pack(side=LEFT)


canvas=Canvas(root,width=Width,height=Height)

root.title("obs avoidance pso")

canvas.pack()

theta=0.0

goalpos=[600,610,620,630]

full_obstacle_list = [(380,420,460,500),(100,120,140,160),(50,130,90,170),(440,420,520,500)]
robotlist=[(60,70,80,90),(360,70,380,90)]
goallist=[(600,610,620,630),(550,610,570,630)]

xspeed=0.0
yspeed=0.0

#Obstacle
for obs in full_obstacle_list:
    canvas.create_oval(obs,fill='orange')

#start
for rpos1 in robotlist:

    canvas.create_oval(rpos1,fill="yellow")
#GOAL
for goalpos1 in goallist:
    
    canvas.create_oval(goalpos1,fill="green")
class Robot:
    def __init__(self,rpos,goalpos,full_obstacle_list):
        self.shape=canvas.create_oval(rpos,fill="red")
        self.theta=float(math.atan2(float(goalpos[1]-rpos[1]),float(goalpos[0]-rpos[0])))
        self.xspeed=float(3*math.cos(self.theta))
        self.yspeed=float(3*math.sin(self.theta))
    def move(self,goalpos):                                                          
        i=0         
        j=0          
        deta=0.0         
                
        #print(rpos,goalpos)
       
        
        
        

        z=0.0005
        f=50
        g=30
        
        canvas.move(self.shape,self.xspeed,self.yspeed)
        pos=canvas.coords(self.shape)
        obs =full_obstacle_list[0]
        deta= float(math.atan2(float(goalpos[1]-pos[1]),float(goalpos[0]-pos[0])))
        for obs1 in full_obstacle_list :
            if abs(obs1[0]-pos[0])<abs(obs[0]-pos[0]):
                obs=obs1
                
        print (deta)
        p=abs(pos[0]-obs[0]+f)
        k=abs(pos[0]-obs[2]-f)
        l=abs(pos[1]-obs[1]+f)
        m=abs(pos[1]-obs[3]-f)
        n=abs(obs[2]-obs[0]+2*f)
        o=abs(obs[3]-obs[1]+2*f)
        for i in range(obs[0]-g,obs[2]+g):
            for j in range(obs[1]-g,obs[3]+g):
                
                if (i in range(int(pos[0])-g,goalpos[0]) and j in range(int(pos[1]),goalpos[1]))or(i in range(int(pos[0])+g,goalpos[0]) and j in range(int(pos[1]),goalpos[1]))or(i in range(int(pos[0]),goalpos[0]) and j in range(int(pos[1])+g,goalpos[1]))or(i in range(int(pos[0]),goalpos[0]) and j in range(int(pos[1])-g,goalpos[1])):
                    

                    if n>=k>=p and o>=m>=l:
                        if l>=p:
                            self.xspeed-=z
                            self.yspeed+=z
                        else:
                            self.xspeed+=z
                            self.yspeed-=z
                            
                    elif n>=p>=k and o>=m>=l:
                        if k>=l:
                            self.xspeed+=z
                            self.yspeed-=z
                        else:
                            self.xspeed-=z
                            self.yspeed+=z
                        

                    elif n>=k>=p and o>l>m:
                        if m>=p:
                            self.xspeed-=z
                            self.yspeed+=z
                        else:
                            self.xspeed+=z
                            self.yspeed-=z
                            
                       

                    if n>=p>=k and o>l>m:
                        if k>=m:
                            self.xspeed-=z
                            self.yspeed+=z
                        else:
                            self.xspeed+=z
                            self.yspeed-=z


                    

                    
        
                else:
                    deta=float(math.atan2(float(goalpos[1]-pos[1]),float(goalpos[0]-pos[0])))
                    a=float(10*math.cos(deta))
                    b=float(10*math.sin(deta))
                    self.xspeed=a
                    self.yspeed=b
        
newrobot=[]        
for goalpos,rpos in zip(goallist,robotlist):
    newrobot.append(Robot(rpos,goalpos,full_obstacle_list))
def move2():
    while True:
        for robot,goalpos in zip(newrobot,goallist):
                
            robot.move(goalpos)
            root.update()
            time.sleep(0.01)




button1= Button(leftFrame, text="move",fg="red",command=move2)
button1.pack(side=LEFT)



    


root.mainloop()
