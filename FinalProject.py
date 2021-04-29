import PySimpleGUI as et
import pandas
import matplotlib.pyplot as plt

#this chart will display the monthly income and expenditures and amount saved each month towards couch.
file = open('theBudget.csv', 'r')
for i in file:
    x = i.split(",")
    print (x)
    for value in x:
        if value 


'''labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
MoneyIn = [6764, 6075, 12820, 3805, 0]
MoneyOut = [5464, 2540, 5970, 893, 0]


width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots()

ax.bar(labels, MoneyIn, width, label='Money In')
ax.bar(labels, MoneyOut, width, bottom=MoneyIn,
       label='Money Out')

ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.legend()

plt.show()


layout = [  [et.Text("What's your name?")],     # Part 2 - The Layout
            [et.Input()],
            [et.Button('Ok')] ]
window = et.Window('Expense Tracker', layout)
event, values = window.read()
print('Hello', values[0], "! Thanks for trying PySimpleGUI")







window.close()'''
exit()

