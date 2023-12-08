from time import sleep
import sys
import math
from tkinter import END
import keyboard 

sys.path.append('../')

# Import from parent directory
from dynamixel_controller import dynamixel

servo = dynamixel(ID=[1,2,3,4], descriptive_device_name="XM430 test motor",
                    series_name=["xm", "xm", "xm", "xm"], baudrate=1000000, port_name="COM6")
#servo.begin_communication()
#servo.set_operating_mode("extended position", ID = "all")

servo.begin_communication()
servo.set_operating_mode("position", ID = "all")



while True:  # making a loop
        pos0_1 = servo.read_position(1)
        pos0_2 = servo.read_position(2)
        pos0_3 = servo.read_position(3)
        pos0_4 = servo.read_position(4)

        m1=np.linspace(pos0_1, m1_goal, num=10)
        m2=np.linspace(pos0_2, m2_goal, num=10)
        m3=np.linspace(pos0_3, m3_goal, num=10)
        m4=np.linspace(pos0_4, m4_goal, num=10)

        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
           print('Standing!')


           
           
        if keyboard.is_pressed('w'):  # if key 'q' is pressed 
           print('Jumping!')
           servo.write_position(math.floor(7/360*4086),ID=2)
           servo.write_position(math.floor(130/360*4086),ID=4)
           #sleep(1)

        if keyboard.is_pressed('e'):
            break
           
  
            