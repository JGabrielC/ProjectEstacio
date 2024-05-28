import __main__ as mn
import tkinter as tk
from defs.varControl import *
from defs.windowControl import *
from defs.databaseControl import *
import defs.varControl as vc



def Mensage(modo,  mensage = '', table= '', aux= ''):
    ''' Cria um novo popup para exibição de mensagens
        @param modo: tipo de toast que sera usado; 0 ou Msg: mensagem, 1 ou Confirm: Confirmação, 2 ou Erro: Erro.
        @param mensage: Mensagem qual sera exibida
        @param table: table qual sera utilizada no filtro
    
    '''
    global toast

    if modo == 0 or modo == 'msg':
        toast = tk.Toplevel()
        toast.title('MENSAGEM!')
        toast.geometry('220x110')
        toast.resizable(False, False)
        toast.focus_force()
        toast.grab_set()
        
        #tstwFrame = tk.Frame(toast,width=200,height=65,bg='black').pack()
        tsticon = tk.PhotoImage(file= r'assets/-tstMsg.png', master=toast)
        tstbticon = tk.PhotoImage(file= r'assets/ok.png', master=toast).subsample(2,2)
        toast.iconphoto(False,tsticon) 

        tstwText = tk.Text(toast, height=4, wrap= 'word')
        tstwText.insert(1.0, mensage)
        tstwText.configure(state='disabled')
        tstwText.tag_configure("center", justify='center')
        tstwText.tag_add("center", 1.0, "end")
        tstwText.pack(expand= False, fill='x')

        tstwButton = tk.Button(toast, width=20, height=20, image= tstbticon, relief= 'solid', command= toast.destroy)
        tstwButton.pack(pady=5)
        


        toast.mainloop()

    elif modo == 1 or modo == 'confirm':

        conf= ''
        toast = tk.Toplevel()
        toast.title('CONFIRMAÇÃO!')
        toast.geometry('270x120')
        toast.resizable(False,False)
        toast.focus_force()
        toast.grab_set()
        tsticon = tk.PhotoImage(file= r'assets/-tstConf.png', master=toast)
        toast.iconphoto(False,tsticon) 
        tstbticon1 = tk.PhotoImage(file= r'assets/ok.png', master=toast).subsample(2,2)
        tstbticon2 = tk.PhotoImage(file= r'assets/cancel.png', master=toast).subsample(2,2)
        



        tstwText = tk.Text(toast, height=4, wrap= 'word', relief='solid', borderwidth=5)
        tstwText.insert(1.0, mensage, 'center')
        tstwText.configure(state='disabled')
        tstwText.tag_configure("center", justify='center')
        tstwText.tag_add("center", 1.0, "end")
        tstwText.pack(expand= False, fill='x')

        #tstwLabel = tk.Label(toast, text='deseja confirmar ?', font='Arial 12 bold').pack(side='top')
        tstwButton1 = tk.Button(toast, image= tstbticon2, padx=5, width=20, height=20, relief='solid', command= lambda:subdef_Con(False))
        tstwButton1.pack(side='left', pady=10, padx= 20)
        tstwButton1.image = tstbticon1
        tstwButton2 = tk.Button(toast, image= tstbticon1, padx=20, width=20, height=20, relief='solid', command=lambda:subdef_Con(True))
        tstwButton2.pack(side='right', pady=10, padx= 20)
        tstwButton2.image = tstbticon2

        #toast.mainloop()
        
        #toast.wait_window()
        
        mn.toast = toast
        return  conf, toast
    
    elif modo == 2 or modo =='erro':


        toast = tk.Toplevel()
        toast.title('ERRO!')
        toast.geometry('220x110')
        toast.resizable(False, False)
        toast.focus_force()
        toast.grab_set()
        tsticon = tk.PhotoImage(file= r'assets/-tstErro.png', master=toast)
        tstbticon = tk.PhotoImage(file= r'assets/ok.png', master=toast).subsample(2,2)
        toast.iconphoto(False,tsticon) 


        tstlabel= tk.Label(toast, text='Algo deu errado.')
        tstlabel.pack()
        tstwText = tk.Text(toast, height=3,width= 4, wrap= 'word')
        tstwText.insert(1.0, 'Detalhes: %s '%(mensage))
        tstwText.configure(state='disabled')
        tstwText.tag_configure("center", justify='center')
        tstwText.tag_add("center", 1.0, "end")
        tstwText.pack(expand= False, fill='x')
        tstwButton = tk.Button(toast, width=20, height=20, image= tstbticon, relief= 'solid', command= lambda:[toast.destroy()]).pack(pady=2)

        toast.mainloop() 

    elif modo == 3 or modo == 'pesquisa':
        
        toast = tk.Toplevel()
        toast.title('Resultado da Pesquisa')
        toast.geometry('477x138')
        toast.resizable(False, False)
        toast.focus_force()
        toast.grab_set()
        tsticon = tk.PhotoImage(file= r'assets/-seach.png', master=toast)
        tstbticon = tk.PhotoImage(file= r'assets/ok.png', master=toast).subsample(2,2)
        toast.iconphoto(False,tsticon) 

        tstMFrame = tk.Frame(toast,bg='black')
        tstMFrame.pack()
        tstLabel1 = tk.Label(toast, text= ' %s encontrados: ' %(table)).pack(side= 'top')
        tstwButton = tk.Button(toast, image=tstbticon, command= toast.destroy).pack(side='bottom')
        if aux.isnumeric(): pass 
        else: aux= "'%"+aux+"%'"
        wc.shwConsulta(tstMFrame, '', table,modelo= '-1b', id= aux , hg=3)

        toast.mainloop()

