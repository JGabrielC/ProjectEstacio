
import sqlite3
import pyodbc 
import pandas as pd
import tkinter as tk
import __main__ as mn
from defs.windowControl import *
import defs.windowControl as wc
import defs.toast as tt
import defs.varControl as vc
from warnings import filterwarnings



filterwarnings("ignore", category=UserWarning, message='.*pandas only supports SQLAlchemy connectable.*')


global con,cur 

def opendbOld():
    ''' Abre conexção com banco de dados
    '''
    global con, cur
    con = sqlite3.connect(r'mainbase.db')
    cur = con.cursor()

    return con, cur

def opendb():
    ''' Abre conexção com banco de dados
    '''
    global con, cur


    con = pyodbc.connect('DRIVER={Devart ODBC Driver for SQL Server};Server=JhonsComputer\MAINBASE;Database=ProjectEstacio;Port=1433;Integrated Security=true')
    cur = con.cursor()
    mn.con = con
    mn.cur = cur  

    return con, cur

def createdb(shwConsole = False): #databaseControl
    ''' Cria as tabelas no banco de dados, caso não existam
    '''

    opendb()
    try:
            
            cur.execute(""" 
                            CREATE TABLE estudantes
                            ( 
                                ID int PRIMARY KEY NOT NULL ,
                                Nome VARCHAR(40) NOT NULL, 
                                CPF VARCHAR(14) UNIQUE NOT NULL, 
                                Matricula VARCHAR(13) NOT NULL,
                                Senha INT NOT NULL
                            ) 
                        """)
            con.commit()
            found = cur.execute('Select * FROM estudantes')
            if found: print("table Estudantes criada com sucesso")
            else: print('Ouve algum erro ao tentar criar tabela Estudantes')
    except Exception as e:
        if shwConsole: print("A Tabela estudantes Já existe atualmente.") and print(e)
        


    try:

                    
        cur.execute(""" 
                        CREATE TABLE professores
                        ( 
                            id int PRIMARY KEY NOT NULL ,
                            nome VARCHAR(40) NOT NULL, 
                            cpf VARCHAR(14) UNIQUE NOT NULL, 
                            matricula VARCHAR(13) NOT NULL,
                            senha INT NOT NULL
                        ) 
                    """)
        
        con.commit()
        found = cur.execute('Select * FROM professores')
        if found: print("table professores criada com sucesso")
        else: print('Ouve algum erro ao tentar criar tabela professores')
    except Exception as e:
        if shwConsole: print("A Tabela professores Já existe atualmente.")and print(e)
        



    try:


        cur.execute(""" 
                        CREATE TABLE cursos
                        ( 
                            ID INT PRIMARY KEY NOT NULL,
                            nome VARCHAR(40) NOT NULL,  
                            CHoraria INT,
                            professor INT NOT NULL,
                            FOREIGN KEY (professor) REFERENCES professores(ID)

                        ) 
                    """)
        
        con.commit()
        found = cur.execute('Select * FROM professores')
        if found: print("table professores criada com sucesso")
        else: print('Ouve algum erro ao tentar criar tabela professores')
    except Exception as e:
        if shwConsole: print("A Tabela cursos Já existe atualmente.") and print(e)
        

       

    try:
                    
        cur.execute(""" 
                        CREATE TABLE classes
                        ( 
                            ID int not null,
                            cursoID int not null,
                            estudantesID int not null,
                            turno varchar(10) not null,
                            FOREIGN KEY (cursoID) REFERENCES cursos(ID),
                            FOREIGN KEY (estudantesID) REFERENCES estudantes(ID)
                        ) 
                    """)        
        con.commit()
        found = cur.execute('Select * FROM professores')
        if found: print("table professores criada com sucesso")
        else: print('Ouve algum erro ao tentar criar tabela professores')
    except Exception as e:
        if shwConsole: print("A Tabela classes Já existe atualmente.") and print(e)



    con.close()

