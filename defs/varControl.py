from defs.databaseControl import *
from defs.windowControl import *
from datetime import date
import defs.windowControl as wc 
import defs.databaseControl as dc
import defs.toast as tt


import __main__ as mn
global nid,pmtmask

def habCBnt(event): 
    ''' habilita botões de edição
    '''

    global selection,ccSFbutton2,ccSFbutton5,ccSFbutton6
    dc.opendb()
    curI = wc.shwSFtlist.focus()
    dc.cur.execute("SELECT id FROM Cursos WHERE id LIKE ?" ,(curI))
    selection = dc.cur.fetchall()
    selection = selection[0]


    btnCursoEnabled = 'active'
    
    mn.ccSFbutton2.config(state=btnCursoEnabled)
    mn.ccSFbutton5.config(state=btnCursoEnabled)
    mn.ccSFbutton6.config(state=btnCursoEnabled)
    mn.ccSFbutton2.update()
    mn.ccSFbutton5.update()       
    mn.ccSFbutton6.update()

def formatEntry(frame, modo, event = None):
    '''
        formata a entry
        @param frame: box qual sera formatada
        @param modo: 0 caso a formatação seja de cpf, 1 caso a formatação seja de apenas letras- Primeira Maiuscula por palavra, 2 para caso seja apenas numeros
    '''
    

    if event.keysym.lower() == "backspace": return
    
    if modo == 0: 
        text = frame.get().replace(".", "").replace("-", "")[:11]  
        new_text = "" 
    elif modo == 1: 
        text = frame.get().title()[:40]  
        new_text = ""
    elif modo == 2: 
        text = frame.get()[:4]
        new_text = ""


    for index in range(len(text)):
        if modo == 0:
        

            
            if not text[index] in "0123456789": continue
            if index in [2, 5]: new_text += text[index] + "."
            elif index == 8: new_text += text[index] + "-"
            else: new_text += text[index]
        elif modo == 1:


                        
            if text[index] in "0123456789": continue
            else: new_text += text[index]
        elif modo == 2:


            if not text[index] in "0123456789": continue
            else: new_text += text[index] 

    frame.delete(0, "end")
    frame.insert(0, new_text)

    return

def EnterPressEntry(frames, tables, event= None):
    dc.seachCad(frames,table= tables)    

def setProfMask(event): #c renomeada de SLlist
    '''cria uma mascara por nome para a id da table professores.
    '''
    global curI,subf,pmt, pmtmask,lbSprof
    
    dc.opendb()
    curI = mn.shwSFtlist.focus()
    dc.cur.execute("SELECT id FROM professores WHERE id LIKE ?" ,(curI))
    pmt = dc.cur.fetchone()
    pmt = pmt[0]
    mn.pmt= pmt

    dc.cur.execute("SELECT nome FROM professores WHERE id LIKE ?" ,(curI))
    pmtmask = dc.cur.fetchone()
    pmtmask = pmtmask[0]
    mn.lbSprof.config(text='Professor: %s'%(pmtmask))
    mn.lbSprof.update()
    mn.subf.pack_forget()
    #dc.con.close()
    return pmt, pmtmask

def getchoosed(): # renomeada de shwtyp
    ''' altera variavel choosed 
    '''
    global choosed,val
    choosed = mn.sFRSpinbox.get()
    mn.choosed = choosed
    return choosed

def setnewID(table): # renomeado de newId
    ''' Sistema para Gerenciamento da variavel nid; que é responsavel pelo ID de um novo cadastro
        @param table: Tabela que sera gerenciada por nid
    '''


    dc.opendb()
    
    tempNid = len(dc.cur.execute('SELECT * from %s' %(table)).fetchall())

    tempNid += 1
    

    for i in range(tempNid):
        founded = dc.cur.execute("SELECT * FROM %s WHERE ID = %s" %(table, i))
        founded = founded.fetchone()        
        if founded:
            pass
        else:
            nid= i
            mn.nid = nid
            break
    
    dc.con.close()
    return nid, mn.nid

def setnewMat(table, typ): # renomeado de ftMat
    '''
    cria um numero de matricula 
    @param datab: table que sera utilizada 
    @param typ: digito inicial da matricula podendo ser S: estudantes ou T: professor ou C: curso 
    '''

    global mmt,nid

    setnewID(table)
    nid = mn.nid
    sY = date.today().year
    sM = date.today().month
    nnid = str(nid).zfill(6)
    sY = str(sY).zfill(2)
    mmt= str(typ)+str(sY)+str(sM)+nnid    

    return mmt

def getSelection(table):

    global selection,pmt,ni, pm
    
    dc.opendb()
    curI = mn.shwSFtlist.focus()

    dc.cur.execute("SELECT * FROM %s WHERE id = %s" %(table, curI))
    selection = dc.cur.fetchone()
    s= dc.cur.description
    selection = list(selection)
    i=0

    tt.Window_cadCurso(editing=True) 

    for row in s:
            if table == 'cursos':
                if row[0] == 'Nome': 
                    mn.bxname.insert(0,selection[i])
                    mn.bxname.update()
                if row[0] == 'CHoraria':
                    mn.spcg.delete(0,'end')
                    mn.spcg.insert(0,selection[i])
                    mn.spcg.update()
                if row[0] == 'ID':

                    nid = selection[i]
                    ni = nid
                    mn.ni = ni
                    mn.lbID.grid_forget()
                    mn.lbID.config(text='ID: %s'%(ni))
                    mn.lbID.grid(row=0, column=0, pady=5, sticky= 'w')
                if row[0] == 'Professores':
                    
                    dc.opendb()
                    cc = dc.cur.execute("SELECT nome FROM professores WHERE id = %s" %(selection[i]))
                    mn.pmt=selection[i]
                    pmtmask = cc.fetchone()
                    pmtmask = pmtmask[0]
                    mn.pmtmask = pmtmask
                    mn.lbSprof.grid_forget()
                    mn.lbSprof.config(text='Professor: %s'%(mn.pmtmask))
                    mn.lbSprof.grid(row=0, column=1, pady=5, sticky= 'w')    


                i= i+1

    
    #dc.con.close()        
    #return nid, pmt, ni, pm