def Window_cadCurso(editing= False): # tstMensage(3)
        ''' Cria a Janela de cadastro de Cursos
            @param editing: Caso seja uma edição habilitar com True 
        ''' 

        global toast, ProfessorID, ProfessorMask
        mn.professorMask = ''

        toast = tk.Toplevel()
        toast.title('Cadastro de Curso')
        toast.geometry('290x260')
        toast.resizable(False, False)
        tsticon = tk.PhotoImage(file= r'assets/-new.png')
        
        toast.iconphoto(False, tsticon)

        setnewID('cursos')

        toastFrame = tk.Frame(toast, bg='white')
        toastFrame.pack()
        
        lbname = tk.Label(toastFrame, text="Nome do Curso: ").grid(row= 1, column=0, pady= 5,sticky='w') 
        bxname = tk.Entry(toastFrame, width= 25, borderwidth=1, relief= 'groove' , bg="white")
        bxname.grid(row= 1, column=1, pady= 5)
        bxname.bind("<KeyRelease>", lambda eff: formatEntry(bxname, 1, eff)) 
        lbID = tk.Label(toastFrame, text=" ID: %s" %(mn.nid))
        lbcg = tk.Label(toastFrame, text='Carga Horaria: ').grid(row=2, column=0, pady=5, sticky= 'w')
        spcg = tk.Spinbox(toastFrame, from_=0, to= 10000, increment=10, width=6, relief='groove')
        spcg.grid(row=2, column=1, pady=5, sticky='e')
        btSprof = tk.Button(toastFrame, text='Selecionar Professor',command= lambda:wc.shwConsulta(subf,subf,'professores',modelo='3a',tevent=1,hg=5)).grid(row=3, column=0,padx=5)
        lbSprof = tk.Label(toastFrame, text='Professor: %s'%(mn.pmtmask))#.grid(row=3, column=2, sticky='w', padx=45)
        subf = tk.Frame(toast, width= 290, height= 60, bg='light gray')#.pack()#grid(row=4, column=0)
        if editing == True: btconf = tk.Button(toastFrame,text='confirmar', command= lambda:[dc.editcad('cursos')]).grid(row=3, column=1, pady=5)
        else : btconf = tk.Button(toastFrame,text='confirmar', command= lambda:dc.newCad('cursos','C')).grid(row=3, column=1, pady=5)
        
        lbID.grid(row=0, column=0, pady=5, sticky= 'w')
        lbSprof.grid(row=0, column=1, pady=5, sticky= 'w')

        mn.bxname = bxname
        mn.lbID = lbID
        mn.spcg = spcg
        mn.lbSprof = lbSprof
        mn.subf = subf

