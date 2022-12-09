import frmPageHome as frmHome
from CardData import CardData, DbCardData
from UtilGp import UtilGp
from dBase import ndb
from frmPageShop import  Shop
class ApplyCard:
    @staticmethod
    def show():
        UtilGp.clear()
        UtilGp.title('Applying Card')
        print("Loading...\r",end="")
        UtilGp.sleep(2)		
        name=input("%-30s:"%"Enter Name")
        mobileNo=input("%-30s:"%"Enter Mobile Number")
        if not UtilGp.isValidDigit(mobileNo):
            print("Invalid Mobile Number")
            Shop.showFailure()
            return
        dob=input("%s\n%-30s:"%("Enter Date of Birth","(DD-MM-YYYY)"))
        if not UtilGp.isValidDate(dob):
            print("Invalid Date Format")
            Shop.showFailure()
            return
        dob = dob + ' 00:00:00'
        dobDate = UtilGp.strToDate(dob)
        if UtilGp.age(dobDate)<18:
            print("Minimum age to apply should be 18 years")
            Shop.showFailure()
            return
        netSalary=input("%-30s:"%"Enter Net Annual Salary")
        if not UtilGp.isValidDigit(netSalary,False):
            print("Invalid Salary Input")
            Shop.showFailure()
            return
        netSalary =float(netSalary)
        if netSalary < 300000:
            print("Minimum Salary to apply for Credit Card is Rs.300000.00")
            Shop.showFailure()
            return
        adharNo = input("%-30s:" % "ADHAAR Number")
        if not UtilGp.isValidDigit(adharNo,True,12):
            print("Invalid ADHAAR number")
            Shop.showFailure()
            return
        adharCount = DbCardData.countCardByAdhaar(ndb.dbCard,adharNo)
        if adharCount>0:
            print("Only one credit card per user is allowed")
            Shop.showFailure()
            return
        card = CardData(name,mobileNo,dobDate,netSalary,adharNo)
        card.preCardRegister()
        passCode=input("%-30s:" % "Select Your PIN (4-Digit)")
        if not UtilGp.isValidDigit(passCode,True,4):
            print("Invalid PIN format")
            Shop.showFailure()
            return
        card.passCode = passCode


        DbCardData.addToCard(card)
        print();print("Congratulation!\nYour SBI Credit Card is Approved.");print();
        UtilGp.printCaptionData(('Card No', 'Credit Limit', 'Card Type'),
                                (card.cardNo, UtilGp.priceToStr(card.creditLimit), card.cardType), 20)
        Shop.showFailure()
