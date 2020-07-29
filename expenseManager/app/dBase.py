from ItemData import DbItemData
from CardData import DbCardData
from TranData import DbTranData
class dBase:
    def __init__(self):
        self.dbItem=[];self.dbCat=[];self.dbSubCat=[];
        self.dbCard = [];
        self.dbTran = [];
        self.IsLoggedIn=False;
        self.logInCard = None;
    def loadItem(self,IsMsg=True):
        if (IsMsg): print("Loading DataBase...")
        if(IsMsg): print("Loading Item DataBase...")
        self.dbItem = DbItemData.readItems()
        self.dbCat=DbItemData.getDbCategory(self.dbItem)
        self.dbSubCat = DbItemData.getDbSubCategory(self.dbItem)
        if (IsMsg): print("Loaded Item DataBase %d!"%len(self.dbItem))
    def loadCard(self,IsMsg=True):
        if(IsMsg): print("Loading Card DataBase...")
        self.dbCard = DbCardData.readCards()
        if (IsMsg): print("Loaded Card DataBase %d!"%len(self.dbCard))
    def loadTran(self,valueCard,IsMsg=True):
        if(IsMsg): print("Loading T DataBase...")
        self.dbTran = DbTranData.readTrans(valueCard)
        if (IsMsg): print("Loaded T DataBase%d!"%len(self.dbTran))
    def loadTranByItem(self,valueCard,IsMsg=True):
        if(IsMsg): print("Loading T DataBase...")
        self.dbTran = DbTranData.readTrans(valueCard,True,self.dbItem)
        if (IsMsg): print("Loaded T DataBase%d!"%len(self.dbTran))
    def loadItemCard(self,IsMsg=True):
        if(IsMsg): print("Loading DataBase...")	
        self.loadCard()
        self.loadItem()
        if(IsMsg): print("Loaded DataBase!")
ndb = dBase()