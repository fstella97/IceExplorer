from time import sleep
import sys
import numpy as np
import math
import pandas as pd



# Import from parent directory
from dynamixel_controller import dynamixel
ID=[1,2,3,4,5,6]
servo = dynamixel(ID, descriptive_device_name="XL430 test motor", 
                    series_name=["xl","xm", "xl","xl","xl", "xl"], baudrate=1000000, port_name="COM5")


servo.begin_communication()

servo.set_operating_mode("extended position", ID = "all")
initial_positions=(servo.read_position(ID = "all"))
print(initial_positions)

wire_thickness = 0.6;   "in [mm]"
# pulley_radius=5+2*wire_thickness; "in [mm]"
pulley_radius=5;

df = pd.read_excel('./Guided_positions.xlsx') # can also index sheet by name or fetch all sheets

desired_position_lengths = np.array(df.values.tolist())
sys.path.append('../')

desired_position_rad=desired_position_lengths/pulley_radius;
desired_position_motor=desired_position_rad*(4096/(2*math.pi))
for j in range(len(desired_position_motor)):
    for i in range(len(ID)):
      servo.write_position(desired_position_motor[j][i]+ initial_positions[i], ID=i+1)
    sleep(10)

servo.end_communication()