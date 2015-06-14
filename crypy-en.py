#developers:
#Andrea Dipace email:dipace.skrillex@gmail.com
#Oscar Andrea Merandi email:oscar.andrea@hotmail.it
#Agostino "B50D" Di Lillo    email:dilillo.agostino@gmail.com
from Tkinter import *
import tkFileDialog, os, hashlib
from tkMessageBox import *
def Controlla():
    global ok
    valore_var1 = var1.get()
    valore_var2 = var2.get()
    if valore_var1 == 2 and valore_var2 in (9, 10, 11, 12, 13, 14):
        showinfo("Error", "The algorithm you entered can 'only be encoded.")
        ok = 0
    else:
        ok = 1
def Importa_Testo_Da_File():
    global path
    Controlla()
    if ok == 1:
        valore_var1 = var1.get()
        valore_var2 = var2.get()
        if valore_var1 == 0 or valore_var2 == 0:
            showinfo("Error", "The command or method were not selected. Please try again.")
        else:
            path = tkFileDialog.askopenfilename(title='Select the file', filetypes=[("Text files", "*.txt")])
            path_file, nome_file = os.path.split(path)
            try:
                os.chdir(path_file)
            except:
                pass
            else:
                file_testo = open(nome_file, 'r')
                testo_da_codificare_o_decodificare = file_testo.read()
                file_testo.close()
                if valore_var1 == 1:
                    Codifica(testo_da_codificare_o_decodificare)
                elif valore_var1 == 2:
                    Decodifica(testo_da_codificare_o_decodificare)
def Codifica_o_Decodifica_testo():
    Controlla()
    if ok == 1:
        valore_var1 = var1.get()
        valore_var2 = var2.get()
        if valore_var1 == 0 or valore_var2 == 0:
            showinfo("Error", "The command or method were not selected. Please try again.")
        else:
            testo_da_codificare_o_decodificare = testo.get('1.0', 'end')
            if valore_var1 == 1:
                Codifica(testo_da_codificare_o_decodificare)
            elif valore_var1 == 2:
                Decodifica(testo_da_codificare_o_decodificare)
def Codifica(text):
    import base64
    global ok
    if metodo.lower() == 'base16':
        text_encoded = base64.b16encode(text)
    elif metodo.lower() == 'base32':
        text_encoded = base64.b32encode(text)
    elif metodo.lower() == 'base64':
        text_encoded = base64.b64encode(text)
    elif metodo.lower() == 'binary':
        try:
            number_int = int(text)
        except:
            info = showinfo("Error", "Please enter numbers only")
            ok = 0
        else:
            number_int = bin(number_int)
            text_encoded = number_int[2:]
    elif metodo.lower() == 'octal':
        try:
            number_int = int(text)
        except:
            info = showinfo("Error", "Please enter numbers only")
            ok = 0
        else:
            number_int = oct(number_int)
            text_encoded = number_int[1:]
    elif metodo.lower() == 'hexadecimal':
        try:
            number_int = int(text)
        except:
            info = showinfo("Error", "Please enter numbers only")
            ok = 0
        else:
            number_int = hex(number_int)
            text_encoded = number_int[2:]
    elif metodo.lower() == 'md5':
        hash_object = hashlib.md5(text)
        text_encoded = hash_object.hexdigest()
    elif metodo.lower() == 'sha1':
        hash_object = hashlib.sha1(text)
        text_encoded = hash_object.hexdigest()
    elif metodo.lower() == 'sha224':
        hash_object = hashlib.sha224(text)
        text_encoded = hash_object.hexdigest()
    elif metodo.lower() == 'sha256':
        hash_object = hashlib.sha256(text)
        text_encoded = hash_object.hexdigest()
    elif metodo.lower() == 'sha384':
        hash_object = hashlib.sha384(text)
        text_encoded = hash_object.hexdigest()
    elif metodo.lower() == 'sha512':
        hash_object = hashlib.sha512(text)
        text_encoded = hash_object.hexdigest()
    if ok != 0:
        testo_cod_o_dec.delete('1.0', END)
        testo_cod_o_dec.insert(END, text_encoded)
        salva = askyesno("Do you want to save text?", "Do you want to save the text encoded in a file.txt?")
        if salva:
            file_in_cui_mettere_il_testo = open('CryPy_text_encoded.txt', 'w')
            file_in_cui_mettere_il_testo.write(text_encoded)
            file_in_cui_mettere_il_testo.close()
            showinfo("File saved", "File saved as CryPy_text_encoded.txt")
