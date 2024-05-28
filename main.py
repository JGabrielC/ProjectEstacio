
# Importações
import tkinter 
from tkinter import ttk 
import sqlite3
import defs.windowControl as wc
from defs.windowControl import *
import defs.databaseControl as dc
from defs.databaseControl import *
import defs.toast as tt
import defs.varControl as vc
from defs.varControl import *

# Definir variaveis que seram usadas em todo o projeto,
# Para a correta utilização dentro de um modulo sera necessario chamar __main__.variavel = localVariavel
btnCursoEnabled = 'disabled'
filter_shm = 'LIKE'
filter_cho = 'Estudantes'
filter_cbxstate = 1
filter_sel = "Nome"
filter_order = 'ASC'
cbxvar = ('ID', 'Nome', 'CPF', 'Matricula')
nid = ni = mmt = pmt = pmtmask = choosed= lbID = bxname = spcg = lbSprof = subf= conf= toast= stdBxname = stdBxmtr= stdBxid= stdLmmt= stdLii= shwSFtlist = stdFnew = tstSpbox = tstEntry = tstCXBox = cbxc = ''
    




#criar as tabelas caso nao existam
createdb(shwConsole=False)

# criar janela raiz
root = tkinter.Tk()
root.title("Cadastro Institucional ")
root.minsize(width=750, height= 400)
rtIcon = tkinter.PhotoImage(file= r'assets\icon.png')
root.iconphoto(False, rtIcon)



rmenu = tkinter.Frame(root, height=20, width=750, bg='white')
rmenu.pack(fill='x')


mniconH =tkinter.PhotoImage(file = r"assets\home.png", master=rmenu).subsample(2,2)
rmbtH = tkinter.Button(rmenu, image= mniconH,width=20,height=20, relief='groove',command= lambda:closeFrame(nowFrame)).grid(row=0,column=0)
rmbtAlunos = tkinter.Button(rmenu, text='Alunos',width=6, relief='groove', command= lambda:openFrame(stdFrame)).grid(row=0,column=1)
rmbtProf = tkinter.Button(rmenu, text='Professores',width=9, relief='groove', command= lambda: openFrame(tchFrame)).grid(row=0,column=2)
rmbtcur = tkinter.Button(rmenu, text='Cursos',width=5, relief='groove', command= lambda:shwConsulta(ccSFrame,ccFrame,'cursos',modelo= 2, tevent= 2)).grid(row=0,column=3)
rmbtexibir = tkinter.Button(rmenu, text='Exibir',width=6, relief='groove', command=lambda:[shwConsulta(shwSFrame,shwFrame,'estudantes')]).grid(row=0,column=4)
rmbtfechar = tkinter.Button(rmenu, text='Fechar',width=6, relief='groove', command= lambda:[dc.con.close(), root.destroy()]).grid(row=0,column=5)

rmbtlimiter = tkinter.Label(rmenu, text='',bg='white').grid(row=0,column= 6, padx= 125)

rmbtFilterIcon = tkinter.PhotoImage(file = r'assets\\filter.png', master=rmenu).subsample(2,2)
rmbtFilter = tkinter.Button(rmenu, image= rmbtFilterIcon, command= lambda: tt.Window_filter('Cursos'), padx=0,width=14, height=14, relief='groove')
rmbtFilter.grid(row=0, column=7, sticky='w',padx=0) 

ccSFEntry1 = tkinter.Entry(rmenu, width=20, relief='solid' )#highlightthickness=2)
ccSFEntry1.grid(row=0, column=8, sticky='w', padx=3, pady=1)
ccSFbutton4 = tkinter.Spinbox(rmenu, values=('id', 'nome', 'matricula','senha' ),width=12)

rmbtSeachIcon = tkinter.PhotoImage(file = r'assets\\seach.png', master=rmenu).subsample(2,2)
ccSFbutton3 = tkinter.Button(rmenu, image= rmbtSeachIcon, command=lambda:[dc.seachCad(ccSFEntry1)] , padx=0,width=14, height=14, relief='groove')
ccSFbutton3.grid(row=0 , column= 9, sticky='w', padx=2)

#rmbtOthers = tkinter.Button(rmenu, text='opçoes',width=6, relief='groove', command= lambda:[tt.Window_filter('Cursos')]).grid(row=0,column=6, padx= 20)






