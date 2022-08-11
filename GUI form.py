from tkinter import *
import requests
root = Tk()
root.title('Wethar Details')
root.geometry('400x200')


def S():
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=3b38f7256941d04dc249f965f535ca29&q='
    city = CityNamev.get()
    url = api_address+city
    print(url)
    json_data = requests.get(url).json()
    print(json_data)
    format_add = json_data['weather'][0]['main']
    format_add2 = json_data['coord']['lon']
    format_add3 = json_data['coord']['lat']
    print(format_add,"and", format_add2, "and", format_add3)

    a.set(format_add)
    b.set(format_add2)
    c.set(format_add3)


Label(root,text='CityName').grid(row=0,column=0)
CityNamev=StringVar()
Entry(root,textvariable=CityNamev).grid(row=0,column=1)

Label(root,text='lon').grid(row=1,column=0)
b=StringVar()
Entry(root,textvariable=b).grid(row=1,column=1)

Label(root,text='lat').grid(row=2,column=0)
c=StringVar()
Entry(root,textvariable=c).grid(row=2,column=1)

Label(root,text='weather').grid(row=3,column=0)
a=StringVar()
Entry(root,textvariable=a).grid(row=3,column=1)

Button(root,text='SUBMIT',command=S).grid(row=0,column=3)

root.mainloop()