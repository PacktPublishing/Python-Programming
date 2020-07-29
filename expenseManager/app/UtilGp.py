from datetime import datetime,timedelta
from os import system, name
from time import sleep
import re
import random

class UtilGp:
    @staticmethod
    def clear():
        if name == 'nt': #windows
            _ = system('cls')
        else: #mac,linux
            _ = system('clear')
    @staticmethod
    def dateToStr(valueDate,formatStr = '%d-%m-%Y'):
        strDate = valueDate.strftime(formatStr)
        return strDate
    @staticmethod
    def strToDate(strDate,formatStr = '%d-%m-%Y %H:%M:%S'):
        valueDate = datetime.strptime(strDate,formatStr)
        return valueDate
    @staticmethod
    def now():
        valueNow = datetime.strptime(datetime.now().strftime("%d-%m-%Y %H:%M:%S"),"%d-%m-%Y %H:%M:%S")
        return valueNow
    @staticmethod
    def dateAddDays(valueDate,valueDays):
        resDate =  valueDate + timedelta(days=valueDays)
        return resDate

    @staticmethod
    def age(dob):
        today = UtilGp.now()
        years = today.year - dob.year
        if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
            years -= 1
        return years
    @staticmethod
    def isValidDate(strDate,formatStr='%d-%m-%Y'):
        try:
            valueDate = UtilGp.strToDate(strDate,formatStr)
            return True
        except:
            return False
    @staticmethod
    def isValidDigit(strNo,isExactLen=True,noOfDigits=10):
        return str(strNo).isdigit() and \
               ((not isExactLen) or
                (isExactLen and len(strNo) == noOfDigits))
    @staticmethod
    def numberInput(prompt,isExactLen=False,noOfDigits=5):
        strNo = input(prompt)
        if not UtilGp.isValidDigit(strNo,isExactLen,noOfDigits): return(False,0)
        return (True, int(strNo))
    @staticmethod
    def sleep(sec):
        sleep(sec-1)
        pass
    @staticmethod
    def randNo(startNo, endNo, stepValue, isExcluded=False):
        endNo=endNo/stepValue
        startNo=startNo/stepValue
        if startNo==0: startNo=1
        if isExcluded:
            startNo+=1 #startNo+1 to endNo-1
        else:
            endNo+=1  #startNo to endNo
        return random.randint(startNo,endNo)*stepValue  # Generate randNo here
    @staticmethod
    def parseItemMsg(valueItem,passCode,creditBal):
        # :price  :tranMonYear  :priceInput(msg) :item   :tranNextDate :tranDate
        #print(valueItem.category,valueItem.subCategory,valueItem.itemName)
        isTranSuccess=True
        SuccessCode=0
        newPrice = 0
        if valueItem.itemType==1:
            nos = re.split('-|,', valueItem.priceRange)
            #print(result)
            #print(nos)
            newPrice = UtilGp.randNo(int(nos[0]),int(nos[1]),int(nos[2]),True)
            isNewPrice = True
            printPrice = newPrice
        else:
            printPrice = valueItem.price
        isNewPrice=False
        msg = valueItem.msg
        msgLines = msg.split("\n")
        nowValue = UtilGp.now()
        nowValuePlOne = UtilGp.dateAddDays(nowValue,1)
        for line in msgLines:
            line = str(line).replace(":price","Rs.%.2f"%(printPrice,))
            line = str(line).replace(":item", valueItem.itemName)
            line = str(line).replace(":tranMonYear", UtilGp.dateToStr(nowValue,'%b-%Y'))
            line = str(line).replace(":tranNextDate", UtilGp.dateToStr(nowValuePlOne, '%d-%m-%Y'))
            line = str(line).replace(":tranDate", UtilGp.dateToStr(nowValue, '%d-%m-%Y'))
            if line.startswith(":inputPrice"):
                newPrice = float(input("Enter Amount:"))
                printPrice=newPrice
                isNewPrice=True
            elif line.startswith(":pinConfirm"):
                if printPrice>creditBal:
                    isTranSuccess = False
                    SuccessCode = 1
                else:
                    from getpass import getpass
                    resPassCode = getpass("Confirm Your PIN:")
                    print()
                    if passCode!=resPassCode:
                        isTranSuccess=False
                        SuccessCode = 2
                        break
            else:
                print(line)
        ret = (isTranSuccess,SuccessCode,valueItem,isNewPrice,printPrice)
        #print(ret[0])
        return ret
    @staticmethod
    def mainMenu():
        UtilGp.sleep(2)
        UtilGp.clear()
        from frmPageHome import Home
        from frmPageApplyCard import ApplyCard
        from frmPageShop import Shop
        from frmPageReport import Report
        choice=Home.show()
        if  choice== 1:
            ApplyCard.show()
        elif choice == 2:
            Shop.show()
        elif choice == 3:
            Report.show()
    @staticmethod
    def startApp():
        UtilGp.clear();
        from dBase import ndb
        ndb.loadItemCard()
        UtilGp.mainMenu()
    @staticmethod
    def Login(fnToCall,tranLoader,pageTitle='Login'):
        from dBase import ndb
        ndb.loadItemCard()
        UtilGp.clear();UtilGp.title(pageTitle)
        from CardData import DbCardData
        from dBase import ndb
        from frmPageShop import Shop
        cardNo = input("Enter your card number:")
        vRet = DbCardData.getCardObject(ndb.dbCard, cardNo)
        # print(vRet)
        if vRet[0]:
            valueCard = vRet[1]
            from getpass import  getpass
            passCode = getpass("Enter your PIN:")
            # print("%s %s" % (cardNo, passCode))
            if valueCard.passCode == passCode:
                ndb.IsLoggedIn = True;
                ndb.logInCard = valueCard;
                tranLoader(valueCard, True)
                fnToCall() #Shop.showCat()
            else:
                print("Incorrect PIN")
                Shop.showFailure()
        else:
            print("\nCard does not exits.\n")
            Shop.showFailure()
    @staticmethod
    def centerText(text):
        text=str(text)
        l=len(text)
        sp=(79-len(text))//2
        return text.ljust(sp+l,' ').rjust(sp*2+l,' ')
    @staticmethod
    def linePrint(text='-',spaces=79):
        print(text.ljust(spaces,text))
    @staticmethod
    def title(screenName):
        titleCaption = "Expense Manager" + '-' + screenName
        UtilGp.linePrint()
        print("%s" % (UtilGp.centerText(titleCaption)))
        UtilGp.linePrint()
        #UtilGp.printCaptionData(('A','B'),('1000','Welcome'),20)
    @staticmethod
    def priceToStr(price):
        return 'Rs.%7.2f' % (price,)
    @staticmethod
    def creditLine():
        from dBase import  ndb
        vCard = ndb.logInCard
        print("%s" % (UtilGp.centerText("Credit Limit Used:%s\tCredit Limit Available:%s"%(UtilGp.priceToStr(vCard.creditUsed),UtilGp.priceToStr(vCard.creditBal())))))
        UtilGp.linePrint()
        #UtilGp.printCaptionData(('A','B'),('1000','Welcome'),20)
    @staticmethod
    def printCaptionData(caption, data, colonAt=40):
        sp1 = colonAt-2
        sp2 = 80-colonAt-4
        print()
        UtilGp.linePrint('*')
        for i in range(0,len(caption)):
            format ='# %-' + str(sp1) + 's:%-' + str(sp2) + 's #'
            print(format%(caption[i],data[i]))
        UtilGp.linePrint('*')
        print()