def selecConsulta(table, modelo = 0, id= 0, aux= 'Nome'): # renomeado de shwsl()
    ''' seleciona os parametros da consulta para ser exibida na lista.
        @param table: table qual sera utilizada na consulta.
        @param modelo: estilo da exibição de consultas, 0: Padrão, -1: Filtrados por id, 1: classes, 2: Cursos , 3a Professor Minimizado
        @param id: Id que sera usado como restrição para consultar filtradas.
    '''
    
    global df
    opendb()
    if modelo == 0:
        df = pd.read_sql("""
                            SELECT * 
                            FROM %s 
                            ORDER BY ID ASC
                        
                        """ %(table),con)
    elif modelo == 1:
        df = pd.read_sql("""
                            SELECT cursos.Nome as 'Nome do Curso', cursos.Choraria as 'Carga Horaria', turno as Turno, professores.nome as Professor, estudantes.nome  
                            FROM classes
                            LEFT JOIN  estudantes on  classes.estudantesId = estudantes.id 
                            LEFT JOIN  Cursos on  classes.cursoID = Cursos.ID
                            LEFT JOIN  professores on  Cursos.professores = professores.id
                            ORDER BY classes.ID ASC

                        
                        """ ,con)

    elif modelo == 2: # renomeado de 2
        df = pd.read_sql("""
                            SELECT C.ID , C.Nome as 'Nome do Curso', Choraria as 'Carga Horaria', professores.nome as Professor
                            FROM cursos as C 
                            LEFT JOIN  professores on  C.professores = professores.id
                            ORDER BY C.ID ASC
                                
                        """ ,con)
        
    elif modelo == -1:
        df =pd.read_sql("""
                            SELECT * 
                            FROM %s 
                            WHERE Id = %s 
                            ORDER BY ID

                        """ %(table, id),con)
    elif modelo == '3a':
        df = pd.read_sql("""
                            SELECT id AS ID, nome AS Nome, matricula AS Matricula 
                            FROM professores 
                            ORDER BY id ASC
                        
                        """ ,con)
    elif modelo == '-1a':
        df= pd.read_sql("""
                            SELECT *
                            FROM %s
                            WHERE %s LIKE %s 
                            ORDER BY id ASC
                        """ %(table,aux,id) ,con)
    elif modelo == '-1b':
        df= pd.read_sql("""
                            SELECT *
                            FROM %s
                            WHERE %s %s %s 
                            ORDER BY id %s
                        """ %(mn.filter_cho, mn.filter_sel, mn.filter_shm, id, mn.filter_order ) ,con)
        
    #print(df)       
    con.close()
    return df

def listTables(table, drop = False):
    ''' Exibe se uma Table existe dentro do banco de dados, e seus tipos de informação
        @param table: Tabela que sera verificada
        @param drop: Caso verdadeiro apaga a tabela  
    '''
    opendb()

    t= ('classes', 'cursos', 'estudantes', 'professores')

    try:
        a=cur.execute("SELECT * FROM %s" %(table))
        print(a.description)
        print(a.fetchone())
        if drop:
            cur.execute("DROP TABLE classes" %(table))
            a=cur.execute("SELECT * FROM %s" %(table))
            if a: print('nao apagada')   
            else: print('apagada com sucesso')

        
    except Exception as e:
        print('table dont exist')
        print(e)
        
    
    con.close()
    
def editcad(table): # renomeado de editcad
    '''
    '''
    
    if table == 'cursos':
            
            nm = mn.bxname.get()
            cg = mn.spcg.get()          

            opendb()
            cur.execute("UPDATE cursos SET ID = ?, Nome = ?, cHoraria = ?, professores = ? WHERE id = %s" %(mn.ni),(mn.ni,nm,cg,mn.pmt))
            con.commit()
            cur.execute("SELECT * FROM cursos WHERE ID = %s" %(mn.ni))
            founded = cur.fetchone()
            con.close()
            if founded:
                wc.shwConsulta(mn.ccSFrame, mn.ccFrame,'cursos',modelo=2)
                tt.toast.destroy()                
                tt.Mensage(0, 'O curso foi editado com sucesso.')        
            else:
                tt.Mensage(2, 'Nao foi possivel editar o curso. \n Ouve algum erro.')

def deleteCad(table): #databaseControl renomeado de dellstd
    ''' Deleta o cadastro do banco de dados
        @param 
    '''

    tt.Mensage(1,' Os Cadastros selecionados serão apagados permanentemente, deseja continuar ?')
    mn.root.wait_window(mn.toast)

    if mn.conf:
        table= table.get()
        opendb()
        #curI = shwSFtlist.focus()
        for i in range(len(mn.shwSFtlist.selection())):
            curI = mn.shwSFtlist.selection()[i]
            #curI = ("'"+curI+"'")
            #print(cur.execute("""select from curso where id = %s""") %(curI))
            cur.execute("DELETE FROM %s WHERE id = %s" %(table, curI))
        con.commit()
        con.close()
        mn.shwSFtlist.update()
    
    else: 
        tt.Mensage(0,'A excluão foi cancelada')

