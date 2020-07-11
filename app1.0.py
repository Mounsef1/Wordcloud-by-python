from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter as tk
import tkinter.scrolledtext as st
import os
import random
from tagcloud import one_wordcloud
import matplotlib.pyplot as plt
from PIL import Image
import copy

img_path = dict()

root = Tk()
root.geometry('1200x650')
root.resizable(width=FALSE, height=FALSE)
root.title('TAG CLOUD')
color1 = 'SkyBlue1'
color2 = 'SkyBlue2'
color3 = 'SkyBlue3'
color4 = 'SkyBlue4'
color5 = 'SteelBlue4'
color6 = 'SteelBlue3'
color7 = 'SteelBlue2'
color8 = 'steelBlue1'
c = 0

browse = 0

d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()


def color_func(word, font_size, position, orientation, random_state=None,
               **kwargs):
    return "hsl(" + str(color_words) + ", %d%%, 50%%)" % random.randint(60, 100)


def generer():
    global one, color_words, one2

    if a.get() == 1:
        one.contour_width = 1

    if b.get() == 1:
        one.color = "S"
    elif colors_list.get() != "Random":
        if colors_list.get() == "Red":
            color_words = 0
        elif colors_list.get() == "Green":
            color_words = 114
        elif colors_list.get() == "Blue":
            color_words = 241
        one.color = color_func

    one.bgc = colors_list2.get()

    if v.get() == 2:
        global img_select1, img_select2
        one2 = copy.copy(one)
        one.image = Image.open(os.path.join(d, img_select1));
        one2.image = Image.open(os.path.join(d, img_select2));
    else:
        one.image = Image.open(os.path.join(d, s.get()));

    if v.get() == 1:
        one2.image = one.image
        one2.contour_width = one.contour_width
        one2.color = one.color
        one2.bgc = one.bgc

    print("process")

    k = one.generate()
    if v.get() != 0: k2 = one2.generate()

    print("done")
    if v.get() == 0:
        plt.figure(figsize=(20, 20))
        plt.imshow(k, interpolation="bilinear")
        plt.axis('off')
        plt.show()
    elif v.get() != 0:
        ax1 = plt.subplot(121)
        ax1.imshow(k, interpolation="bilinear")
        ax1.axis('off')
        ax2 = plt.subplot(122)
        ax2.imshow(k2, interpolation="bilinear")
        ax2.axis('off')
        plt.show()


def reset_text(wc, zone):
    f = wc.get_frequencies()
    zone.config(state=NORMAL)
    zone.delete('1.0', END)
    zone.insert(tk.INSERT, str(f).replace(',', '\n'));
    zone.config(state=DISABLED)


def disable1():
    entry1.config(state='disabled')


def lecture_stopwords():
    global one, one2, text_area, text_area_2

    one.add_stopwords(entry2.get())
    reset_text(one, text_area)
    if v.get() == 1:
        one2.add_stopwords(entry2.get())
        reset_text(one2, text_area_2)
    entry2.delete(0, END)


def browse1():
    global one, browse
    root.filename = filedialog.askopenfilename()
    link = str(root.filename)
    label_fucntion1 = Label(labelframe2, text=link, anchor='w', width=35, bg=color6)
    label_fucntion1.place(x=5, y=40)
    one = one_wordcloud(open(link, encoding="utf-8").read());

    reset_text(one, text_area)

    browse += 1

    if v.get() != 1 or browse == 2: generatebutton.config(state='normal')


def select1():
    global img_select1
    img_select1 = s.get()