def Window_editBasicCad(datab, typ): # tstMensage(4) Necessario Revisao
        ''' Tela de edição 
        '''

        global selection
        toast = tk.Tk()
        toast.title('Editar Cadastro')
        toast.geometry('300x200')
        toast.resizable(False, False)
        tsticon = tk.PhotoImage(file= r"assert/-edit.png")
        toast.iconphoto(False, tsticon)


            
        opendb()
        curI = shwSFtlist.focus()
        cur.execute("SELECT id FROM %s WHERE id = %s" %(datab, curI))
        selection = cur.fetchall()
        selection = selection[0]
        print(selection)
        #shwsl(datab,-1,1)
        con.close()


        setnewID(datab)
        setnewMat(datab,typ)
        toastLname = tk.Label(toast, text="Nome :" , background= "white", font= "Inder 12")
        toastLname.grid(row= 0, column= 0, pady= 2, stick='w')
        toastBxname = tk.Entry(toast, width=20, background='white', borderwidth= 3, relief= 'solid')
        toastBxname.grid(row= 0, column= 1, pady= 2)
        toastBxname.bind("<KeyRelease>", lambda eff: formatEntry(stdBxname, 1, eff))
        toastLcpf = tk.Label(toast, text="CPF :" , background= "white", font= "Inder 12")
        toastLcpf.grid(row= 1, column= 0, pady= 2, stick='w')
        toastBxcpf = tk.Entry(toast, width=20, background='white', borderwidth= 3, relief= 'solid')
        toastBxcpf.grid(row= 1, column= 1, pady= 2)
        toastBxcpf.bind("<KeyRelease>", lambda eff: formatEntry(stdBxmtr, 0, eff))
        toastLpw = tk.Label(toast, text="senha :" , background= "white", font= "Inder 12")
        toastLpw.grid(row= 2, column= 0, pady= 2, stick='w')
        toastBxpw = tk.Entry(toast, width=20, background='white', borderwidth= 3, relief= 'solid')
        toastBxpw.grid(row= 2, column= 1, pady= 2)
        toastBxpw.bind("<KeyRelease>", lambda eff: formatEntry(stdBxid, 2, eff)) 
        toastGbutton1 = tk.Button(toast, text='Cancelar', command= lambda:[toastBxname.delete(0, tk.END),toastLcpf.delete(0, tk.END),toastBxpw.delete(0, tk.END), closeFrame(mn.stdFnew)] )
        toastGbutton1.grid(row= 3, column= 0, stick='w', padx= 10)
        toastGbutton2 = tk.Button(toast, text='Confirmar', command= lambda:[dc.newCad(datab,typ)])
        toastGbutton2.grid(row= 3, column= 1, padx= 40)
        toastLid = tk.Label(toast, text='ID: %s'%(nid) )
        toastLid.grid(row= 0, column= 2, padx= 50, pady= 2)
        toastLmtr = tk.Label(toast, text='Matricula: %s'%(vc.mmt) )
        toastLmtr.grid(row=1 , column=2, padx= 50, pady= 2)
        toastGbutton3 = tk.Button(toast, text='Cursos', command= lambda:[])
        toastGbutton3.grid(row = 2, column=2, padx=50, pady = 2)


        #toast.mainloop()
        return

def Frame_Entry(self,datab,typ): #interfaces renomeado de EntryFrame
    ''' abre o Frame de cadastro 
    
        @param self: O frame a qual pertence.
        @param datab: base de dados utilizada
        @param typ: o tipo de cadastro, sendo S: estudantes , P: professor

    ''' 
    global stdBxname, stdBxmtr, stdBxid,nid, stdLmmt, stdLii

    setnewID(datab)
    setnewMat(datab,typ)
    
    stdFnew = tk.Frame(self, width= 725, height= 400, bg= 'white')
    stdFnew.pack(fill='both', expand=True)
    stdLname = tk.Label(stdFnew, text="Nome :" , background= "white", font= "Inder 12")
    stdLname.grid(row= 0, column= 0, pady= 2, stick='w')
    stdBxname = tk.Entry(stdFnew, width=20, background='white', borderwidth= 3, relief= 'solid')
    stdBxname.grid(row= 0, column= 1, pady= 2)
    stdBxname.bind("<KeyRelease>", lambda eff: formatEntry(mn.stdBxname, 1, eff))
    stdLmtr = tk.Label(stdFnew, text="CPF :" , background= "white", font= "Inder 12")
    stdLmtr.grid(row= 1, column= 0, pady= 2, stick='w')
    stdBxmtr = tk.Entry(stdFnew, width=20, background='white', borderwidth= 3, relief= 'solid')
    stdBxmtr.grid(row= 1, column= 1, pady= 2)
    stdBxmtr.bind("<KeyRelease>", lambda eff: formatEntry(stdBxmtr, 0, eff))
    stdLid = tk.Label(stdFnew, text="senha :" , background= "white", font= "Inder 12")
    stdLid.grid(row= 2, column= 0, pady= 2, stick='w')
    stdBxid = tk.Entry(stdFnew, width=20, background='white', borderwidth= 3, relief= 'solid')
    stdBxid.grid(row= 2, column= 1, pady= 2)
    stdBxid.bind("<KeyRelease>", lambda eff: formatEntry(stdBxid, 2, eff)) 
    stdGbutton1 = tk.Button(stdFnew, text='Cancelar', command= lambda:[mn.stdBxname.delete(0, tk.END),mn.stdBxid.delete(0, tk.END),mn.stdBxmtr.delete(0, tk.END), stdFnew.destroy()])#wc.closeFrame(mn.stdFnew)] )
    stdGbutton1.grid(row= 3, column= 0, stick='w', padx= 10)
    stdGbutton2 = tk.Button(stdFnew, text='Confirmar', command= lambda:[dc.newCad(datab,typ)])
    stdGbutton2.grid(row= 3, column= 1, padx= 40)
    stdLii = tk.Label(stdFnew, text='ID: %s'%(mn.nid) )
    stdLii.grid(row= 0, column= 2, padx= 50, pady= 2)
    stdLmmt = tk.Label(stdFnew, text='Matricula: %s'%(vc.mmt) )
    stdLmmt.grid(row=1 , column=2, padx= 50, pady= 2)
    stdGbutton3 = tk.Button(stdFnew, text='Cursos', command= lambda:[])
    stdGbutton3.grid(row = 2, column=2, padx=50, pady = 2)

    mn.stdBxname = stdBxname
    mn.stdBxmtr = stdBxmtr
    mn.stdBxid = stdBxid
    mn.stdLmmt = stdLmmt
    mn.stdLii = stdLii
    mn.stdFnew = stdFnew