def newCad(datab, typ): #databaseControl renomeado de newStd
        ''' cria um novo castro no banco de dados

            @param datab: banco de dados do cadastro
            @param typ: o tipo de cadastro, sendo S: estudantes , P: professor, C: curso 
        '''
        if typ == 'C': # CURSOS
            nm = mn.bxname.get()
            cg = mn.spcg.get()            
            vc.setnewID(datab)
            vc.setnewMat(datab,typ)

            opendb()
            cur.execute("INSERT INTO cursos (ID, Nome, cHoraria, Professores) VALUES (?, ?, ?, ?)", (mn.nid, nm, cg, mn.pmt))
            con.commit()
            cur.execute("SELECT id FROM cursos WHERE id = %s" %(mn.nid))
            founded = cur.fetchone()
            con.close()
            
            if founded:
                vc.setnewID(datab)
                mn.lbID.config(text='ID: %s'%(mn.nid))
                mn.lbSprof.config(text='Professor: %s'%(mn.pmtmask))
                mn.lbID.update()
                mn.lbSprof.update()
                mn.ccSFrame.pack_forget()
                wc.shwConsulta(mn.ccSFrame, mn.ccFrame,'cursos',modelo=2)                
                tt.Mensage(0, 'O curso foi cadastrado com sucesso.')

                
            else:
                tt.Mensage(2, 'Nao foi possivel criar o cadastro do curso. \n Ouve algum erro.')
        
        else:       
            stdname = mn.stdBxname.get()
            stdmtr = mn.stdBxmtr.get()
            stdid = mn.stdBxid.get()
            
            vc.setnewID(datab)
            vc.setnewMat(datab,typ)
            opendb()
            cur.execute("INSERT INTO %s (id, nome, cpf, matricula, senha) VALUES (?, ?, ?, ?, ?)" %(datab), (mn.nid, stdname + " ", stdmtr, vc.mmt ,stdid))
            con.commit()
            cur.execute("SELECT id FROM %s WHERE id = %s" %(datab,mn.nid))
            founded = cur.fetchone()
            con.close()
            if founded:
                vc.setnewID(datab)
                vc.setnewMat(datab,typ)

                mn.stdLii.config(text='ID: %s'%(mn.nid))
                mn.stdLmmt.config(text='Matricula: %s'%(mn.mmt))
                
                mn.stdBxname.delete(0, tk.END)
                mn.stdBxid.delete(0, tk.END)
                mn.stdBxmtr.delete(0, tk.END)

                mn.stdLii.update()
                mn.stdLmmt.update()


                tt.Mensage(0, 'O %s foi cadastrado com sucesso' %(datab))
                
            else:
                tt.Mensage(2, 'Nao foi possivel criar o cadastro do %s. \n Ouve algum erro.' %(datab))

def seachCad(entry, frame ='', modo= 'Mensage', table= 0, filt= 0): #databaseControl renamed SeachStd
    ''' pesquisa por um dado dentro do banco.
        @param typ: tipo de pesquisa : 0 basica, com saida em toast; 1 complexa, com filtos, saidas no menu de exibição.
        @param frame: Entry qual sera buscado. 
        @param datab: base qual sera pesquisada; EX : estudantes, professores, Cursos
        @param filt: filtro selecionado
    '''
    
    if modo == 'Mensage':
        opendb()   
        stdget = entry.get()
        stdget1 = stdget
        if stdget1.isnumeric():
            print()
            pass
        else:
            stdget1 = ("'% "+stdget+" %'")
            
        cur.execute("""
                            SELECT *
                            FROM %s
                            WHERE %s %s %s 
                            ORDER BY id %s
                        """ %(mn.filter_cho, mn.filter_sel, mn.filter_shm, stdget1, mn.filter_order ))
        founded = cur.fetchall()
        con.close()
        if founded:
            tt.Mensage(3, mn.filter_cho, aux= stdget)
        else:
            tt.Mensage(0,'O Cadastro não foi encontrado; \n tente verificar se foi escrito corretamente.')
    
                    
    elif modo == 1:
    
        #closeFrame(rsFrame)
        opendb()
        stdget = entry.get()
       
        if stdget.isnumeric():
            pass
        else:
            stdget = ("'%"+stdget+"%'")
        
        try:    
            table= table.get()
        except:
            pass
       
        try:
            filt = filt.get()
        except:
            pass

        wc.shwConsulta(frame, table= table ,modelo= '-1b', id= stdget , hg=3, aux= filt)
    else:
        tt.Mensage(2,'tipo de pesquisa incorreto')