def submit1():
    global browse, text_area_2

    def browse2():
        global one2, browse
        root.filename = filedialog.askopenfilename()
        link = str(root.filename)
        label_fucntion2 = Label(labelframe3, text=link, anchor='w', width=35, bg=color6)
        label_fucntion2.place(x=5, y=40)
        one2 = one_wordcloud(open(link, encoding="utf-8").read());
        reset_text(one2, text_area_2)

        browse += 1
        if browse == 2: generatebutton.config(state='normal')

    def select2():
        global img_select2
        img_select2 = s.get()

    c = v.get()
    button1.config(state='disabled')
    button2.config(state='disabled')
    button3.config(state='disabled')

    if c == 1:
        labelframe3 = LabelFrame(second_frame, text='Add your second text here', width=270, height=85, font=fontStyle3,
                                 bg=color3)
        labelframe3.place(x=20, y=300)

        button7 = Button(labelframe3, text='Browse your computer', bg=color6, command=lambda: browse2())
        button7.place(x=30, y=10)

        text_area_2 = st.ScrolledText(second_frame,
                                      width=20,
                                      height=15,
                                      font=("Times New Roman",
                                            10))
        text_area_2.insert(tk.INSERT, "");
        text_area_2.grid(column=0, pady=10, padx=10)
        text_area_2.place(x=150, y=410)
        text_area_2.config(state=DISABLED)
        label_list2 = Label(second_frame, text='List of words in the text 2 :', anchor='w', width=35, bg=color3)
        label_list2.place(x=150, y=390)

        browse = 0
    elif c == 2:

        button14 = Button(third_frame, text='second select', width='10', height='3', font=fontStyle3, bg=color7,
                          command=lambda: select2())
        button14.place(x=180, y=580)


def sel_color_disable():
    if b.get() == 1:
        colors_list.config(state="disable")
    else:
        colors_list.config(state="normal")


def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)


# ---------------------------First_frame------------------------------------------------------------------------

first_frame = Frame(root, width=300, height=650, bg=color4)
first_frame.pack(side=LEFT)

fontStyle1 = tkFont.Font(family="Lucida Grande", size=30)
welcome = Label(first_frame, text=''' Welcome in 
our wordcloud 
generator''', font=fontStyle1, bg=color4)
welcome.place(x=20, y=40)

fontStyle2 = tkFont.Font(size=15)
chose = LabelFrame(first_frame, text='choose your mode', width=270, height=430, font=fontStyle2, bg=color4)
chose.place(x=10, y=200)

v = IntVar()
fontStyle3 = tkFont.Font(size=10)
button1 = Radiobutton(chose, text='create wordcloud', width=15, anchor='w',
                      font=fontStyle3, bg=color5, variable=v, value=0)
button1.place(x=20, y=30)

button2 = Radiobutton(chose, text='compare two textes', width=15, anchor='w',
                      font=fontStyle3, bg=color5, variable=v, value=1)
button2.place(x=20, y=80)

button3 = Radiobutton(chose, text='compare two masks', width=15, anchor='w',
                      font=fontStyle3, bg=color5, variable=v, value=2)
button3.place(x=20, y=130)

button8 = Button(chose, text='submit', bg=color5, command=lambda: submit1())
button8.place(x=20, y=170)

cloudy = PhotoImage(file="cloud.png")
cloudy1 = Label(chose, image=cloudy, bg=color4)
cloudy1.place(x=10, y=230)

text1 = Label(chose, text='Create your own word cloud !', bg='white')
text1.place(x=50, y=310)
# --------------------------------second_frame-------------------------------------------------------------------

second_frame = Frame(root, width=300, height=650, bg=color3)
second_frame.pack(side=LEFT)

fontStyle4 = tkFont.Font(size=20)
label1 = Frame(second_frame, width=300, height=100, bg='cyan4')
label1.place(x=0, y=0)

label2 = Label(label1, text='Compose your texte :', font=fontStyle4, bg='cyan4')
label2.place(x=10, y=30)

labelframe1 = LabelFrame(second_frame, text='Add some others stop words', width=270, height=80, font=fontStyle3,
                         bg=color3)
labelframe1.place(x=20, y=100)

entry2 = Entry(labelframe1, width=20, bg='white')
entry2.place(x=20, y=12)

button5 = Button(labelframe1, text='submit', bg=color6, command=lambda: lecture_stopwords())
button5.place(x=160, y=10)

