import tkinter as tk

root = tk.Tk()

name_var = tk.StringVar()
result_var = tk.StringVar()

#szyfr atbash
lookup_table = {
    'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
    'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
    'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
    'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
    'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B', 'Z': 'A',
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v',
    'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q',
    'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l',
    'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
    'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'
}

def atbash(message):
    cipher = ''
    for letter in message:
        if letter in lookup_table:
            cipher += lookup_table[letter]
        else:
            cipher += letter
    return cipher

def siemson():
    name = name_var.get()
    encrypted_name = atbash(name)
    result_var.set(encrypted_name)
    name_var.set("")


def show(): 
    tk.Label.config( text = clicked.get() ) 
  
# Dropdown menu options 
options = [ 
    "ATBASH", 
    "ROT-13" 
] 
  
# datatype of menu text 
clicked = tk.StringVar() 
  
# initial menu text 
clicked.set( "Szyfry" ) 
  
# Create Dropdown menu 
drop = tk.OptionMenu( root , clicked , *options ) 
drop.grid(row=0, column=2) 

name_label = tk.Label(root, text='Tekst do zakodowania', font=('calibre', 10, 'bold'))
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))
result_label = tk.Label(root, text='Zaszyfrowany tekst', font=('calibre', 10, 'bold'))
result_display = tk.Label(root, textvariable=result_var, font=('calibre', 10, 'normal'))

sub_btn = tk.Button(root, text='zakoduj', command=siemson)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
result_label.grid(row=1, column=0)
result_display.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

root.mainloop()