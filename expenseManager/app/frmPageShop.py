import frmPageHome as frmHome
from CardData import CardData, DbCardData
from TranData import TranData,DbTranData
from UtilGp import UtilGp
from dBase import ndb
class Shop:
    @staticmethod
    def show():
        UtilGp.Login(Shop.showCat,ndb.loadTran,'Shopping (Login)')
        #print("Welcome To Shopping (Card No:xxxx)\nCredit Limit:xxxx, Credit Used: xxxx, Credit Balance: xxxx\n")
    @staticmethod
    def showFailure():
        ndb.IsLoggedIn = False; ndb.logInCard = None;
        choice = input("\n1-Exit App, 2-Main Menu\nYour Choice:")
        if not choice.isdigit():return
        choice=int(choice)
        if not (choice == 2): return
        UtilGp.mainMenu()
    @staticmethod
    def showCat():
        UtilGp.sleep(2);UtilGp.clear();UtilGp.title('Shopping');UtilGp.creditLine();
        print("\n %-10s  %-16s" % ('ID', 'Category'))
        UtilGp.linePrint('-', 42)
        for valueCat in ndb.dbCat:
            print(" %-10d %-16s"%(valueCat.catId,valueCat.category))
        UtilGp.linePrint('-', 42)
        choiceCatId = int(input("Enter Catgory ID\nYour Choice:"))
        isExist=False;resCat=None;
        for valueCat in ndb.dbCat:
            if valueCat.catId==choiceCatId:
                isExist=True;resCat=valueCat;
                break
        if isExist:
            Shop.showSubCat(resCat)
        else:
            print("You Category Not Exist.")
            Shop.showFailure()
    @staticmethod
    def showSubCat(valueCat):
        UtilGp.sleep(2)
        UtilGp.clear()
        UtilGp.title('Shopping(%s)'%(valueCat.category,));UtilGp.creditLine();
        subCat = list(filter(lambda x:x.catId==valueCat.catId,ndb.dbSubCat))
        print("\n %-10s  %-16s" % ('ID', 'Sub Category'))
        UtilGp.linePrint('-', 42)
        for valueSubCat in subCat:
            print(" %-10d %-16s" % (valueSubCat.subCatId, valueSubCat.subCategory))
        UtilGp.linePrint('-', 42)
        choiceSubCatId = int(input("Enter Sub Category ID\nYour Choice:"))

        #print(choiceSubCatId)
        isExist = False;resSubCat=None;
        for valueSubCat in subCat:
            if valueSubCat.subCatId == choiceSubCatId:
                isExist = True;resSubCat=valueSubCat;
                break
        if isExist:
            Shop.showItem(resSubCat)
        else:
            print("You Sub Category Not Exist.")
            Shop.showFailure()
    def showItem(valueSubCat):
        UtilGp.sleep(2);UtilGp.clear();UtilGp.title('Shopping(%s)' % (valueSubCat.subCategory,));UtilGp.creditLine();
        its = list(filter(lambda x:x.itemId//100==valueSubCat.subCatId,ndb.dbItem))
        if len(its)==1:
            if its[0].itemType==1:
                Shop.savingItem(its[0])
        else:
            print("\n %-10s  %-22s %12s" % ('ID', 'Item','Price') if valueSubCat.subCatId!=21 else "\n %-10s  %-16s" % ('ID', 'Item'))
            UtilGp.linePrint('-',48)
            for valueItem in its:
                print(" %-10d  %-22s %12s" % (valueItem.itemId, valueItem.itemName,'Rs.%7.2f' % (valueItem.price,))if valueSubCat.subCatId!=21 else "%-10d  %-16s" % (valueItem.itemId, valueItem.itemName))
            UtilGp.linePrint('-', 48)
            choidItemId = int(input("Enter Item ID\nYour Choice:"))
            #print(choidItemId)
            isExist = False;resItem=None;
            for valueItem in its:
                if valueItem.itemId == choidItemId:
                    isExist = True;resItem=valueItem;
                    break
            if isExist:
                Shop.savingItem(resItem)
            else:
                print("Your Item Not Exist.")
                Shop.showFailure()

    def savingItem(resItem):
        #amount validations against credit balance
        #confirming pin
        #success message
        res = UtilGp.parseItemMsg(resItem,ndb.logInCard.passCode,ndb.logInCard.creditBal())
        #end

        if res[0] == False:
            if res[1]==1:
                print("No sufficient credit balance.\nYour transaction is cancelled.\n")
            else:
                print("Incorrect PIN.\nFor security reason Your transaction is cancelled.\n")
            Shop.showFailure()
        else:
            #print(ndb.logInCard,resItem,res[4])
            Shop.saveItem(ndb.logInCard,resItem,res[4])
    @staticmethod
    def saveItem(valueCard, valueItem, price):
        tranId = 1 if len(ndb.dbTran)==0 else ndb.dbTran[len(ndb.dbTran)-1].tranId + 1
        tranData=TranData(tranId,valueCard.cardId,valueCard.cardNo,valueCard.name,
                          UtilGp.now(),valueItem.itemId,price)
        DbTranData.addToTran(tranData)
        valueCard.creditUsed+=price
        tranRewardPoint = price//100 * (1 if valueCard.cardType=='Gold' else 2)
        valueCard.creditUsed += price
        valueCard.rewardPoint += tranRewardPoint
        DbCardData.updateCards(ndb.dbCard, valueCard)

        print();print("Reward Points earned for this transaction : %d"%(tranRewardPoint,));print();
        UtilGp.printCaptionData(('Credit Limit Used', 'Credit Limit Available', 'Total Reward Points'),
                                (UtilGp.priceToStr(valueCard.creditUsed),UtilGp.priceToStr(valueCard.creditBal()), valueCard.rewardPoint), 25)

        print("Loading..DB.2.\r", end="")
        ndb.loadCard(False)
        ndb.loadTran(valueCard,False)
        print("               \n", end="")

        Shop.showFailure()