labelframe2 = LabelFrame(second_frame, text='Add your first text here', width=270, height=85, font=fontStyle3,
                         bg=color3)
labelframe2.place(x=20, y=200)

button6 = Button(labelframe2, text='Browse your computer', bg=color6, command=lambda: browse1())
button6.place(x=30, y=10)

text_area = st.ScrolledText(second_frame,
                            width=20,
                            height=15,
                            font=("Times New Roman",
                                  10))
text_area.insert(tk.INSERT, "");
text_area.grid(column=0, pady=10, padx=10)
text_area.place(x=5, y=410)
label_list = Label(second_frame, text='List of words in the text 1 :', anchor='w', width=35, bg=color3)
label_list.place(x=5, y=390)
text_area.config(state=DISABLED)



# ------------------------third_frame---------------------------------------------------------------------------
third_frame = Frame(root, width=300, height=650, bg=color2)
third_frame.pack(side=LEFT)

label10 = Frame(third_frame, width=300, height=100, bg='cyan3')
label10.place(x=0, y=0)

label12 = Label(label10, text='Choose your mask :', font=fontStyle4, bg='cyan3')
label12.place(x=10, y=30)

s = StringVar()
parrot12 = PhotoImage(file="parrot1.png")
parrot = Label(third_frame, image=parrot12, bg=color2)
parrot.place(x=5, y=110)

parrotRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="parrot1.jpg")
parrotRadioButton.place(x=35, y=175)
parrotRadioButton.select()

sonic = PhotoImage(file="sonic.png")
Sonic = Label(third_frame, image=sonic, bg=color2)
Sonic.place(x=125, y=105)

sonicRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="sonic.jpg")
sonicRadioButton.place(x=135, y=175)

jerry = PhotoImage(file="jerry.png")
Jerry = Label(third_frame, image=jerry, bg=color2)
Jerry.place(x=210, y=100)

jerryRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="jerry.jpg")
jerryRadioButton.place(x=230, y=175)

tree = PhotoImage(file="tree.png")
Tree = Label(third_frame, image=tree, bg=color2)
Tree.place(x=10, y=215)

treeRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="tree.jpg")
treeRadioButton.place(x=35, y=265)

spiderman = PhotoImage(file="spiderman.png")
Spiderman = Label(third_frame, image=spiderman, bg=color2)
Spiderman.place(x=110, y=200)

spidermanRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="spiderman.jpg")
spidermanRadioButton.place(x=135, y=265)

bebe = PhotoImage(file="bebe.png")
Bebe = Label(third_frame, image=bebe, bg=color2)
Bebe.place(x=217, y=200)

bebeRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="bebe.jpg")
bebeRadioButton.place(x=230, y=265)

green = PhotoImage(file="green.png")
Green = Label(third_frame, image=green, bg=color2)
Green.place(x=20, y=295)

greenRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="green.jpg")
greenRadioButton.place(x=35, y=365)

jocker = PhotoImage(file="jocker.png")
Jocker = Label(third_frame, image=jocker, bg=color2)
Jocker.place(x=125, y=300)

jockerRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="jocker.jpg")
jockerRadioButton.place(x=135, y=365)

piro2 = PhotoImage(file="piro2.png")
parrot2 = Label(third_frame, image=piro2, bg=color2)
parrot2.place(x=217, y=295)

parrot2RadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="piro2.jpg")
parrot2RadioButton.place(x=230, y=365)

rabbit = PhotoImage(file="rabbit.png")
Rabbit = Label(third_frame, image=rabbit, bg=color2)
Rabbit.place(x=20, y=385)

rabbitRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="rabbit.jpg")
rabbitRadioButton.place(x=32, y=456)

suit = PhotoImage(file="suit.png")
Suit = Label(third_frame, image=suit, bg=color2)
Suit.place(x=125, y=390)

suitRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="suit.jpg")
suitRadioButton.place(x=133, y=456)