#Frame do estudante
stdFrame = tkinter.Frame(root, height= 400 , width= 750, background='white')
stdSubframe1 = tkinter.Frame(stdFrame, width=25, height= 25, background='Black')
stdSubframe1.pack(fill= 'x', side= 'top', expand= False)
stdSubfLabel = tkinter.Label(stdSubframe1, text='Área dos Alunos', fg='white',bg='black', font=' 14')
stdSubfLabel.pack(side='left')
stdSubframe2 = tkinter.Frame(stdFrame, width=25, height= 25, background='Black')
stdSubframe2.pack(fill= 'x', side= 'top', expand= False)
stdSubf2Button1 = tkinter.Button(stdSubframe2, text='Adicionar', command= lambda:tt.Frame_Entry(stdFrame,'estudantes','S'), bg='black', fg='white', bd=0)
stdSubf2Button1.pack( side= 'left')
stdSubf2Button2 = tkinter.Button(stdSubframe2, text='excluir', command='', bg='black', fg='white', bd=0)
stdSubf2Button2.pack( side= 'left')
stdSL1 = tkinter.Label(stdSubframe2,padx=100, bg='black')
stdSL1.pack(side='left')
stdSubf2Entry1 = tkinter.Entry(stdSubframe2, width=25, background='black', relief= 'solid', fg='white', highlightbackground='white', highlightthickness= 1)
stdSubf2Entry1.pack(side='left')
stdSubf2Entry1.bind("<Return>", lambda eff: vc.EnterPressEntry(stdSubf2Entry1,'Estudantes', eff))
stdSubf2Button3 = tkinter.Button(stdSubframe2, text='Pesquisar', command= lambda:[dc.seachCad(stdSubf2Entry1,table='Estudantes')], bg='black', fg='white', bd=0)
stdSubf2Button3.pack( side= 'left')
nowFrame = stdFrame

# Frame do professor
tchFrame = tkinter.Frame(root, height= 400 , width= 750, background='white')
tchSubframe1 = tkinter.Frame(tchFrame, width=25, height= 25, background='Black')
tchSubframe1.pack(fill= 'x', side= 'top', expand= False)
tchSubfLabel = tkinter.Label(tchSubframe1, text='Área dos Professores', fg='white',bg='black', font=' 14')
tchSubfLabel.pack(side='left')
tchSubframe2 = tkinter.Frame(tchFrame, width=25, height= 25, background='Black')
tchSubframe2.pack(fill= 'x', side= 'top', expand= False)
tchSubf2Button1 = tkinter.Button(tchSubframe2, text='Adicionar', command= lambda:tt.Frame_Entry(tchFrame,'professores','P'), bg='black', fg='white', bd=0)
tchSubf2Button1.pack( side= 'left')
tchSubf2Button2 = tkinter.Button(tchSubframe2, text='excluir', command='', bg='black', fg='white', bd=0)
tchSubf2Button2.pack( side= 'left')
tchSL1 = tkinter.Label(tchSubframe2,padx=100, bg='black')
tchSL1.pack(side='left')
tchSubf2Entry1 = tkinter.Entry(tchSubframe2, width=25, background='black', relief= 'solid', fg='white', highlightbackground='white', highlightthickness= 1)
tchSubf2Entry1.pack(side='left')
tchSubf2Entry1.bind("<Return>", lambda eff: vc.EnterPressEntry(stdSubf2Entry1,'Estudantes', eff))
tchSubf2Button3 = tkinter.Button(tchSubframe2, text='Pesquisar', bg='black', fg='white', command= lambda:[dc.seachCad(tchSubf2Entry1,table = 'Professores')])
tchSubf2Button3.pack( side= 'left')

#Frame de exibição
shwFrame = tkinter.Frame(root)
sFlabel1 = tkinter.Label(shwFrame, text='Consultar.', font='Arial 12 bold')
sFlabel1.grid(column=0, row=0)
shwSFrame = tkinter.Frame(shwFrame,bg='black')
shwSFrame.grid(row= 2, column=1, stick='n')
sFRSpinbox = tkinter.Spinbox(shwSFrame, values= ('estudantes', 'professores'), command= lambda:[getchoosed(),shwConsulta(shwSFrame,shwFrame,choosed)],bg='black',fg='white', state='readonly',readonlybackground='black')
sFRSpinbox.grid(row=1, column=1,sticky='nw',padx=2,pady=4)
shIRF = tkinter.PhotoImage(file = r'assets\\-refresh.png', master=shwSFrame).subsample(2,2)
rfbutton = tkinter.Button(shwSFrame, image= shIRF,bg='black', relief='ridge', width=14,height=14, borderwidth=3, command= lambda: openFrame(shwFrame)).grid(row=1,column=0,padx=2, pady=2)
shwSFrame2 = tkinter.Frame(shwFrame)
shwSFrame2.grid(row=3, column=1,pady=10)
shwSFbutton2 = tkinter.Button(shwSFrame, text='Deletar',command=lambda:[getchoosed(),deleteCad(sFRSpinbox),shwConsulta(shwSFrame,shwFrame,choosed,modelo=0)], width=10, bg='white')#,state='disabled')
shwSFbutton2.grid(row=2, column=2, sticky='en', padx=10)


'''shwSFEntry1 = tkinter.Entry(shwSFrame2, width=20, relief='solid' )#highlightthickness=2)
shwSFEntry1.grid(row=0, column=1, sticky='se', padx=10)
shwSFbutton4 = tkinter.Spinbox(shwSFrame2, values=('id', 'nome', 'matricula','senha' ),width=12)
shwSFbutton4.grid(row=0, column=0, sticky='se') 
shwSFbutton3 = tkinter.Button(shwSFrame2, text='Pesquisar: ', command=lambda:seachCad(shwSFEntry1,shwSFrame2 ,1, sFRSpinbox, shwSFbutton4))
shwSFbutton3.grid(row=0 , column= 2, sticky='se')'''

