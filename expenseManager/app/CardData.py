import pickle
from UtilGp import UtilGp

class CardData:
    def __init__(self, name, mobileNo, dob, netSalary, adharNo):
        self.cardId=0;
        self.name=name;self.mobileNo=mobileNo;self.dob=dob;self.netSalary=netSalary;
        self.cardNo='8000';self.cardType="";self.creditLimit=0;
        self.creditUsed=0;self.passCode='1234';self.adharNo=adharNo;
        self.rewardPoint=0;self.rewardUsed=0;
    def __repr__(self):
        return "%s- %s-%s-%s-%s- %s-%s-%s -%s-%s -%s-%s %s-%s"%(str(self.cardId),
                self.name,self.mobileNo,self.dob,str(self.netSalary),
                str(self.cardNo),self.cardType,self.creditLimit,
                self.creditUsed,self.creditBal(),
                self.passCode,self.adharNo,str(self.rewardPoint),
                str(self.rewardUsed))
    def creditBal(self):
        return self.creditLimit - self.creditUsed
    def preCardRegister(self):
        from dBase import ndb
        dbCard = ndb.dbCard
        cardNo = DbCardData.genCardNo(dbCard);
        creditLimit = self.netSalary * 20 / 100;
        cardType = 'Gold' if creditLimit<100000 else 'Platinum'
        self.cardNo=cardNo
        self.creditLimit=creditLimit
        self.cardType=cardType
        self.cardId = len(dbCard)+1

DbCardDataFile="data/Card.dat"
class DbCardData:
    @staticmethod
    def addToCard(valueCard):
        with open(DbCardDataFile, 'ab') as output:
            pickle.dump(valueCard, output, pickle.HIGHEST_PROTOCOL)
    @staticmethod
    def initDbCards(): #list Of Cards
        with open(DbCardDataFile, 'wb') as output:
            pass
    @staticmethod
    def updateCards(dbCard,argCard): #list Of Cards
        with open(DbCardDataFile, 'wb') as output:
            for valueCard in dbCard:
                if valueCard.cardNo==argCard.cardNo:
                    pickle.dump(argCard, output, pickle.HIGHEST_PROTOCOL)
                else:
                    pickle.dump(valueCard, output, pickle.HIGHEST_PROTOCOL)
    @staticmethod
    def readCards():
        dbCard = []
        with open(DbCardDataFile, "rb") as f:
            while True:
                try:
                    dbCard.append(pickle.load(f))
                except EOFError:
                    break
        return dbCard
    @staticmethod
    def checkCardNoExist(cardNo, dbCard):
        for valueCard in dbCard:
            if valueCard.cardNo == cardNo:
                return True
        return False
    @staticmethod
    def countCardByAdhaar(dbCard,adhaarNo):
        count = 0
        for valueCard in dbCard:
            if valueCard.adharNo == adhaarNo:
                count += 1
        return count
    @staticmethod
    def genCardNo(dbCard):
        noStart = 8000;noEnd = 9000;stepValue = 1;
        cardNo = UtilGp.randNo(noStart, noEnd, stepValue,True)
        while DbCardData.checkCardNoExist(cardNo,dbCard):
            cardNo = UtilGp.randNo(noStart, noEnd, stepValue,True)
        cardNo = str(cardNo)
        return cardNo
    @staticmethod
    def getCardObject(dbCard, cardNo):
        for valueCard in dbCard:
            if valueCard.cardNo==cardNo:
                return (True, valueCard)
        return (False, None)

