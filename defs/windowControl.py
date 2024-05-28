

import tkinter as tk
from defs.databaseControl import *
import defs.databaseControl as dc 
from defs.varControl import * 
import __main__ as mn





def closeFrame(frame):
    ''' Fecha o frame selecionado.
        @param frame: frame que sera fechado 
    '''

    try:
        frame.info()
        frame.pack_forget()
    except:
        frame.grid_forget()

def openFrame(frame):
    ''' Abre uma nova janelacls
        @param self: Janela que sera aberta
    '''
    global nowFrame

    
    try:
        closeFrame(nowFrame)
    except :
        pass

    try:
        frame.pack(fill='both', expand= True)
        nowFrame = frame
    except Exception as e:
        print(e)
    return nowFrame

def shwConsulta(frame, parent = '', table = '', modelo= 0,tevent = 0, hg= 11, id= 0, aux= 'Nome'): # renomeado de shwList
    ''' exibe em formato de lista a tabela
        @param self: frame pertencente.
        @param parent: frame pai qual pertence
        @param table: table qual sera utilizada
        @param modelo: 0: mostrar tudo, 1: filtro para classes, 2:filtro para cursos
        @param tevent: evento ao dar click na tabela; padrao 0 NADA
        @param hg: quantidades de linhas da tabela  
    '''

    
    global shwSFtlist,ccSFbutton2,ccSFbutton5,ccSFbutton6, l1, df,btnCursoEnabled
    try:
        if parent != '':       
            openFrame(parent)
    
    except Exception as e:
        pass
    selecConsulta(table,modelo,id, aux)   

    df = dc.df
    l1= list(df)
    rowSet= df.to_numpy().tolist()

    

    shwSFtlist = tk.ttk.Treeview(frame, show='headings', columns=l1,height= hg)
    shwSFtlist.grid(row= 2, column=1, pady=0)
    
    if tevent == 1:
        shwSFtlist.bind("<<TreeviewSelect>>",vc.setProfMask)
    elif tevent == 2:
        mn.btnCursoEnabled = 'disabled'

        mn.ccSFbutton2.config(state= mn.btnCursoEnabled)
        mn.ccSFbutton5.config(state= mn.btnCursoEnabled)
        mn.ccSFbutton6.config(state= mn.btnCursoEnabled)
        #mn.ccSFbutton2.update()
        #mn.ccSFbutton5.update()       
        #mn.ccSFbutton6.update()
        shwSFtlist.bind("<<TreeviewSelect>>",vc.habCBnt)    

    for i in l1:
        shwSFtlist.column(i, width=95, anchor='c',stretch=False) # original width 95
        shwSFtlist.heading(i, text= str(i))
    for dt in rowSet:
        v = [r for r in dt]
        shwSFtlist.insert("", 'end', iid= v[0], values= v)
    
    mn.shwSFtlist = shwSFtlist


    try:
        return btnCursoEnabled
    except:
        pass

        