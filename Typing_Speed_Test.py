# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:04:23 2020

@author: saksham jain
"""
#Imports
import tkinter as tk
import random
from tkinter import ttk
import ttkthemes as tt
import time as tm
import threading
import keyboard
import math
import mysql.connector as mc
import requests



#Variables
elapsedTime=0
elapsed_time_in_minute=0
total_words=0
wrong_words=0
wpm=0
accuracy=0
label_sentence=""
entry=''
entry2=""
btn_start=""
btn_reset=""
btn_rec=""
btn_close=''
lbl_total_words=""
lbl_accuracy=""
lbl_wpm=""
lbl_elapsedTime=""
lbl_wrong_words=""
lbl_remaining_words=""
lbl_elapsedTimer=""
window=""
x=0
y=0
name=""
flag=''
result=[]


#Connecting to MySQl


cs=mc.connect(host='localhost',user='root',password='root')
mycursor=cs.cursor()
mycursor.execute('use cs')



def create_table():
    sql="create table if not exists records(Name varchar(30), WPM int, Accuracy int, Date date)"
    mycursor.execute(sql)
    cs.commit()

def insertrec():
    sql='insert into records values("{}",{},{},curdate())'.format(name,x,y)
    mycursor.execute(sql)
    cs.commit()

def showrec():
    global result
    global btn_rec

    btn_rec.config(state='disabled')

    sql='select * from records where name="{}"'.format(name)
    mycursor.execute(sql)
    result=mycursor.fetchall()






#Functions
def start_timer():
    global elapsedTime
    global label_sentence
    global entry
    global btn_start
    global btn_reset
    global lbl_total_words
    global lbl_wpm
    global lbl_accuracy
    global lbl_elapsedTime
    global lbl_wrong_words
    global lbl_remaining_words
    global lbl_elapsedTimer
    global window


    f=open("sentences.txt")
    list_of_sentences=f.readlines()
    sentence=random.choice(list_of_sentences)
    f.close()

    label_sentence['text']=sentence

    entry.focus()
    entry.config(state='normal')
    btn_start.config(state='disabled')
    btn_rec.config(state='disabled')
    while(True):
        if keyboard.is_pressed('Enter'):
            break
        elapsedTime+=1
        lbl_elapsedTimer['text']=elapsedTime
        tm.sleep(1)
        window.update()
    count()
    entry.config(state='disabled')
    btn_reset.config(state='normal')
    btn_rec.config(state='normal')



def count():
    global wrong_words
    global elpasedTime
    global elpased_time_in_minute
    global label_sentence
    global entry
    global btn_start
    global btn_reset
    global lbl_total_words
    global lbl_wpm
    global lbl_accuracy
    global lbl_elapsedTime
    global lbl_wrong_words
    global lbl_remaining_words
    global lbl_elapsedTimer
    global x
    global y
    global name



    words=label_sentence['text'].split()


    entered_sentence=entry.get(1.0,'end-1c').split()
    total_words=len(entered_sentence)
    lbl_total_words['text']=total_words
    if total_words==0:
        lbl_accuracy['text']=0
        lbl_wpm['text']=0
        lbl_wrong_words['text']=0
        remaining_words=len(words)
        lbl_remaining_words['text']=remaining_words

    else:
        for pair in list(zip(words,entered_sentence)):
            if pair[0]!=pair[1]:
                wrong_words+=1
        lbl_wrong_words['text']=wrong_words


        remaining_words=len(words)-total_words
        lbl_remaining_words['text']=remaining_words+wrong_words





        elapsed_time_in_minute=elapsedTime/60
        wpm=((total_words-wrong_words)/elapsed_time_in_minute)
        lbl_wpm['text']=math.fabs(round(wpm,2))
        x=math.fabs(round(wpm,2))


        accuracy=((total_words-wrong_words)/total_words)*100
        lbl_accuracy['text']=math.fabs(round(accuracy,2))
        y=math.fabs(round(accuracy,2))


    if keyboard.is_pressed('Enter'):
        btn_reset.config(state="normal")
        btn_rec.config(state='normal')
        create_table()
        insertrec()



def start():
    thr1=threading.Thread(target=start_timer)
    thr1.start()
    thr2=threading.Thread(target=count)
    thr2.start()



def reset():
    global elapsedTime
    global wrong_words
    global label_sentence
    global entry
    global btn_start
    global btn_reset
    global lbl_total_words
    global lbl_wpm
    global lbl_accuracy
    global lbl_elapsedTime
    global lbl_wrong_words
    global lbl_remaining_words
    global lbl_elapsedTimer
    global window
    global name
    global flag


    '''btn_reset.config(state='disabled')
    btn_start.config(state='normal')

    entry.config(state='normal')
    entry.delete(1.0,tk.END)
    entry.config(state='disabled')'''

    elapsedTime=0
    wrong_words=0
    name=''
    flag=True

    '''lbl_elapsedTimer['text']=0
    lbl_wpm['text']=0
    lbl_accuracy['text']=0
    lbl_total_words['text']=0
    lbl_wrong_words['text']=0
    sentence=random.choice(list_of_sentences)
    label_sentence['text']=sentence
    lbl_remaining_words['text']=0'''

    window.destroy()
    name_window()



def getname():
    global name
    name=entry2.get(1.0,"end-1c")



def btn_config():
    global btn_rec

    btn_rec.config(state='normal')



def asciiart():
    text=('Hello '+name)
    r=requests.get(f'http://artii.herokuapp.com/make?text={text}')
    print(r.text)




#GUI
def rec_window():
    global btn_close

    window3=tt.ThemedTk()
    window3.get_themes()
    window3.set_theme('radiance')
    window3.title("Previous Records")
    window3.geometry()
    window3.resizable(0,0)

    main_frame3=tk.Frame(window3,bg="white",bd=4)

    title_frame3=tk.Frame(main_frame3,bg="black",relief="flat")
    label_title3=tk.Label(title_frame3,text="Previous Records",font=("Helvetica",18,"bold"),height=2,bg="white",fg="black",bd=2,width=55,relief="groove")
    label_title3.grid(row=0,column=0,pady=5, padx=5)
    title_frame3.grid(row=0,column=0)

    table_frame=tk.Frame(main_frame3,bg="white",relief="flat")
    table=tk.Entry(table_frame,width=10,fg='Red',font=('Arial',16,"bold"))
    table.grid(row=0,column=0,pady=15)
    table.insert(tk.END,"Name")
    table.config(state='disabled')
    table=tk.Entry(table_frame,width=10,fg='Red',font=('Arial',16,"bold"))
    table.grid(row=0,column=1,pady=15)
    table.insert(tk.END,"WPM")
    table.config(state='disabled')
    table=tk.Entry(table_frame,width=11,fg='Red',font=('Arial',16,"bold"))
    table.grid(row=0,column=2,pady=15)
    table.insert(tk.END,"Accuracy(%)")
    table.config(state='disabled')
    table=tk.Entry(table_frame,width=10,fg='Red',font=('Arial',16,"bold"))
    table.grid(row=0,column=3,pady=15)
    table.insert(tk.END,"Date")
    table.config(state='disabled')
    for i in range(len(result)):
        for j in range(4):
            table=tk.Entry(table_frame,fg='blue',font=('Arial',16))
            table.grid(row=i+1,column=j,pady=5,padx=5)
            table.insert(tk.END,result[i][j])
            table.config(state='disabled')
    table_frame.grid(row=1,column=0)

    btn_close=ttk.Button(main_frame3,text='Close',command=lambda:[window3.destroy(),btn_config()])
    btn_close.grid(row=len(result)+3,column=0,padx=10,pady=20)

    main_frame3.grid()
    window3.mainloop()



def main_window():
    global label_sentence
    global entry
    global btn_start
    global btn_reset
    global btn_rec
    global lbl_total_words
    global lbl_wpm
    global lbl_accuracy
    global lbl_elapsedTime
    global lbl_wrong_words
    global lbl_remaining_words
    global lbl_elapsedTimer
    global window


    window=tt.ThemedTk()
    window.get_themes()
    window.set_theme('radiance')
    window.title("Typing speed test")
    window.geometry()
    window.resizable(0,0)



    #Main frame
    main_frame=tk.Frame(window,bg="white",bd=4)


    #Title frame
    title_frame=tk.Frame(main_frame,bg="orange",relief="flat")
    label_title=tk.Label(title_frame,text="Test Your Speed",font=("Helvetica",14,"bold"),height=3,bg="yellow",fg="black",bd=10,width=80,relief="groove")
    label_title.grid(row=0,column=0,pady=5, padx=5)
    title_frame.grid(row=0,column=0)


        #Test frame
    test_frame=tk.Frame(main_frame,bg="white",relief="flat")


    #sentence
    label_sentence=tk.Label(test_frame,text="Sentence-(Will be shown after pressing start)",wraplength=750,relief="ridge",height=4,font=("italic",15))
    label_sentence.grid(row=1,column=0,pady=20)

    test_frame.grid(row=1,column=0)


    #input box
    entry=tk.Text(test_frame,bg="black",fg="white",height=20,width=80,bd=10)
    entry.grid(row=2,column=0,pady=10)
    entry.config(state="disabled")


    #output frame
    output_frame=tk.Frame(main_frame,bg="white",relief="groove")

    frame_labels=tk.Frame(output_frame,bg="white")

    # elapsed time

    lbl_elapsedTime = tk.Label(frame_labels,text='Elapsed Time(in sec)',font='Tahoma 10 bold',fg='red',bg='white')
    lbl_elapsedTimer = tk.Label(frame_labels,text='0',font='Tahoma 10 bold',fg='black',bg='white')

    lbl_elapsedTime.grid(row=0,column=0,padx=10,pady=10)
    lbl_elapsedTimer.grid(row=0,column=1,padx=10,pady=10)

    # wpm

    lbl_wpm_title = tk.Label(frame_labels,text='WPM',font='Tahoma 10 bold',fg='red',bg='white')
    lbl_wpm = tk.Label(frame_labels,text='0',font='Tahoma 10 bold',fg='black',bg='white')

    lbl_wpm_title.grid(row=0,column=4,padx=10,pady=10)
    lbl_wpm.grid(row=0,column=5,padx=10,pady=10)

    # accuracy

    lbl_accuracy_title = tk.Label(frame_labels,text='Accuracy(%)',font='Tahoma 10 bold',fg='red',bg='white')
    lbl_accuracy = tk.Label(frame_labels,text='0',font='Tahoma 10 bold',fg='black',bg='white')

    lbl_accuracy_title.grid(row=0,column=6,padx=10,pady=10)
    lbl_accuracy.grid(row=0,column=7,padx=10,pady=10)

    # total words

    lbl_total_words_title = tk.Label(frame_labels,text='Total Words',font='Tahoma 10 bold',fg='red',bg='white')
    lbl_total_words = tk.Label(frame_labels,text='0',font='Tahoma 10 bold',fg='black',bg='white')

    lbl_total_words_title.grid(row=0,column=8,padx=10,pady=10)
    lbl_total_words.grid(row=0,column=9,padx=10,pady=10)

    # wrong words

    lbl_wrong_words_title = tk.Label(frame_labels,text='Wrong Words',font='Tahoma 10 bold',fg='red',bg='white')
    lbl_wrong_words = tk.Label(frame_labels,text='0',font='Tahoma 10 bold',fg='black',bg='white')

    lbl_wrong_words_title.grid(row=0,column=10,padx=10,pady=10)
    lbl_wrong_words.grid(row=0,column=11,padx=10,pady=10)


    #remaining words
    lbl_remaining_words_title = tk.Label(frame_labels,text='Remaining Words',font='Tahoma 10 bold',fg='red',bg='white')
    lbl_remaining_words = tk.Label(frame_labels,text='0',font='Tahoma 10 bold',fg='black',bg='white')

    lbl_remaining_words_title.grid(row=0,column=12,padx=10,pady=10)
    lbl_remaining_words.grid(row=0,column=13,padx=10,pady=10)
    frame_labels.grid(row=0)


    #Control frame
    control_frame=tk.Frame(output_frame,bg="white")

    # Start
    btn_start=ttk.Button(control_frame,text='Start',command=start)
    btn_start.grid(row=0,column=0,padx=10,pady=5)

    # Reset
    btn_reset=ttk.Button(control_frame,text='Reset',command=reset)
    btn_reset.grid(row=0,column=1,padx=10,pady=5)
    btn_reset.config(state='disabled')


    btn_rec=ttk.Button(control_frame,text='Show Record',command=lambda:[showrec(),rec_window()])
    btn_rec.grid(row=0,column=2,padx=10,pady=5)

    control_frame.grid(row=1)

    output_frame.grid(row=2,column=0,pady=5)


    main_frame.grid()

    window.mainloop()



def name_window():
    global entry2
    global name
    global flag

    window2=tt.ThemedTk()
    window2.get_themes()
    window2.set_theme('radiance')
    window2.title("Enter your Name")
    window2.geometry()
    window2.resizable(0,0)

    main_frame2=tk.Frame(window2,bg="white",bd=4)

    title_frame2=tk.Frame(main_frame2,bg="black",relief="flat")
    label_title2=tk.Label(title_frame2,text="Enter Your Name",font=("Helvetica",10,"bold"),height=2,bg="white",fg="black",bd=5,width=30,relief="groove")
    label_title2.grid(row=0,column=0,pady=5, padx=5)
    title_frame2.grid(row=0,column=0)

    btn_ok=ttk.Button(main_frame2,text='Continue',command=lambda:[getname(),window2.destroy(),asciiart(),main_window()])
    btn_ok.grid(row=2,column=0,padx=10)

    entry2=tk.Text(main_frame2,bg="white",fg="black",height=10,width=20,bd=3)
    entry2.grid(row=1,column=0,pady=5)

    entry2.focus()
    flag=False


    main_frame2.grid()
    window2.mainloop()
name_window()
