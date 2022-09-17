import mysql.connector
import tkinter as tk
from tkinter import messagebox
import faceRec


def faculty(screen,name):
    
    screen = tk.Tk()
    screen.configure(background='floral white')
    screen.geometry("400x500")
    screen.title("FRAT User")
    year = tk.StringVar(screen)
    year.set("First")
    course = tk.StringVar(screen)
    course.set("B.Tech")
    branch = tk.StringVar(screen)
    branch.set("CSE")
    section = tk.StringVar(screen)
    section.set("A")
    tk.Label(text = "Welcome to FRAS", bg = "peach puff", width = "300", height = "2", font = ("Times", 16), fg = "SeaGreen3").pack()
    
    tk.Label(text = "Lecturer : "+str(name), bg = "floral white", width = "300", height = "2", font = ("Times", 12,"bold"), fg = "green").pack()

    tk.Label(text = "Course", bg = 'floral white', font = ("Times", 10), fg = 'hot pink').pack()
    m = tk.OptionMenu(screen, course, "B.Tech", "BBA", "BCA", "MBA", "Diploma")
    m.configure(bg = 'SeaGreen1')
    m.pack()
    tk.Label(text = "", bg = 'floral white').pack()
    tk.Label(text = "Branch", bg = 'floral white', font = ("Times", 10), fg = 'hot pink').pack()
    a = tk.OptionMenu(screen, branch, "CSE", "ME", "EC", "EN","CE")
    a.configure(bg = 'SeaGreen1')
    a.pack()
    tk.Label(text = "", bg = 'floral white').pack()
    tk.Label(text = "Year", bg = 'floral white', font = ("Times", 10), fg = 'hot pink').pack()
    w = tk.OptionMenu(screen, year, "First", "Second", "Third", "Fourth")
    w.configure(bg = 'SeaGreen1')
    w.pack()
    tk.Label(text = "", bg = 'floral white').pack()
    tk.Label(text = "Section", bg = 'floral white', font = ("Times", 10), fg = 'hot pink').pack()
    b = tk.OptionMenu(screen, section, "A", "B", "C", "D", "E")
    b.configure(bg = 'SeaGreen1')
    b.pack()
    tk.Label(text = "", bg = 'floral white').pack()
    tk.Button(master=screen, text = "Start Scanning", fg = "dark violet", bg = "SeaGreen1", height = "2", width = "30", command = lambda : faceRec.face_rec(str(year.get()),str(course.get()),str(branch.get()),str(section.get()),screen.destroy())).pack()
    
    tk.Label(text=" ",bg = 'floral white').pack()
    tk.Button(master=screen, text = "Logout", fg = "red", bg = "SeaGreen1", height = "1", width = "10", command = lambda : mainScreen(screen.destroy())).pack()

    
def loginCheck(user,password,screen):
    if user!="" and password!="":
        mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="fras")
        mycursor= mydb.cursor()
        query="select faculty from access where userid like '"+user+"' and password like '"+password+"';"
        mycursor.execute(query)
        result=mycursor.fetchone()
        if mycursor.rowcount==1:
            faculty(screen.destroy(),result[0])
        else:
            messagebox.showerror("LOGIN","User ID or Password is Incorrect...")
            login(screen)
    else:
        messagebox.showwarning("LOGIN","User ID or Password Required...")
        login(screen)


def login(screen1):

    screen1.destroy()
    screen1=tk.Tk()
    screen1.configure(background='floral white')
    screen1.geometry("400x400")
    screen1.title("FRAT Login")
        
    tk.Label(screen1, text = "FRAS Login Welcomes you", bg = "peach puff", width = "300", height = "2", font = ("Times", 14), fg = "SeaGreen3").pack()
    tk.Label(screen1, text = "", bg = 'floral white').pack()
    tk.Label(screen1, text = "Username * ", bg = 'floral white', fg = 'black', font = ('Times',12)).pack()
        
    user=tk.StringVar()
    password= tk.StringVar()
    tk.Entry(screen1, text = " ", textvariable=user).pack()
    

    tk.Label(screen1, text = "", bg = 'floral white').pack()
    tk.Label(screen1, text = "Password * ", bg = 'floral white', fg = 'black', font = ('Times',12)).pack()
    
    tk.Entry(screen1, text = " ", textvariable=password,show="*").pack()
    
    tk.Button(screen1, text = "Login", fg = "dark violet", bg = "SeaGreen1", height = "2", width = "20", command =lambda : loginCheck(str(user.get()),str(password.get()),screen1)).place(bordermode=tk.OUTSIDE, x=125, y=220)
   

def mainScreen(screen=None):
    screen = tk.Tk()
    screen.configure(background='floral white')
    screen.geometry("400x200")
    screen.title("FRAS Login")
    tk.Label(text = "FRAS Login", bg = "peach puff", width = "300", height = "2", font = ("Times","14","bold"), fg = "SeaGreen3").pack()
    tk.Label(text = "", bg = 'floral white').pack()
    tk.Button(text = "Login", fg = "black", bg = "SeaGreen1",font=("Times","10") ,height = "2", width = "30", command = lambda: login(screen)).place(bordermode=tk.OUTSIDE, x=90, y=100)
    

    screen.mainloop()
    
if __name__=="__main__":
    mainScreen()    
