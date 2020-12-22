from tkinter import *
import datetime
import calendar
root = Tk()
root.title('Calendar')
days = []
now = datetime.datetime.now()
month = now.month
year = now.year

def prev():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    fill()

def next():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    fill()
    
def fill():
    info_label['text'] = calendar.month_name[month] + ', ' + str(year)
    month_days = calendar.monthrange(year, month)[1]
    
    if month == 1:
        prev_month_days = calendar.monthrange(year-1, 12)[1]
    else:
        prev_month_days = calendar.monthrange(year, month - 1)[1]
    week_day = calendar.monthrange(year, month)[0]
    
    for n in range(month_days):
        days[n + week_day]['text'] = n+1
        days[n + week_day]['fg'] = 'white'
        
        if year == now.year and month == now.month and n == now.day:
            days[n + week_day]['background'] = 'red'
        else:
            days[n + week_day]['background'] = 'green'
            
    for n in range(week_day):
        days[week_day - n - 1]['text'] = prev_month_days - n
        days[week_day - n - 1]['fg'] = 'gray'
        
    for n in range(6*7 - month_days - week_day):
        days[week_day + month_days + n]['text'] = n+1
        days[week_day + month_days + n]['fg'] = 'gray'
        
prew_button = Button(root, text='<', command=prev)
prew_button.grid(row=0, column=0, sticky='nsew')

next_button = Button(root, text='>', command=next)
next_button.grid(row=0, column=6, sticky='nsew')

info_label = Label(root, text='0', width=1, height=1, 
            font=('georgia', 16, 'bold'), fg='blue')
info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

for n in range(7):
    lbl = Label(root, text=calendar.day_abbr[n], width=1, height=1, 
                font=('Georgia', 10, 'normal'), fg='black')
    lbl.grid(row=1, column=n, sticky='nsew')
    
for row in range(6):
    for col in range(7):
        lbl = Label(root, text='0', width=4, height=2, 
                    font=('Georgia', 16, 'bold'))
        lbl.grid(row=row+2, column=col, sticky='nsew')
        days.append(lbl)
fill()
root.mainloop()