from UtilGp import UtilGp
from dBase import ndb
from TranData import DbTranData
from frmPageShop import Shop
class Report:
    @staticmethod
    def show():
        UtilGp.Login(Report.reportMenu, ndb.loadTranByItem,'Reports (Login)')
    @staticmethod
    def showDateRange():
        UtilGp.sleep(2);UtilGp.clear();UtilGp.title('Reports(%s)' % ('Transactions between two dates',))
        fromDate = input("From Date(dd-MM-YYYY):")
        toDate = input("To Date  (dd-MM-YYYY):")
        fromDate = UtilGp.strToDate(fromDate + ' 00:00:00')
        toDate = UtilGp.strToDate(toDate + ' 23:59:00')
        #print(fromDate,toDate)
        dbTran=DbTranData.queryByDateRange(ndb.dbTran,fromDate,toDate)
        DbTranData.printTran(dbTran)
        print("****End of Report****");print();
        from frmPageShop import Shop
        Shop.showFailure()
    @staticmethod
    def showBySortedAmount():
        UtilGp.sleep(2);UtilGp.clear();UtilGp.title('Reports(%s)' % ('All Transactions sorted on amount',))
        dbTran = DbTranData.queryAll(ndb.dbTran)
        dbTran.sort(key=lambda x:x.price)
        #print(dbTran)
        DbTranData.printTran(dbTran)
        print("****End of Report****");print();
        from frmPageShop import Shop
        Shop.showFailure()
    @staticmethod
    def showAmountRange():
        UtilGp.sleep(2);UtilGp.clear();UtilGp.title('Reports(%s)' % ('Transactions within amount range',))
        fromAmount = float(input("From Amount:"))
        toAmount = float(input("To Amount:"))
        #print(fromDate,toDate)
        dbTran=DbTranData.queryByAmount(ndb.dbTran,fromAmount,toAmount)
        DbTranData.printTran(dbTran)
        print("****End of Report****");print();
        Shop.showFailure()
    @staticmethod
    def showByCat():
        UtilGp.sleep(2);UtilGp.clear();UtilGp.title('Reports(%s)' % ('Transactions of a Category',))
        for valueCat in ndb.dbCat:
            print("%d %s"%(valueCat.catId,valueCat.category))
        choiceCatId = int(input("Enter Catgory ID\nYour Choice:"))
        isExist=False;resCat=None;
        for valueCat in ndb.dbCat:
            if valueCat.catId==choiceCatId:
                isExist=True;resCat=valueCat;
                break
        if isExist:
            dbTran = DbTranData.queryByCategory(ndb.dbTran, choiceCatId)
            DbTranData.printTran(dbTran)
            print("****End of Report****");print();
            Shop.showFailure()
        else:
            print("You Category Not Exist.")
            Shop.showFailure()
    @staticmethod
    def showCatTot():
        UtilGp.sleep(2);UtilGp.clear();UtilGp.title('Reports(%s)'%('Total Amount Spent on a Category',))
        for valueCat in ndb.dbCat:
            print("%d %s"%(valueCat.catId,valueCat.category))
        choiceCatId = int(input("Enter Catgory ID\nYour Choice:"))
        isExist=False;resCat=None;
        for valueCat in ndb.dbCat:
            if valueCat.catId==choiceCatId:
                isExist=True;resCat=valueCat;
                break
        if isExist:
            dbTran = DbTranData.queryByCategory(ndb.dbTran, choiceCatId)
            amount = sum(list(map(lambda x:x.price,dbTran)))
            UtilGp.printCaptionData(('Category','Total Amount Spent is'),
                                    (valueCat.category,'Rs.%.2f'%(amount,)), 45)
            #print("Total Amount Spent for category %s is Rs.%f"%(valueCat.category,amount))
            print("****End of Report****");print();
            Shop.showFailure()
        else:
            print("You Category Not Exist.")
            Shop.showFailure()

    @staticmethod
    def reportMenu():
        UtilGp.sleep(2);UtilGp.clear();UtilGp.title('Reports')
        print("1-All transactions done between two dates")
        print("2-All transactions that fall within a specified amount range")
        print("3-All transactions done on a category")
        print("4-Total amount spent on a category")
        print("5-Transactions sorted based on amount")
        choice=int(input("Your Choice:"))
        if choice == 1:
            Report.showDateRange()
        elif choice == 2:
            Report.showAmountRange()
        elif choice == 3:
            Report.showByCat()
        elif choice == 4:
            Report.showCatTot()
        elif choice == 5:
            Report.showBySortedAmount()