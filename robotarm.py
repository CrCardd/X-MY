# version: Python3
from DobotEDU import *


ground  = -50
dist = 120

part_h = 10
part_l  = 20

init_x =  270 
init_y = 70
init_z= 30

parts_l_qtd = 4
for i in range(parts_l_qtd):
  for j in range(parts_l_qtd):
    
    x = init_x +( i * part_l)
    y = init_y + (j * part_l)
    z = init_z
    
    m_lite.set_ptpcmd(ptp_mode=2, x=x, y=y, z=z, r=0)
 
    z -= 70 
    m_lite.set_ptpcmd(ptp_mode=2, x=x, y=y, z=z, r=0)
    m_lite.set_endeffector_suctioncup(enable=True, on=True)
    z+=70
    m_lite.set_ptpcmd(ptp_mode=2, x=x, y=y, z=z, r=0)
    
    y -= (2 * (part_l/2 + (j*part_l))) + dist
    m_lite.set_ptpcmd(ptp_mode=2, x=x, y=y, z=z, r=0)
    
    z -= 70 
    m_lite.set_ptpcmd(ptp_mode=2, x=x, y=y, z=z, r=0)
    m_lite.set_endeffector_suctioncup(enable=True, on=False)
    z+=70
    m_lite.set_ptpcmd(ptp_mode=2, x=x, y=y, z=z, r=0)

    

for i in range(2):
  
  for i in range(parts_l_qtd - 2):
    



























