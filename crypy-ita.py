#programmatori:
#Andrea Dipace             email:<dipace.skrillex@gmail.com>
#Oscar Andrea Merandi      email:<oscar.andrea@hotmail.it>
#Agostino  "B50D" Di Lillo    email:<dilillo.agostino@gmail.com>

from Tkinter import *
import tkFileDialog, os, hashlib
from tkMessageBox import *

def Controlla():
    global ok
    valore_var1 = var1.get()
    valore_var2 = var2.get()
    if valore_var1 == 2 and valore_var2 in (9, 10, 11, 12, 13, 14):
        showinfo("Errore", "L'algoritmo che hai inserito pu0' solo essere codificato")
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
            showinfo("Errore", "Il comando o il metodo non sono stati selezionati. Riprova.")
        else:
            path = tkFileDialog.askopenfilename(title='valore_var2 the file', filetypes=[("Text files", "*.txt")])
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
            showinfo("Errore", "Il comando o il metodo non sono stati selezionati. Riprova.")
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
    elif metodo.lower() == 'binario':
        try:
            number_int = int(text)
        except:
            info = showinfo("Errore", "Puoi inserire solo numeri")
            ok = 0
        else:
            number_int = bin(number_int)
            text_encoded = number_int[2:]
    elif metodo.lower() == 'ottale':
        try:
            number_int = int(text)
        except:
            info = showinfo("Errore", "Puoi inserire solo numeri")
            ok = 0
        else:
            number_int = oct(number_int)
            text_encoded = number_int[1:]
    elif metodo.lower() == 'esadecimale':
        try:
            number_int = int(text)
        except:
            info = showinfo("Errore", "Puoi inserire solo numeri")
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
        salva = askyesno("Vuoi salvare?", "Vuoi salvare il testo codificato in un file.txt?")
        if salva:
            file_in_cui_mettere_il_testo = open('CryPy_testo_codificato.txt', 'w')
            file_in_cui_mettere_il_testo.write(text_encoded)
            file_in_cui_mettere_il_testo.close()
            showinfo("File salvato", "File salvato con il nome CryPy_testo_codificato.txt")
def Decodifica(text):
    import base64
    global ok
    if metodo.lower() == 'base16':
        text_decoded = base64.b16decode(text)
    elif metodo.lower() == 'base32':
        text_decoded = base64.b32decode(text)
    elif metodo.lower() == 'base64':
        text_decoded = base64.b64decode(text)
    elif metodo.lower() == 'binario':
        try:
            text_decoded = int(text, 2)
        except:
            info = showinfo("Errore", "Puoi inserire solo i numeri 0 e 1")
            ok = 0
    elif metodo.lower() == 'ottale':
        try:
            text_decoded = int(text, 8)
        except :
            info = showinfo("Errore", "Puoi inserire solo numerida 0 a 7")
            ok = 0
    elif metodo.lower() == 'esadecimale':
        try:
            text_decoded = int(text, 16)
        except:
            info = showinfo("Errore", "Puoi inserire solo numeri da 0 a 9 e lettere dalla 'a' alla 'f'")
            ok = 0
    if ok != 0:
        testo_cod_o_dec.delete('1.0', END)
        testo_cod_o_dec.insert(END, text_decoded)
        salva = askyesno("Vuoi salvare?", "Vuoi salvare il testo decodificato in un file.txt?")
        if salva:
            file_in_cui_mettere_il_testo = open('CryPy_testo_decodificato.txt', 'w')
            file_in_cui_mettere_il_testo.write(text_decoded)
            file_in_cui_mettere_il_testo.close()
            showinfo("File salvato", "File salvato con il nome CryPy_testo_decodificato.txt")
def sel_command():
    valore_var2_command = var1.get()
    if valore_var2_command == 1:
        metodo_comando = 'codifica'
    elif valore_var2_command == 2:
        metodo_comando = 'decodifica'
    valore_var2ion = "Comando: " + metodo_comando
    label_comando.config(text = valore_var2ion)
