
import matplotlib.pyplot as plt
import numpy as np

# part 1 : import and display terrace
file = open(r"C:\Users\Schelte\Documents\Tobias\Inhalt\Python\mountain_paths\Colorado_480x480.txt","r")
lines = file.readlines()
floats = []
for i in range(0, len(lines)):
      
        data = lines[i].rstrip('\n').split('   ')
        #zuvor: jede Linie wird einzeln gelesen 
        #und mit .rstrip der Zeilenumbrich am Ende einer jeden Zeile entfernt
        # die erste Zeile als ein langes Element wird an den Leerzeichen in viele kleine Elemente aufgeteilt
        # diese Elemente sind strings
        data.pop(0)
        #zuvor: das erste Element einer jeden Zeile wird gelöscht
        data = [float(i) for i in data]
        #zuvor: data ist die Liste voller Höhenwerte, die als Strings dargestellt werden.
        # Diese werden in floats umgewandelt
        floats.append(data)
               

terrain = np.array(floats)
plt.imshow(terrain, cmap= "gray")
marker_size = 0.01
# check cases
def getValidation(row_num):
    validation = dict()
    if row_num - 1 < 0:
        validation.update({'has_upper': False})
    else:
        validation.update({'has_upper': True})
    if row_num + 1 > 479:
        validation.update({'has_lower': False})
    else:
        validation.update({'has_lower': True})
    
    return validation
# apply greedy algorithm
def getNextRow(terrain, tracker, ind):
    validation = getValidation(tracker)
    current = terrain[tracker][ind]
    mid_next = terrain[tracker][ind + 1]
    diff_1 = abs(current - mid_next)
    diff_min = diff_1
    next_step = 'mid_next'
    if validation.get('has_upper'):
        upper_next = terrain[tracker - 1][ind + 1]
        diff_2 = abs(current - upper_next)
        if diff_2 < diff_min:
            diff_min = diff_2
            next_step = 'upper_next'
        
    if validation.get('has_lower'):
        lower_next = terrain[tracker + 1][ ind + 1]
        diff_3 = abs(current - lower_next)
        if diff_3 < diff_min:
            diff_min = diff_3
            next_step = 'lower_next'
    if next_step == 'mid_next':
        plt.scatter(ind, tracker , c = 'r', s = marker_size)
        return tracker
    elif next_step == 'upper_next':
        plt.scatter( ind, tracker -1 , c = 'r', s = marker_size)
        return tracker - 1
    else:
        plt.scatter( ind, tracker + 1 , c = 'r', s = marker_size)

        return tracker + 1
    
for row_ind in range(450,470):
    plt.scatter(0, row_ind, c='r', s = marker_size)
    tracker = row_ind
    for ind in range(479):
        tracker = getNextRow(terrain, tracker, ind)
        

plt.show
plt.savefig('result.png')
#print(lines[479])

#take first value
#path = []
#data = lines[0].rstrip('\n').split('   ')
#path.append(data[0])
#
#x = lines[0]
#y = lines[1]

#column = []
#for ii in range(0,2):
#    data = lines[ii].rstrip('\n').split('   ')
#    date = data[1]
#    column.append(date)
#print(column)
    
#add second values to list "column"
       
#data[1]
#column.append(data[1])
#
##findsmallest value out of list "column"
#min_val = min(column)
#path.append(min_val)
#
#for y in 480:
#    x = data[y]
#    paths.append(x)
#
#for i in range(0, len(lines)):
#        data = lines[i].rstrip('\n').split('   ')
#        data[0]
#        path.append(data[0])
        
#way_one =[]
#for y in range(len(lines)):
    