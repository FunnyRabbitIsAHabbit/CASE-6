"""Case-study №6 Trains and Metropolitan
Developers:
Ermokhin S.A.(50%), Nikitina N.V.(50%), Popov I.I.(50%)"""

from math import *
from random import choice


class Station:
    """Figure class"""

    def __init__(self, canvas, center=(0, 0),
                 far_from_start=0, radius=6):
        """Class constructor"""

        self.canvas = canvas
        self.center = center
        self.coords = [center[0]-radius+far_from_start,
                       center[1]-radius+far_from_start,
                       center[0]+radius+far_from_start,
                       center[1]+radius+far_from_start]
        self.radius = radius

    def build_oval(self):
        """Build oval function"""

        self.canvas.create_oval(self.coords, width=self.radius,
                                fill='red')


class Wagon:
    """Wagon class"""
    
    def __init__(self, canvas, tag, center_1, center_2,
                 far_from_start=0, radius=2):
        """Class constructor"""

        self.canvas = canvas
        self.tag = tag
        self.center_1 = center_1
        self.center_2 = center_2
        self.far_from_start = far_from_start
        self.radius = radius
        self.coords = [self.center_1-radius+far_from_start,
                       -self.center_2-radius+far_from_start,
                       self.center_1+radius+far_from_start,
                       -self.center_2+radius+far_from_start]
        self.count = 0
        self.pick = 0
        
    def move(self, radius_1, angle):
        """Move function"""
        
        new_coords = [radius_1*cos(radians(180-angle))-self.radius+self.far_from_start,
                      radius_1*sin(radians(180-angle))-self.radius+self.far_from_start,
                      radius_1*cos(radians(180-angle))+self.radius+self.far_from_start,
                      radius_1*sin(radians(180-angle))+self.radius+self.far_from_start]

        self.canvas.coords(self.tag, new_coords)


    def check(self, angle):
        """Check function"""
        
        time = [i/30 for i in range(10,130,10)]
        pick = choice(time)
        
        if self.pick == 0:
            self.pick = pick
        
        if 180-angle in (270, 306, 342, 6, 42, 66, 78, 114, 150, 174, 210, 234):
            if self.pick != 10/30 and self.count > self.pick:
                self.count = 0
                self.pick = 0
                
                return 1
            else:
                self.count += 1/30
                
                return 0
        else:
            self.count = 0
            self.pick = 0
            
            return 1


        

            







