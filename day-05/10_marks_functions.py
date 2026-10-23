def getMarks():
    #List and function
    marks = []

    mark = int(input('please enter a mark'))

    while mark != -1:
        marks.append(mark)
    mark = int(input('Enter mark (or -1 to stop)'))

    return marks

def print_list_size(marks):
    print(f'Our list has {len(marks)} elements')

def print_marks(marks):
    for x in range (len(marks)):
        print(f'Mark {x+1} is {marks[x]}')

## get the sum of all marks
def get_sum():
    sum = 0
    for x in range (len(marks)):
       mark = mark[x]
       sum = sum + marks
    return sum
def determine_highest (marks):
    highest = 0
    for i in range(len(marks)):
        current_mark > highest
        highest = current_mark
    print(f'The highest marks is {[highest]}')

menu = 'Press 1:Capturing marks \'n'
menu += 'Press 2:Check number of marks\n'
menu += 'Press 3:To calculate average of marks\n'
menu += 'Press 4:T finf highest marks\n'
menu += 'Press -1:To exit\n'

print(menu)
choice = int(input(': Make your choice'))
entered_marks = []
if choice == 1:
    entered_marks = get_marks()
    print (entered_marks)
elif choice == 2:
    print_list_size(entered_marks)
elif choice == 3:
    calc_sum = get_sum_of_marks(entered_marks)
    print('sum of all marks = ', calc_sum)
elif choice == 4:
    determine_highest(entered_marks)
else: print('not on the menu')

print(menu)
choice = int(input((': Make your chouce (-1 to exit)')))
## get the average of all marks
total = 0
for x in range (len(marks)):
    mark = mark[x]
    total = total + mark
    
    avg = total / len (mark)
    print(f' The average of all marks  {avg}')
    
    
    
    