def Window_filter(table= ''):
        
        global tstCXBox

        toast = tk.Toplevel()
        toast.title('Filtros')
        toast.geometry('205x310')
        toast.resizable(False, False)
        toast.focus_force()
        toast.grab_set()
        
        #tstwFrame = tk.Frame(toast,width=200,height=65,bg='black').pack()
        tsticon = tk.PhotoImage(file= r'assets/-filter.png', master=toast)
        tstbticon = tk.PhotoImage(file= r'assets/ok.png', master=toast).subsample(2,2)
        toast.iconphoto(False,tsticon)


        
        tstFramel1 = tk.Frame(toast)
        tstFramel1.pack(fill='x')
        tstLabel1 = tk.Label(tstFramel1, text='Metodo de pesquisa')
        tstLabel1.pack(side= 'left')
        tstFrame1 = tk.Frame(toast, width=200, height=2)
        tstFrame1.pack(fill='x', expand=False)

        methodo = tk.StringVar()

        tstCBox1 = tk.Checkbutton(tstFrame1,text= 'Literal', onvalue = '=', variable= methodo)
        tstCBox1.grid(row=1, column=0, padx=5, pady= 5)
        tstCBox1.config(command= lambda: subdef_getShm(tstCBox1))
        tstCBox2 = tk.Checkbutton(tstFrame1,text= 'Aproximado', onvalue = 'LIKE',variable= methodo)
        tstCBox2.grid(row=1, column= 1, padx= 20, pady= 5)
        tstCBox2.config(command= lambda: subdef_getShm(tstCBox2))

        if mn.filter_shm == 'LIKE':
            tstCBox1.deselect()
            tstCBox2.select()
        else:
            tstCBox2.deselect()
            tstCBox1.select()

        tstSeparator = tk.ttk.Separator(toast, orient='horizontal').pack(fill='x')
        tstFramel2 = tk.Frame(toast)
        tstFramel2.pack(fill='x')
        tstlabel3 = tk.Label(tstFramel2, text= 'Table a pesquisar').pack(side= 'left')

        tstFrame2 = tk.Frame(toast)
        tstFrame2.pack()

        select = tk.IntVar(value= 1)

        

        tstCBox3 = tk.Checkbutton(tstFrame2, text='Estudantes', onvalue = 'Estudantes', variable= select)
        tstCBox3.grid(row=1, column=0, padx=1, pady= 5, sticky= 'w')
        tstCBox3a = tk.Checkbutton(tstFrame2, text='Professores', onvalue = 'Professores', variable= select)
        tstCBox3a.grid(row=2, column=0, padx=1, pady= 5, sticky= 'w')
        tstCBox4 = tk.Checkbutton(tstFrame2, text='Cursos', onvalue = 'Cursos', variable= select)
        tstCBox4.grid(row=1, column=1, padx=1, pady= 5, sticky= 'w')
        tstCBox5 = tk.Checkbutton(tstFrame2, text='Classes', onvalue = 'Classes', variable= select)
        tstCBox5.grid(row=2, column=1, padx=1, pady= 5, sticky= 'w')

        tstCBox3.config(command= lambda:subdef_EntryUpdate(mode= 'Estudantes'))
        tstCBox3a.config(command= lambda:subdef_EntryUpdate(mode= 'Professores'))
        tstCBox4.config(command= lambda:subdef_EntryUpdate(mode= 'Cursos'))
        tstCBox5.config(command= lambda:subdef_EntryUpdate(mode= 'Classes'))

        if mn.filter_cho == 'Cursos':
            tstCBox4.select()
        elif mn.filter_cho == 'Classes':
            tstCBox5.select()
        else:
             tstCBox3.select()
        cbxc = tk.StringVar()


        tstSeparator = tk.ttk.Separator(toast, orient='horizontal').pack(fill='x',pady= 10)
        tstFramel3 = tk.Frame(toast)
        tstFramel3.pack(fill='x')

        tstLabel2 = tk.Label(tstFramel3,text='Atributo :').pack(side='left')

        tstCXBox = tk.ttk.Combobox(toast, textvariable=cbxc, values= mn.cbxvar, state= 'readonly')
        tstCXBox.pack()
        tstCXBox.bind("<<ComboboxSelected>>", subdef_getSel)
        tstCXBox.current(mn.filter_cbxstate)
        mn.tstCXBox = tstCXBox
        mn.cbxc = cbxc

        tstSeparator = tk.ttk.Separator(toast, orient='horizontal').pack(fill='x',pady= 10)
        tstFramel4 = tk.Frame(toast)
        tstFramel4.pack(fill='x')

        tstLabel2 = tk.Label(tstFramel4,text='Ordernado por').pack(side='left')
        
        
        select2= tk.StringVar()

        tstFrame3 = tk.Frame(toast, width=200, height=22)
        tstFrame3.pack(fill= 'both', side= 'bottom')
        tstwButton = tk.Button(tstFrame3, width=20, height=20, image= tstbticon, relief= 'solid', command= toast.destroy)
        tstwButton.grid(row= 1, column= 2, sticky= 'e', padx=2 , pady= 1)#pack(side='right')
        
        tstCBox6 = tk.Checkbutton(tstFrame3, text='Cres', onvalue = 'ASC', variable= select2)
        tstCBox6.grid(row=0, column=0, padx=25, pady= 0)

        tstCBox7 = tk.Checkbutton(tstFrame3, text='Decres', onvalue = 'DESC', variable= select2)
        tstCBox7.grid(row=0, column=1, padx=5, pady= 0)
        tstCBox6.config(command= lambda:subdef_getorder(tstCBox6))
        tstCBox7.config(command= lambda:subdef_getorder(tstCBox7))

        if mn.filter_order == 'DESC':
            tstCBox7.select()
        else:
            tstCBox6.select()

        

        toast.mainloop()
        