def Decodifica(text):
    import base64
    global ok
    if metodo.lower() == 'base16':
        text_decoded = base64.b16decode(text)
    elif metodo.lower() == 'base32':
        text_decoded = base64.b32decode(text)
    elif metodo.lower() == 'base64':
        text_decoded = base64.b64decode(text)
    elif metodo.lower() == 'binary':
        try:
            text_decoded = int(text, 2)
        except:
            info = showinfo("Error", "You can enter only the numbers 0 and 1")
            ok = 0
    elif metodo.lower() == 'octal':
        try:
            text_decoded = int(text, 8)
        except :
            info = showinfo("Error", "You can only enter numbers from 0 to 7")
            ok = 0
    elif metodo.lower() == 'hexadecimal':
        try:
            text_decoded = int(text, 16)
        except:
            info = showinfo("Error", "You can only enter numbers from 0 to 9 and letters from 'a' to 'f'")
            ok = 0
    if ok != 0:
        testo_cod_o_dec.delete('1.0', END)
        testo_cod_o_dec.insert(END, text_decoded)
        salva = askyesno("Do you want to save text?", "Do you want to save the text decoded in a file.txt?")
        if salva:
            file_in_cui_mettere_il_testo = open('CryPy_text_decode.txt', 'w')
            file_in_cui_mettere_il_testo.write(text_decoded)
            file_in_cui_mettere_il_testo.close()
            showinfo("File saved", "File saved as CryPy_text_decode.txt")
def sel_command():
    valore_var2_command = var1.get()
    if valore_var2_command == 1:
        metodo_comando = 'encode'
        do_ok = 'Encode'
    elif valore_var2_command == 2:
        metodo_comando = 'decode'
        do_ok = 'Decode'
    valore_info1 = "\nEnter the text to be {0}:".format(metodo_comando + 'd')
    valore_info2 = "\nText {0}:".format(metodo_comando + 'd')
    valore_var2ion = "Command: " + metodo_comando
    label_comando.config(text = valore_var2ion)
    inserisci_testo.config(text = valore_info1)
    infor_text.config(text = valore_info2)
    invio.config(text = do_ok)
def sel_metodo():
    global metodo
    valore_var2 = var2.get()
    if valore_var2 == 3:
        metodo = 'base16'
    elif valore_var2 == 4:
        metodo =  'base32'
    elif valore_var2 == 5:
        metodo = 'base64'
    elif valore_var2 == 6:
        metodo = 'binary'
    elif valore_var2 == 7:
        metodo = 'octal'
    elif valore_var2 == 8:
        metodo = 'hexadecimal'
    elif valore_var2 == 9:
        metodo = 'md5'
    elif valore_var2 == 10:
        metodo = 'sha1'
    elif valore_var2 == 11:
        metodo = 'sha224'
    elif valore_var2 == 12:
        metodo = 'sha256'
    elif valore_var2 == 13:
        metodo = 'sha384'
    elif valore_var2 == 14:
        metodo = 'sha512'
    selection = "Method asked: " + metodo
    label_metodo.config(text = selection)
def Info():
    info = Tk()
    info.title('Info of CryPy')
    crypy_info_en = Label(info, text = """CryPy 1.0-beta
            
Created by CryPy team
Released under the GNU/GPL
This is a simple application
designed to encrypt and
decrypt a text in various
algorithms or systems
""").pack(side = TOP)
def How_to_use_it():
    how_to_use = Tk()
    how_to_use.title('How to use CryPy')
    crypy_how_to_use = Label(how_to_use, text = """Select what you want to do (coding, decoding),
then go to the menu above, and go with the
mouse pointer over the section 'Algorithms',
there are 3 menus in which there are three
subsections: each section contains the methods
(in depending on the type), click on the method
you need. Then, enter the text in the first
input box that you can find on the program,
after click on button 'Encode' or 'Decode'
and the text encoded or decoded will be released
in the second input box. Or: After selecting
what to do and the algorithm, go to the
section 'File', after click on 'Import text
from files', select the file.txt that contains
the text to encode / decode  and text encoded or
decoded will be released in the second input box.
After that the text will be encoded or decoded,
the program asks you whether to save the result
in a file.txt, awards to yes if you want to save
the text in a .txt file (called
'CryPy_text_encoded.txt' for a consolidated
text, ' CryPy_text_decoded.txt 'for a decoded text),
no prizes if you do not want to save.""").pack(side = TOP)
def quit():
    chiude = askyesno("Exit?", "Do you want to close the window?")
    if chiude == True:
        CryPy.destroy()