print(shwSFrame2.winfo_parent)

#frame de cadastro de cursos



ccFrame = tkinter.Frame(root)
sccFlabel1 = tkinter.Label(ccFrame, text='  Cursos.  ', font='Arial 12 bold')
sccFlabel1.grid(column=0, row=0)
ccSFrame = tkinter.Frame(ccFrame,bg='black')
ccSFrame.grid(row= 2, column=1, stick='n')

ccSFrameA = tkinter.Frame(ccFrame,bg='black', width= 95 , height=273)
ccSFrameA.grid(row= 2, column= 2, sticky='n')#, padx=10, pady= 11)

ccFRSpinbox = tkinter.Spinbox(ccSFrame, values= ('cursos'), command= lambda:[getchoosed(),shwConsulta(ccSFrame,ccFrame, 'Cursos',2)],bg='black',fg='white', state='readonly',readonlybackground='black')
ccFRSpinbox.grid(row=1, column=1,sticky='nw', pady=4, padx=2)
ccIRF = tkinter.PhotoImage(file = r'assets\\-refresh.png', master=ccSFrame).subsample(2,2)
rfbutton = tkinter.Button(ccSFrame, image= ccIRF,bg='black', relief='ridge', width=14,height=14,borderwidth=3, command= lambda: openFrame(ccFrame)).grid(row=1,column=0,padx=2, pady=2)
ccSFrame2 = tkinter.Frame(ccFrame, bg='white')
ccSFrame2.grid(row=3, column=1,pady=10,sticky='w')

limitccSFrameA = tkinter.Label(ccSFrameA, text='',bg='black').grid(row=0, pady= 3)

ccINW = tkinter.PhotoImage(file = r'assets\\new.png', master=ccSFrame).subsample(2,2)
ccSFbutton4 = tkinter.Button(ccSFrameA, image= ccINW, compound= 'top' ,text='Novo', command=lambda:tt.Window_cadCurso(3), padx=20,width=20, height=30)
ccSFbutton4.grid(row= 1, column= 0, sticky='n', padx=10, pady= 0)

ccIDL = tkinter.PhotoImage(file = r'assets\\delete.png', master=ccSFrame).subsample(2,2)
ccSFbutton2 = tkinter.Button(ccSFrameA, image= ccIDL, compound= 'top', text='Deletar', state= btnCursoEnabled ,command=lambda:[deleteCad(ccFRSpinbox),shwConsulta(ccSFrame, ccFrame,'cursos',modelo='1a',tevent =2)], width=58,height= 35, bg='white')#,state='disabled')
ccSFbutton2.grid(row=2, column=0, sticky='n', padx=10, pady=5)


ccIED = tkinter.PhotoImage(file = r'assets\\edit.png', master=ccSFrame).subsample(2,2)
ccSFbutton5 = tkinter.Button(ccSFrameA, image= ccIED, compound= 'top', text='Editar', state= btnCursoEnabled ,command= lambda:vc.getSelection('cursos'), width=58,height= 35, bg='white')#,state='disabled')
ccSFbutton5.grid(row= 3, column= 0, sticky='n', padx=10, pady= 0)


ccICS = tkinter.PhotoImage(file = r'assets\\class.png', master=ccSFrame).subsample(2,2)
ccSFbutton6 = tkinter.Button(ccSFrameA, image= ccICS, compound= 'top' ,text='Classes', state= btnCursoEnabled, command=lambda:tt.Window_cadCurso(3), padx=20,width=20, height=30)
ccSFbutton6.grid(row= 4, column= 0, sticky='n', padx=10, pady= 5)

limitccSFrameB = tkinter.Label(ccSFrameA, text='',bg='black').grid(row=9, pady= 21)

'''ccIFT = tkinter.PhotoImage(file = r'assets\\filter.png', master=ccSFrame).subsample(2,2)
ccSFbutton4 = tkinter.Button(ccSFrame2, image= ccIFT, command= lambda: tt.Window_filter('Cursos'), padx=0,width=14, height=14, relief='groove')
ccSFbutton4.grid(row=0, column=0, sticky='sw',padx=0,) 

ccSFEntry1 = tkinter.Entry(ccSFrame2, width=20, relief='solid' )#highlightthickness=2)
ccSFEntry1.grid(row=0, column=1, sticky='sw', padx=3, pady=1)
ccSFbutton4 = tkinter.Spinbox(ccSFrame2, values=('id', 'nome', 'matricula','senha' ),width=12)

ccISH = tkinter.PhotoImage(file = r'assets\\seach.png', master=ccSFrame).subsample(2,2)
ccSFbutton3 = tkinter.Button(ccSFrame2, image= ccISH, command=lambda:[dc.seachCad(ccSFEntry1)] , padx=0,width=14, height=14, relief='groove')
ccSFbutton3.grid(row=0 , column= 2, sticky='sw', padx=2)'''








root.mainloop()