#SUBFUNÇÕES 
def subdef_Con(sel = bool):
    ''' Subfução, não deve ser utilizada fora do ambiente
        altera variavel tconf 
    '''
    global tconf

    tconf = sel
    mn.conf = tconf
    toast.destroy()
    return tconf

def subdef_EntryUpdate(mode= ''):
    mn.filter_cho= mode
    
    if mode == 'Estudantes' or mode == 'Professores':
        mn.cbxvar = ('ID', 'Nome', 'CPF', 'Matricula')
        tstCXBox.config(value = mn.cbxvar)
        tstCXBox.update()

            
    elif mode == 'Cursos':
        mn.cbxvar = ('ID', 'Nome', 'Professores')
        tstCXBox.config(value = mn.cbxvar)
        tstCXBox.update()        


    elif mode == 'Classes':
        
        mn.cbxvar = ('ID', 'ID do Curso', 'ID do Estudante', 'Turno')
        tstCXBox.config(value = mn.cbxvar)
        tstCXBox.update()          
            
def subdef_getShm(frame):
        filter_shm = frame.cget("onvalue")
        mn.filter_shm = filter_shm

def subdef_getorder(frame):
        filter_order = frame.cget("onvalue")
        mn.filter_order = filter_order

def subdef_getSel(event):
    sel = tstCXBox.get()
    if sel == 'ID':
         mn.filter_cbxstate = 0
    elif sel == 'Nome':
         mn.filter_cbxstate = 1
    elif sel == 'CPF':
         mn.filter_cbxstate = 2
    elif sel == 'Matricula':
         mn.filter_cbxstate = 3
    elif sel == 'ID do Curso':
         mn.filter_cbxstate = 1
         sel= "cursoID"
    elif sel == 'ID do Estudante':
         mn.filter_cbxstate = 2
         sel= 'estudantesID'
    elif sel == 'Turno':
         mn.filter_cbxstate = 3
    elif sel == 'Professor':
         mn.filter_cbxstate = 2

    mn.filter_sel = sel
     