def sel_metodo():
    global metodo
    global chiave
    valore_var2 = var2.get()
    if valore_var2 == 3:
        metodo = 'base16'
    elif valore_var2 == 4:
        metodo =  'base32'
    elif valore_var2 == 5:
        metodo = 'base64'
    elif valore_var2 == 6:
        metodo = 'binario'
    elif valore_var2 == 7:
        metodo = 'ottale'
    elif valore_var2 == 8:
        metodo = 'esadecimale'
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
    
    selection = "Metodo richiesto: " + metodo
    label_metodo.config(text = selection)

CryPy = Tk()
CryPy.geometry('300x285')
CryPy.title('CryPy 1.0-beta')
CryPy.resizable(False, False)
var1 = IntVar()
var2 = IntVar()
menu_principale = Menu(CryPy)
menu_file = Menu(menu_principale, tearoff = 0)
menu_principale.add_cascade(label = 'File', menu = menu_file)
menu_file.add_command(label = 'Importa testo da file', command = Importa_Testo_Da_File)
menu_algoritmo = Menu(menu_principale, tearoff = 0)
menu_principale.add_cascade(label = 'Algoritmo', menu = menu_algoritmo)
menu_base = Menu(menu_algoritmo, tearoff = 0)
menu_algoritmo.add_cascade(label = 'Base', menu = menu_base)
menu_base.add_radiobutton(label="base16", variable = var2, value = 3,command=sel_metodo)
menu_base.add_radiobutton(label="base32", variable = var2, value = 4,command=sel_metodo)
menu_base.add_radiobutton(label="base64", variable = var2, value = 5,command=sel_metodo)
menu_sistemi = Menu(menu_algoritmo, tearoff = 0)
menu_algoritmo.add_cascade(label = 'Sistemi', menu = menu_sistemi)
menu_sistemi.add_radiobutton(label="binario", variable = var2, value = 6,command=sel_metodo)
menu_sistemi.add_radiobutton(label="ottale", variable = var2, value = 7,command=sel_metodo)
menu_sistemi.add_radiobutton(label="esadecimale", variable = var2, value = 8,command=sel_metodo)
menu_hash = Menu(menu_algoritmo, tearoff = 0)
menu_algoritmo.add_cascade(label = 'Algoritmi di generazione hash', menu = menu_hash)
menu_hash.add_radiobutton(label="md5", variable = var2, value = 9,command=sel_metodo)
menu_hash.add_radiobutton(label="sha1", variable = var2, value = 10,command=sel_metodo)
menu_hash.add_radiobutton(label="sha224", variable = var2, value = 11,command=sel_metodo)
menu_hash.add_radiobutton(label="sha256", variable = var2, value = 12,command=sel_metodo)
menu_hash.add_radiobutton(label="sha384", variable = var2, value = 13,command=sel_metodo)
menu_hash.add_radiobutton(label="sha512", variable = var2, value = 14,command=sel_metodo)
menu_crypt = Menu(menu_algoritmo, tearoff = 0)


comando = Label(CryPy, text = "Comando:").pack( anchor = W )
codifica = Radiobutton(CryPy, text="Codifica", variable = var1, value = 1,command=sel_command).pack( anchor = W )
decodifica = Radiobutton(CryPy, text="Decodifica", variable = var1, value = 2, command=sel_command).pack( anchor = W )
label_comando = Label(CryPy, text = 'Comando: niente selezionato')
label_comando.pack(anchor = W)
label_metodo = Label(CryPy, text = 'Metodo richiesto: niente selezionato')
label_metodo.pack(anchor = W)
inserisci_testo = Label(CryPy, text = '\nInserisci testo da codificare/decodificare:').pack(anchor = W)
testo = Text(CryPy, width=42, height=3)
testo.pack()
invio = Button(CryPy, text = 'Applica', command = Codifica_o_Decodifica_testo).pack(fill = X)
infor_text = Label(CryPy, text = "Testo codificato/decodificato").pack(anchor = W)
testo_cod_o_dec = Text(CryPy,width=42,height=3)
testo_cod_o_dec.pack()
CryPy.config(menu = menu_principale)
CryPy.mainloop()
