from time import sleep
import sys
import math
from tkinter import END
import keyboard 
import numpy as np

sys.path.append('../')

# Import from parent directory
from dynamixel_controller import dynamixel

servo = dynamixel(ID=[1,2,3,4], descriptive_device_name="XM430 test motor",
                    series_name=["xm", "xm", "xm", "xm"], baudrate=1000000, port_name="COM6")

servo.begin_communication()
servo.set_operating_mode("position", ID = "all")


n_steps=3;
while True:  # making a loop
        pos0_1 = servo.read_position(1)
        pos0_2 = servo.read_position(2)
        pos0_3 = servo.read_position(3)
        pos0_4 = servo.read_position(4)


        if keyboard.is_pressed('s'):  
           print('Basic Pose!')
           m1_goal=84/360*4086;
           m2_goal=106/360*4086;
           m3_goal=83/360*4086;
           m4_goal=75/360*4086;
           m1=np.linspace(pos0_1, m1_goal, num=n_steps)
           m2=np.linspace(pos0_2, m2_goal, num=n_steps)
           m3=np.linspace(pos0_3, m3_goal, num=n_steps)
           m4=np.linspace(pos0_4, m4_goal, num=n_steps)
           for i in range(len(m1)):
             servo.write_position(math.floor(m1[i]),ID=1)
             servo.write_position(math.floor(m2[i]),ID=2)
             servo.write_position(math.floor(m3[i]),ID=3)
             servo.write_position(math.floor(m4[i]),ID=4)
             sleep(0.1)

 
           
        ###
        #if keyboard.is_pressed('w'):  
        #   print('All Up!')
        #   servo.write_position(math.floor(72/360*4086),ID=1)
        #   servo.write_position(math.floor(4/360*4086),ID=2)
        #   servo.write_position(math.floor(114/360*4086),ID=3)
        #   servo.write_position(math.floor(75/360*4086),ID=4)   

        #if keyboard.is_pressed('e'):  
        #   print('Left!')
        #   servo.write_position(math.floor(84/360*4086),ID=1)
        #   servo.write_position(math.floor(119/360*4086),ID=2)
        #   servo.write_position(math.floor(53/360*4086),ID=3)
        #   servo.write_position(math.floor(96/360*4086),ID=4)  

        ##if keyboard.is_pressed('q'):  
        #   print('Right!')
        #   servo.write_position(math.floor(84/360*4086),ID=1)
        #   servo.write_position(math.floor(50/360*4086),ID=2)
        #   servo.write_position(math.floor(114/360*4086),ID=3)
        #   servo.write_position(math.floor(61/360*4086),ID=4)

        if keyboard.is_pressed('u'):  
           print('Up!')
           m1_goal=117/360*4086;
           m2_goal=76/360*4086;
           m3_goal=82/360*4086;
           m4_goal=110/360*4086;
           m1=np.linspace(pos0_1, m1_goal, num=n_steps)
           m2=np.linspace(pos0_2, m2_goal, num=n_steps)
           m3=np.linspace(pos0_3, m3_goal, num=n_steps)
           m4xs=np.linspace(pos0_4, m4_goal, num=n_steps)
           for i in range(len(m1)):
             servo.write_position(math.floor(m1[i]),ID=1)
             servo.write_position(math.floor(m2[i]),ID=2)
             servo.write_position(math.floor(m3[i]),ID=3)
             servo.write_position(math.floor(m4[i]),ID=4)
             sleep(0.02)










        if keyboard.is_pressed('p'):  
           print('sitting!')
           m1_goal=162/360*4086;
           m2_goal=149/360*4086;
           m3_goal=31/360*4086;
           m4_goal=336/360*4086;
           m1=np.linspace(pos0_1, m1_goal, num=n_steps)
           m2=np.linspace(pos0_2, m2_goal, num=n_steps)
           m3=np.linspace(pos0_3, m3_goal, num=n_steps)
           m4xs=np.linspace(pos0_4, m4_goal, num=n_steps)
           for i in range(len(m1)):
             servo.write_position(math.floor(m1[i]),ID=1)
             servo.write_position(math.floor(m2[i]),ID=2)
             servo.write_position(math.floor(m3[i]),ID=3)
             servo.write_position(math.floor(m4[i]),ID=4)
             sleep(0.02)
        if keyboard.is_pressed('x'):  
           print('down right!')
           m1_goal=50/360*4086;
           m2_goal=107/360*4086;
           m3_goal=127/360*4086;
           m4_goal=61/360*4086;
           m1=np.linspace(pos0_1, m1_goal, num=n_steps)
           m2=np.linspace(pos0_2, m2_goal, num=n_steps)
           m3=np.linspace(pos0_3, m3_goal, num=n_steps)
           m4xs=np.linspace(pos0_4, m4_goal, num=n_steps)
           for i in range(len(m1)):
             servo.write_position(math.floor(m1[i]),ID=1)
             servo.write_position(math.floor(m2[i]),ID=2)
             servo.write_position(math.floor(m3[i]),ID=3)
             servo.write_position(math.floor(m4[i]),ID=4)
             sleep(0.02)
        ##
        #if keyboard.is_pressed('c'):  
         #  print('down back!')
           # servo.write_position(math.floor(59/360*4086),ID=1)
           #servo.write_position(math.floor(170/360*4086),ID=2)
           #servo.write_position(math.floor(115/360*4086),ID=3)
           #servo.write_position(math.floor(18/360*4086),ID=4)

        if keyboard.is_pressed('z'):  
           print('down back!')
           m1_goal=47/360*4086;
           m2_goal=189/360*4086;
           m3_goal=110/360*4086;
           m4_goal=3/360*4086;
           m1=np.linspace(pos0_1, m1_goal, num=n_steps)
           m2=np.linspace(pos0_2, m2_goal, num=n_steps)
           m3=np.linspace(pos0_3, m3_goal, num=n_steps)
           m4=np.linspace(pos0_4, m4_goal, num=n_steps)
           for i in range(len(m1)):
             servo.write_position(math.floor(m1[i]),ID=1)
             servo.write_position(math.floor(m2[i]),ID=2)
             servo.write_position(math.floor(m3[i]),ID=3)
             servo.write_position(math.floor(m4[i]),ID=4)
             sleep(0.02)

        if keyboard.is_pressed('c'):  
           print('down front!')
           m1_goal=21/360*4086;
           m2_goal=86/360*4086;
           m3_goal=169/360*4086;
           m4_goal=71/360*4086;
           m1=np.linspace(pos0_1, m1_goal, num=n_steps)
           m2=np.linspace(pos0_2, m2_goal, num=n_steps)
           m3=np.linspace(pos0_3, m3_goal, num=n_steps)
           m4=np.linspace(pos0_4, m4_goal, num=n_steps)
           for i in range(len(m1)):
             servo.write_position(math.floor(m1[i]),ID=1)
             servo.write_position(math.floor(m2[i]),ID=2)
             servo.write_position(math.floor(m3[i]),ID=3)
             servo.write_position(math.floor(m4[i]),ID=4)
             sleep(0.02)
       
           

        if keyboard.is_pressed('t'):
            break
           
  
            