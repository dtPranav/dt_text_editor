import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog,messagebox
import os

win=tk.Tk()
win.title('Dt Editor')
win.geometry('1200x800')
win.wm_iconbitmap('icon.ico')
# label1=ttk.LabelFrame(win,text='Editor')
# label1.grid(row=0,column=0)
# --------------------------------------------------------main menu---------------------------------------------------
main_menu=tk.Menu(win)


# file icons
new_icon=tk.PhotoImage(file='icons2/new.png')
open_icon=tk.PhotoImage(file='icons2/open.png')
save_icon=tk.PhotoImage(file='icons2/save.png')
saveas_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_icon=tk.PhotoImage(file='icons2/exit.png')
file_menu=tk.Menu(main_menu,tearoff=0)
main_menu.add_cascade(label='File',menu=file_menu)
                 

copy_icon=tk.PhotoImage(file='icons2/copy.png')
paste_icon=tk.PhotoImage(file='icons2/paste.png')
cut_icon=tk.PhotoImage(file='icons2/cut.png')
clear_icon=tk.PhotoImage(file='icons2/clear_all.png')
find_icon=tk.PhotoImage(file='icons2/find.png')
edit_menu=tk.Menu(main_menu,tearoff=0)
main_menu.add_cascade(label='Edit',menu=edit_menu)


tool_icon=tk.PhotoImage(file='icons2/tool_bar.png')
status_icon=tk.PhotoImage(file='icons2/status_bar.png')
view_menu=tk.Menu(main_menu,tearoff=0)
main_menu.add_cascade(label='View',menu=view_menu)


light_icon=tk.PhotoImage(file='icons2/light_default.png')
light2_icon=tk.PhotoImage(file='icons2/light_plus.png')
dark_icon=tk.PhotoImage(file='icons2/dark.png')
red_icon=tk.PhotoImage(file='icons2/red.png')
mk_icon=tk.PhotoImage(file='icons2/monokai.png')
nb_icon=tk.PhotoImage(file='icons2/night_blue.png')
color_theme=tk.Menu(main_menu,tearoff=0)

theme_choice=tk.StringVar()
color={
    'Light Default':light_icon,
    'Light Plus':light2_icon,
    'Dark':dark_icon,
    'Red':red_icon,
    'Monokai':mk_icon,
    'Night Blue':nb_icon
    }
color_dict={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')
    }
main_menu.add_cascade(label='Color Theme',menu=color_theme)
# ---------------------------------------------------------end menu-------------------------------------------------------

# ---------------------------------------------------------tool bar----------------------------------------------------
#-----------font box------------------
tool_bar=ttk.Label(win)
tool_bar.pack(side=tk.TOP,fill=tk.X)

font_tuples=tk.font.families()
font_family=tk.StringVar()
c_font=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
c_font['values']= font_tuples
c_font.current(font_tuples.index('Arial'))
c_font.grid(row=0,column=0,padx=5)

# ------------------size box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=20,textvariable=size_var)
font_size['values']=tuple(range(8,100,2))
font_size.current(2)
font_size.grid(row=0,column=1)

#----------buttons----------------

# print(buttons[0])
bold_icons=tk.PhotoImage(file='icons2/bold.png')
italic_icons=tk.PhotoImage(file='icons2/italic.png')
under_icons=tk.PhotoImage(file='icons2/underline.png')
font_icons=tk.PhotoImage(file='icons2/font_color.png')
align_left_icons=tk.PhotoImage(file='icons2/align_left.png')
align_center_icons=tk.PhotoImage(file='icons2/align_center.png')
align_right_icons=tk.PhotoImage(file='icons2/align_right.png')
buttons={'bold':bold_icons ,
        'italic':italic_icons ,
        'underline':under_icons,
        'font_color':font_icons,
        'align_left':align_left_icons,
        'align_center':align_center_icons,
        'align_right':align_right_icons,
        }
k=2
button=[]
for i,j in buttons.items():
    i=ttk.Button(tool_bar,image=j)
    i.grid(row=0,column=k,padx=5)
    button.append(i)
    k+=1
# ---------------------------------------------------------end tool bar----------------------------------------------------

# ---------------------------------------------------------text editor----------------------------------------------------
text_editor=tk.Text(win)
text_editor.config(wrap='word',relief=tk.FLAT) #wrap=to move word to next line 
scroll_bar=tk.Scrollbar(win)
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)
text_editor.pack(fill=tk.BOTH,expand=True)
text_editor.focus_set()

# scroll_bar2=tk.Scrollbar(win)
# text_editor.config(wrap='word',relief=tk.FLAT) #wrap=to move word to next line 
# scroll_bar2.pack(side=tk.BOTTOM ,fill=tk.X)
# scroll_bar2.config(command=text_editor.xview)
# text_editor.config(xscrollcommand=scroll_bar2.set)
# text_editor.pack(fill=tk.BOTH,expand=True)
# text_editor.focus_set()

#font family and font size functionality
current_font_family='Arial'
current_font_size=12

def change_font(win):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.config(font=(current_font_family,current_font_size))    

def change_font_size(win):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.config(font=(current_font_family,current_font_size))
c_font.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_font_size)

text_editor.config(font=('Arial',12))
# ------------------button functionality------------------
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']== 'normal':
        text_editor.config(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']== 'bold':
        text_editor.configure(font= (current_font_family, current_font_size,'normal'))        
button[0].configure(command=change_bold)

def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman' :
        text_editor.config(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.config(font=(current_font_family,current_font_size,'normal'))
button[1].configure(command=change_italic)

def underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.config(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.config(font=(current_font_family,current_font_size,'normal'))
button[2].configure(command=underline)    

def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.config(fg=color_var[1])
button[3].configure(command=change_font_color)


def change_align_left():
    change_var=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,change_var,'left')
button[4].configure(command=change_align_left)

def change_align_right():
    change_var=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,change_var,'right')
button[6].configure(command=change_align_right)

def change_align_center():
    change_var=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,change_var,'center')
