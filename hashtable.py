class No:
    def __init__(self,idNo,ListData):
        self.idNo=idNo
        self.ListData=ListData
 
    def getIdNo(self):
        return self.idNo

    def setIdNo(self,newId):
        self.idNo=newId
        
    def getListData(self):
        return self.ListData

    def setListData(self,novaLista):
        self.ListData=novaLista

class HashTable:
    def __init__(self,funcao,N):
        self.funcao=funcao
        self.table=[]
        for i in range(N):
            self.table.append([])
        
    def insert(self,no):
        id_no=no.getIdNo()
        Dad=no.getListData()
        Pos=self.funcao(id_no)
        self.table[Pos].append(Dad)

    def printNo(self):
        return self.table

    def deleteno(self,IDNoh):
        Posi=self.funcao(IDNoh)
        if Daw!="None" and Daw!=[]:
            self.table[Posi]=[]
        else:
            return ""

    def printData(self,IDNoh):
        Posi=self.funcao(IDNoh)
        Daw=self.table[Posi][0]

        if Daw!="None" and Daw!=[]:
            return Daw
        else:
            return ""

    
    def updateno(self,IDNoh,ListaNova):
        Posi=self.funcao(IDNoh)
        self.table[Posi]=[ListaNova]