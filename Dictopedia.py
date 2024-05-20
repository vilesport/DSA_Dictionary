import json
import Load_Database
import TRIE
import tkinter as TKB
from pathlib import Path
from tkinter import Tk, Button, PhotoImage, ttk, scrolledtext
"""
    Init database - Trie
"""

a_v = open('./database/dba-v.json', encoding = 'utf-8')
v_a = open('./database/dbv-a.json', encoding = 'utf-8')

base_a_v = json.load(a_v)
base_v_a = json.load(v_a)

mode = 0

trie = []
history = []
history.append([])
history.append([])

trie.append(TRIE.Trie())
trie.append(TRIE.Trie())

for i in base_a_v:
    trie[0].insert(i['word'], i)

for i in base_v_a:
    trie[1].insert(i['word'], i)

ASSETS_PATH = Path(__file__).parent / 'assets'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def repress():
    global button_image_2
    global button_2
    global button_image_3
    global button_3
    global mode
    if(mode == 0):
        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3_on.png"))

    if(mode == 1):
        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2_on.png"))
        
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ENG_Mode(),
        relief="flat"
    )
    button_2.place(
        x=755.9999694824219,
        y=148.00000774860382,
        width=187.0001220703125,
        height=31.0
    )
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: VNI_Mode(),
        relief="flat"
    )
    button_3.place(
        x=755.9999771118164,
        y=187.00000774860382,
        width=187.0001220703125,
        height=31.0
    )

def ENG_Mode():
    global mode
    if(mode == 0):
        return
    mode = 0
    repress()

def VNI_Mode():
    global mode
    if(mode == 1):
        return
    mode = 1
    repress()

def Search():
    global mode
    global history
    global table
    OUT = 0
    word = entry_1.get().lower()
    if(len(word) == 0):
        return
    result = trie[mode].search(word)
    if (result != None):
        table.configure(state="normal")
        table.delete('1.0', TKB.END)
        for i in result:
            if(OUT == 0):
                table.insert(TKB.INSERT, "Word: " + i['word'] + "\n")
                if(i['word'] not in history[mode]):
                    history[mode].append(i['word'])
                OUT = 1
            table.insert(TKB.INSERT, "Pronunciation: " + i['pronunciation'] + "\n")
            table.insert(TKB.INSERT, "Definition:\n" + i['definition'] + "\n")
        table.configure(state="disabled")
        table_place()

def Search_alt(event):
    global mode
    global history
    global table
    OUT = 0
    word = event.widget.get().lower()
    result = trie[mode].search(word)
    table.configure(state="normal")
    table.delete('1.0', TKB.END)
    if(len(word) == 0):
        table.configure(state="disabled")
        table_place()
        return
    if (result != None):
        for i in result:
            if(OUT == 0):
                table.insert(TKB.INSERT, "Word: " + i['word'] + "\n")
                if(i['word'] not in history[mode]):
                    history[mode].append(i['word'])
                OUT = 1
            table.insert(TKB.INSERT, "Pronunciation: " + i['pronunciation'] + "\n")
            table.insert(TKB.INSERT, "Definition:\n" + i['definition'] + "\n")
    table.configure(state="disabled")
    table_place()

def table_place():
    global table
    table.place(
        x = 265.0,
        y = 243.9999772310257,
        width = 678,
        height = 333,
    )
    return

window = Tk()

window.geometry("1024x640")
window.title("DICTOPEDIA")
window.configure(bg = "#FEFAF6")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Search(),
    relief="flat"
)
button_1.place(
    x=115.58740234375,
    y=243.89641015637318,
    width=123.4496195585009,
    height=44.20748654368634
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2_on.png"))
if(mode == 0):
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ENG_Mode(),
    relief="flat"
)
button_2.place(
    x=755.9999694824219,
    y=148.00000774860382,
    width=187.0001220703125,
    height=31.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3_on.png"))
if(mode == 1):
    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: VNI_Mode(),
    relief="flat"
)

button_3.place(
    x=755.9999771118164,
    y=187.00000774860382,
    width=187.0001220703125,
    height=31.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=0.0985107421875,
    y=0.863229502647755,
    width=1025.1970377663297,
    height=118.72643057372852
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=124.96380615234375,
    y=135.81052147808384,
    width=225.0724248480161,
    height=43.37897354082554
)

def typing(event):
    global mode
    word = event.widget.get().lower()
    if word == '':
        entry_1['value'] = history[mode]
    else:
        data = trie[mode].autocomplete(word, 10)
        ret = []
        for i in data:
            if(len(i[0]) > 26):
                continue
            ret.append(i[0])
        entry_1['value'] = ret

combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                        settings = {'TCombobox':
                                    {'configure':
                                    {'fieldbackground': '#DAC0A3',
                                    'foreground' : '#102C57',
                                    'background' : '#DAC0A3',
                                    'selectbackground' : 'DimGray',
                                    'font' : "Calibri 14 bold",
                                    }}}
                        )
combostyle.theme_use('combostyle')

entry_1 = ttk.Combobox(
    window,
    font=("Calibri 14 bold"),
    value = history
)
entry_1.place(
    x=131.0,
    y=189.00000774860382,
    width=555.0,
    height=28.0
)

entry_1.bind('<KeyRelease>', typing)
entry_1.bind('<Button-1>', typing)
entry_1.bind('<Return>', Search_alt)

table = scrolledtext.ScrolledText(window, 
                                width = 678,  
                                height = 333,  
                                background="#DAC0A3",
                                foreground="#102C57",
                                selectbackground='DimGray',
                                font=("Calibri 14 bold"),
                                )

table_place()

def main():
    window.resizable(False, False)
    window.mainloop()

if __name__ == '__main__':
    main()