"""Case-study №6 Trains and Metropolitan
Developers:
Ermokhin S.A.(50%), Nikitina N.V.(50%), Popov I.I.(50%)"""

from tkinter import *
from math import *

from oop import *
from local import *

print(HELLO)

root = Tk()
root.title('Trains and Metropolitan')

size = 800
canvas = Canvas(root, width=size, height=size, bg='white')
canvas.pack()

#----------------------------------------------------------------------

def start():
    """Start function"""
    
    global wagon_objects_1, wagons, radius_1, radius_2
    
    for key in wagon_objects_1:
        if wagons[key][1] == 0:
            if wagon_objects_1[key].check(wagons[key][0]):
                wagon_objects_1[key].move(radius_1, wagons[key][0])
                wagons[key][0] += int(wagons[key][2]/194)+1
        else:
            if wagon_objects_1[key].check(wagons[key][0]):
                wagon_objects_1[key].move(radius_2, wagons[key][0])
                wagons[key][0] -= int(wagons[key][2]/194)+1
                
    root.after(100, start)


def stop():
    """Stop function"""
    
    root.destroy()

#----------------------------------------------------------------------

wagons = {}
wagon_objects_1 = {}
center = size/2
len_oval = 1940
radius_1 = 1940/(2*pi)
radius_2 = (1940/(2*pi)) + 10
radius_3 = (1940/(2*pi)) + 5
radius = 2
wagons = {}
wagon_objects_1 = {}
stations = (270, 306, 342, 6, 42, 66, 78, 114, 150, 174, 210, 234)

#----------------------------------------------------------------------

line1 = canvas.create_oval(center-radius_1,center-radius_1,
                           center+radius_1,center+radius_1, outline='red', width=3)

line2 = canvas.create_oval(center-radius_2,center-radius_2,
                           center+radius_2,center+radius_2, outline='red', width=3)

for i in stations:
    station = Station(canvas,(radius_3*cos(radians(i)), radius_3*sin(radians(i))),
                      center).build_oval()

#----------------------------------------------------------------------

file = open('metro.txt','r')
text = file.readlines()
file.close()


stations_for_file = {'Проспект_Мира':270, 'Комсомольская':306, 'Курская':342,
                     'Таганская':6, 'Павелецкая':42, 'Добрынинская':66,
                     'Октябрьская':78, 'Парк_культуры':114, 'Киевская':150,
                     'Краснопресненская':174, 'Белорусская':210,
                     'Новослободская':234}

for j in range(len(text)):
    text[j] = text[j].split(' ')

    text[j][0] = int(text[j][0])
    text[j][2] = int(text[j][2])
    text[j][3] = int(text[j][3])


for item in text:
    wagons[item[0]] = [stations_for_file[item[1]], item[2], item[3]]
    
    if item[2] == 0:
        center_1 = radius_1*sin(stations_for_file[item[1]]*pi/180)
        center_2 = radius_1*cos(stations_for_file[item[1]]*pi/180)
    else:
        center_1 = radius_2*sin(stations_for_file[item[1]]*pi/180)
        center_2 = radius_2*cos(stations_for_file[item[1]]*pi/180)

    coords = [center_1-radius+center,
              center_2-radius+center,
              center_1+radius+center,
              center_2+radius+center]
    
    tag = canvas.create_oval(coords, fill='yellow')
    wagon_objects_1[item[0]] = Wagon(canvas, tag, center_1, center_2, center)
    
#----------------------------------------------------------------------

Button(root, text='START', command=start).pack()
Button(root, text='STOP', command=stop).pack()

root.mainloop()

print(BYE)