def key(event):
    char = repr(event.char)
    if char == "'\\t'":
        Importa_Testo_Da_File()
CryPy = Tk()
CryPy.geometry('300x330')
CryPy.title('CryPy 1.0-beta')
CryPy.resizable(False, False)
CryPy.protocol("WM_DELETE_WINDOW", quit)
CryPy.bind("<Key>", key)
var1 = IntVar()
var2 = IntVar()
menu_principale = Menu(CryPy)
menu_file = Menu(menu_principale, tearoff = 0)
menu_principale.add_cascade(label = 'File', menu = menu_file)
menu_file.add_command(label = 'Import text from files    Ctrl + I', command = Importa_Testo_Da_File)
menu_algoritmo = Menu(menu_principale, tearoff = 0)
menu_principale.add_cascade(label = 'Algorithm', menu = menu_algoritmo)
menu_base = Menu(menu_algoritmo, tearoff = 0)
menu_algoritmo.add_cascade(label = 'Bases', menu = menu_base)
menu_base.add_radiobutton(label="base16", variable = var2, value = 3,command=sel_metodo)
menu_base.add_radiobutton(label="base32", variable = var2, value = 4,command=sel_metodo)
menu_base.add_radiobutton(label="base64", variable = var2, value = 5,command=sel_metodo)
menu_sistemi = Menu(menu_algoritmo, tearoff = 0)
menu_algoritmo.add_cascade(label = 'Systems', menu = menu_sistemi)
menu_sistemi.add_radiobutton(label="binary", variable = var2, value = 6,command=sel_metodo)
menu_sistemi.add_radiobutton(label="octal", variable = var2, value = 7,command=sel_metodo)
menu_sistemi.add_radiobutton(label="hexadecimal", variable = var2, value = 8,command=sel_metodo)
menu_hash = Menu(menu_algoritmo, tearoff = 0)
menu_algoritmo.add_cascade(label = 'Generation algorithms hash', menu = menu_hash)
menu_hash.add_radiobutton(label="md5", variable = var2, value = 9,command=sel_metodo)
menu_hash.add_radiobutton(label="sha1", variable = var2, value = 10,command=sel_metodo)
menu_hash.add_radiobutton(label="sha224", variable = var2, value = 11,command=sel_metodo)
menu_hash.add_radiobutton(label="sha256", variable = var2, value = 12,command=sel_metodo)
menu_hash.add_radiobutton(label="sha384", variable = var2, value = 13,command=sel_metodo)
menu_hash.add_radiobutton(label="sha512", variable = var2, value = 14,command=sel_metodo)
menu_info = Menu(menu_principale, tearoff = 0)
menu_principale.add_cascade(label = 'Info', menu = menu_info)
menu_info.add_command(label = 'Info', command = Info)
menu_info.add_command(label = 'How to use it', command = How_to_use_it)
comando = Label(CryPy, text = "Command:").pack( anchor = W )
codifica = Radiobutton(CryPy, text="coding", variable = var1, value = 1,command=sel_command).pack( anchor = W )
decodifica = Radiobutton(CryPy, text="decoding", variable = var1, value = 2, command=sel_command).pack( anchor = W )
label_comando = Label(CryPy, text = 'Command: nothing selected')
label_comando.pack(anchor = W)
label_metodo = Label(CryPy, text = 'Method asked: nothing selected')
label_metodo.pack(anchor = W)
inserisci_testo = Label(CryPy, text = '\nEnter the text to be ... :')
inserisci_testo.pack(anchor = W)
testo = Text(CryPy, width=42, height=3)
testo.pack()
invio = Button(CryPy, text = '...', command = Codifica_o_Decodifica_testo, bg = 'Black', fg = 'White')
invio.pack(fill = X)
infor_text = Label(CryPy, text = "\nText ... :")
infor_text.pack(anchor = W)
testo_cod_o_dec = Text(CryPy,width=42,height=5)
testo_cod_o_dec.pack()
CryPy.config(menu = menu_principale)
CryPy.mainloop()
