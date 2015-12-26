import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.filedialog as filedialog
from tkinter import *

#Window
win = tk.Tk()#create a window
win.title("Tkinter Text Editor") #create title

#Menu
menu1 = tk.Menu(win) #create a menu
win.config(menu=menu1) #add menu to window

current_file = None
current_filename = None

#Save Command
def Save():
    print("Saving changes ...")
    # filename = dialog.askopenfilename(initialdir='C:\\Users\\mike\\Documents', title='Save python file', filetypes=(('python files', '*.py'),('python files', '*.pyw'),('text files', '*.txt'),('all files','*.*')))
    print(current_filename)
    file = open(current_filename, 'w')
    file.write(editArea.get('1.0','end-1c'))

#Save As Command
def Save_As():
    print('Saving as new file ...')
    # filename = dialog.askopenfilename(initialdir='C:\\Users\\mike\\Documents', title='Save python file', filetypes=(('python files', '*.py'),('python files', '*.pyw'),('text files', '*.txt'),('all files','*.*')))
    filename = filedialog.asksaveasfilename()
    file = open(filename, 'w')
    file.write(editArea.get('1.0',END))
    
#Open Command
def Open():
    print("Opening file ...")
    filename = filedialog.askopenfilename()
    file = open(filename, 'r')
    text = file.read()
    print(text)
    editArea.delete('1.0', END)
    editArea.insert(INSERT,text)
    global current_file
    global current_filename
    current_file = file
    current_filename = filename
    
#File Menu
file = tk.Menu(menu1, tearoff=False) #create file menu
file.add_command(label='Open', command=Open) #add save command to file menu
file.add_command(label='Save', command=Save) #add save command to file menu
file.add_command(label='Save As', command=Save_As) #add save as command to file menu
file.add_separator()
file.add_command(label='Exit', command=exit)
menu1.add_cascade(label='File', menu=file) #add the file menu to the menu

#Frame
frame1 = tk.Frame(
    master = win,
)
frame1.pack(fill='both', expand='yes')

#Edit Area
editArea = scrolledtext.ScrolledText(
    master = frame1,
    wrap = tk.WORD,
    width = 50,
    height = 20    
)
editArea.pack(fill=tk.BOTH, expand=True)


win.mainloop()