fish = PhotoImage(file="fish.png")
Fish = Label(third_frame, image=fish, bg=color2)
Fish.place(x=217, y=390)

fishRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="fish.jpg")
fishRadioButton.place(x=230, y=456)

tom = PhotoImage(file="tom.png")
Tom = Label(third_frame, image=tom, bg=color2)
Tom.place(x=20, y=480)

tomRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="tom.jpg")
tomRadioButton.place(x=32, y=540)

love = PhotoImage(file="love.png")
Love = Label(third_frame, image=love, bg=color2)
Love.place(x=125, y=480)

loveRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="love.jpg")
loveRadioButton.place(x=133, y=540)

aman = PhotoImage(file="aman.png")
Aman = Label(third_frame, image=aman, bg=color2)
Aman.place(x=217, y=485)

amanRadioButton = Radiobutton(third_frame, bg=color2, variable=s, value="aman.jpg")
amanRadioButton.place(x=228, y=540)

button13 = Button(third_frame, text='select', width='7', height='3', font=fontStyle3, bg=color7,
                  command=lambda: select1())
button13.place(x=20, y=580)

# --------------------------------------------fourth_frame-------------------------------------------------------
fourth_frame = Frame(root, width=300, height=650, bg=color1)
fourth_frame.pack(side=LEFT)

label15 = Frame(fourth_frame, width=300, height=100, bg='cyan2')
label15.place(x=0, y=0)

label16 = Label(label15, text='      Last details !', font=fontStyle4, bg='cyan2')
label16.place(x=10, y=30)

labelframe3 = LabelFrame(fourth_frame, text='Colors settings', width=280, height=250, font=fontStyle2, bg=color1)
labelframe3.place(x=5, y=100)

colors_list = ttk.Combobox(labelframe3, values=["Random", "Red", "Blue", "Green"])
colors_list.current(0)

colors_list.place(x=5, y=70)

b = IntVar()
color1RadioButton = Radiobutton(labelframe3, text='choose the color in the picture', font=fontStyle3, bg=color1,
                                variable=b, value=1, command=sel_color_disable)
color1RadioButton.select()
color1RadioButton.place(x=5, y=5)

color2RadioButton = Radiobutton(labelframe3, text='choose a single color', font=fontStyle3, bg=color1, variable=b,
                                value=2, command=sel_color_disable)
color2RadioButton.place(x=5, y=40)

colors_list.config(state="disable")

label17 = Label(labelframe3, text='Do you want to add an outline?', bg=color1)
label17.place(x=5, y=90)

a = IntVar()
counterradiobutton1 = Radiobutton(labelframe3, text='YES', bg=color1, variable=a, value=1)
counterradiobutton1.place(x=15, y=110)

counterradiobutton2 = Radiobutton(labelframe3, text='NO', bg=color1, variable=a, value=0)
counterradiobutton2.place(x=110, y=110)

label18 = Label(labelframe3, text='Choose your background color  :', bg=color1)
label18.place(x=5, y=130)

colors_list2 = ttk.Combobox(labelframe3, values=["black", "red", "blue", "green", "white"])
colors_list2.current(0)
colors_list2.place(x=5, y=150)

fontStyle5 = tkFont.Font(family='freesansbold.ttf', size=20)
generatebutton = Button(fourth_frame, text='GENERATE', font=fontStyle5, bg='red2', command=lambda: generer())
generatebutton.place(x=50, y=370)
generatebutton.config(state='disabled')

button13 = Button(fourth_frame, text='Restart', width=10, font=fontStyle5, bg='SpringGreen2', command=lambda: restart())
button13.place(x=50, y=480)

exit_button = Button(fourth_frame, text='Exit', width=10, font=fontStyle5, bg='gray20', command=lambda: exit())
exit_button.place(x=50, y=590)
dor = PhotoImage(file="dor.png")
Dor = Label(fourth_frame, image=dor, bg='gray20')
Dor.place(x=60, y=600)

# ---------------------------------------------------------------------------------------------------
root.mainloop()