button[5].configure(command=change_align_center)
# ---------------------------------------------------------end text editor----------------------------------------------------


# ---------------------------------------------------------status bar----------------------------------------------------
status_bar=ttk.Label(win,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Characters: {characters} words:{words}')
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',changed)        

#------- ------------------------------------------------end status bar----------------------------------------------------

#-----------------------------------------------------main menu functionality------------------------------------------------
#--------------variable-------------
url = ''
# ---------new_functionality----
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)

def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text file','*.txt'),('All files','*.*')))
    try:
        with open (url,'r') as f:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,f.read())
    except FileNotFoundError:
        return
    except:
        return
    win.title(os.path.basename(url))

#-----------save file---------------
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0, tk.END))
            with open(url, 'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url= filedialog.asksaveasfile(mode= 'w',defaultextension='.txt',filetypes=(('Text file','*.txt'),('All files','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return

# --------------------save as--------------------
def saveas_file(event=None):
    global url
    try:
        content=text_editor.get(1.0, tk.END)
        url= filedialog.asksaveasfile(mode= 'w',defaultextension='.txt',filetypes=(('Text file','*.txt'),('All files','*.*')))
        url.write(content)
        url.close()
    except:
        return

#-----------------------exit---------------------
def exit_file(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning','Do you want to save the file')
            if mbox is True:
                if url:
                    content=text_editor.get(1.0,'tk.end')
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content) 
                        win.destroy()
                else:
                    content2 = text_editor.get(1.0,tk.END)
                    url= filedialog.asksaveasfile(mode= 'w',defaultextension='.txt',filetypes=(('Text file','*.txt'),('All files','*.*')))
                    url.write(content2)
                    win.destroy()
            elif mbox is False:
                win.destroy()
        else:
            win.destroy()
    except:
        return            

# file menu Commands

file={'New':[new_file,new_icon,'Ctrl+N'],
    'Open':[open_file,open_icon,'Ctrl+O'],
    'Save':[save_file,save_icon,'Ctrl+S'],
    'Save as':[saveas_file,saveas_icon,'Ctrl+Alt+S'],
    'exit':[exit_file,exit_icon,'Ctrl+Q']}

for i,j in file.items():
    file_menu.add_command(label=i,image=j[1],compound=tk.LEFT,accelerator=j[2],command=j[0])
    

#----------------------------------------------------- edit commands-----------------------------------------------------------
# ----------------------find functionality------
def find_func(event=None):
    
    def find():
        word=find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos=1.0
            while True:
                start_pos = text_editor.search(word, start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos = end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')                
    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
    
    find_dialogue=tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title("Find")
    find_dialogue.resizable(0,0)
    
    #frame
    find_frame=ttk.LabelFrame(find_dialogue,text='find replace')
    find_frame.pack(pady=20)
    #labels
    text_find_label=ttk.Label(find_frame,text='Find :')
    text_replace_label=ttk.Label(find_frame,text='Replace :')
    #entry input
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)
    #button
    find_button=ttk.Button(find_frame,text='Find',command=find)
    replace_button=ttk.Button(find_frame,text='Replace',command=replace)
    #label grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)
    #entry grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    #button grid
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)

    find_dialogue.mainloop()

edit={'Copy':[copy_icon,lambda:text_editor.event_generate("<Control c>"),'Ctrl+C'],
    'Cut':[cut_icon,lambda:text_editor.event_generate("<Control x>"),'Ctrl+X'],
    'Paste':[paste_icon,lambda:text_editor.event_generate("<Control v>"),'Ctrl+V'],
    'Clear All':[clear_icon,lambda:text_editor.destroy(1.0,tk.END),'Ctrl+Alt+C'],
    'Find':[find_icon,find_func,'Ctrl+F']}

for i,j in edit.items():
    edit_menu.add_command(label=i,image=j[0],compound=tk.LEFT ,accelerator=j[2],command=j[1])


# view commands
status_show=tk.BooleanVar()
status_show.set(False)
tool_show=tk.BooleanVar()
tool_show.set(False)

def hide_status():
    global status_show
    if status_show:
        status_bar.pack_forget()
        status_show=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        status_show=True
def hide_tool():
    global tool_show
    if tool_show:
        tool_bar.pack_forget()
        tool_show=False
    else:
        text_editor.pack_forget()
        tool_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        tool_show=True

view={'Tool bar':[tool_icon,'tool_show',hide_tool],
    'Status bar':[status_icon,'status_show',hide_status]}
for i,j in view.items():
    a=str(i)+'_show'
    view_menu.add_checkbutton(label=i,onvalue=True,offvalue=False,variable=j[1],image=j[0],compound=tk.LEFT,command=j[2])

# Color Theme Commands
def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)

for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color[i],variable=theme_choice,compound=tk.LEFT,command=change_theme)
# --------------------------------------------------end main menu functionalty---------------------------------------------
win.config(menu=main_menu)
#bind shortcut keys
win.bind('<Control-n>',new_file)
win.bind('<Control-o>',open_file)
win.bind('<Control-s>',save_file)
win.bind('<Control-Alt-s>',saveas_file)
win.bind('<Control-q>',exit_file)
win.bind('<Control-f>',find_func)

win.mainloop()  