marks = []
i = 0
mark = int(input('please enter a mark'))

while mark != -1:
    marks.append(mark)

    mark = int(input('Enter mark (or -1 to stop)'))
print(f'Our list has {len(marks)} elements')

## get the sum of all marks
sum = 0
for x in range (len(marks)):
   mark = mark[x]
   sum = sum + marks
   print('The sum of all marks = {sum}')
   
   ## get the average of all marks
   total = 0
for x in range (len(marks)):
    mark = mark[x]
    total = total + mark
    
    avg = total / len (mark)
    print(f' The average of all marks  {avg}')

                    
          

