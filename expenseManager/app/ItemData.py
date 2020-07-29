import pickle
class ItemData:
    def __init__(self, itemId, category, subCategory, itemName, price, itemType, priceRange, msg):
        self.itemId = itemId; self.category = category; self.subCategory = subCategory; self.itemName = itemName;
        self.price = price; self.itemType=itemType; self.priceRange=priceRange; self.msg = msg;
    def __repr__(self):
        return "%s-%s-%s-%s-%s-%s-%s-%s"%(str(self.itemId),self.category,self.subCategory,
                self.itemName,str(self.price),str(self.itemType),self.priceRange,self.msg)
class CategoryData:
    def __init__(self, catId, category):
        self.catId = catId; self.category = category;
    def __repr__(self):
        return "%s-%s"%(str(self.catId),self.category)
class SubCategoryData:
    def __init__(self, subCatId, subCategory, catId):
        self.subCatId = subCatId; self.subCategory = subCategory;self.catId = catId;
    def __repr__(self):
        return "%s-%s-%s"%(str(self.subCatId),self.subCategory,self.catId)

DbItemDataFile="data/Item.dat"
class DbItemData:
    @staticmethod
    def initItems():
        dbItem = []
        dbItem.append(ItemData(1101, "Bills", "Electricity", "#", 0, 1, "700-1000,50", "Your current bill amount is: :price\n:pinConfirm\nBill Paid Successfully for :tranMonYear\nThank you for using our servies!")) #1 Amount Auto Generate
        dbItem.append(ItemData(1201, "Bills", "Mobile", "#", 0, 1, "400-800,20", "Your current bill amount is: :price\n:pinConfirm\nBill Paid Successfully for :tranMonYear\nThank you for using our servies!"))
        dbItem.append(ItemData(1301, "Bills", "Internet", "#", 0, 1, "800-1200,50", "Your current bill amount is: :price\n:pinConfirm\nBill Paid Successfully for :tranMonYear\nThank you for using our servies!"))
        dbItem.append(ItemData(1401, "Bills", "Water", "#", 0, 1, "100-500,10", "Your current bill amount is: :price\n:pinConfirm\nBill Paid Successfully for :tranMonYear\nThank you for using our servies!"))
        dbItem.append(ItemData(2101, "Vehicle", "Fuel", "Diesel", 0, 2, "", ":inputPrice\n:pinConfirm\nYour vehicle refilled with :item of amount :price\nHappy Journey!"))#2 User Input
        dbItem.append(ItemData(2102, "Vehicle", "Fuel", "Petrol", 0, 2, "", ":inputPrice\n:pinConfirm\nYour vehicle refilled with :item of amount :price\nHappy Journey!"))
        dbItem.append(ItemData(2201, "Vehicle", "Servicing", "Full Car Service", 5000, 3, "", "Service Includes Engine Oil Change, Full Body Check Up, Body Wash\n:pinConfirm\nYour car has been scheduled for the service on :tranNextDate\nThe amount paid is :price\nThank you for using our services!"))#3 DB Price
        dbItem.append(ItemData(2202, "Vehicle", "Servicing", "Water Wash Service", 1000, 3, "", "Service Includes Body Wash, Interior Foam Wash and Polishing\n:pinConfirm\nYour car has been scheduled for the service on :tranDate\nThe amount paid is :price\nThank you for using our services!"))
        dbItem.append(ItemData(2301, "Vehicle", "Accessories", "Floor Mate", 2000, 3, "", ":pinConfirm\nThank you for purchasing from us!\nAmount paid is :price"))
        dbItem.append(ItemData(2302, "Vehicle", "Accessories", "Seat Cover", 8000, 3, "", ":pinConfirm\nThank you for purchasing from us!\nAmount paid is :price"))
        dbItem.append(ItemData(2303, "Vehicle", "Accessories", "Tyre", 4000, 3, "", ":pinConfirm\nThank you for purchasing from us!\nAmount paid is :price"))
        dbItem.append(ItemData(3101, "Entertainment", "Movies", "Hindi Movie", 150, 3, "", ":pinConfirm\nThank you for choosing PVR Movies!\nAmount paid is :price"))
        dbItem.append(ItemData(3102, "Entertainment", "Movies", "Telugu Movie", 150, 3, "", ":pinConfirm\nThank you for choosing PVR Movies!\nAmount paid is :price"))
        dbItem.append(ItemData(3103, "Entertainment", "Movies", "English Movie", 200, 3, "", ":pinConfirm\nThank you for choosing PVR Movies!\nAmount paid is :price"))
        dbItem.append(ItemData(3201, "Entertainment", "Dining", "Music Restaurant(for 2 pax)", 1500, 3, "",":pinConfirm\nEnjoy the tasties food and melodius music!\nAmount paid is :price"))
        dbItem.append(ItemData(3202, "Entertainment", "Dining", "Pub with DJ(for 2 pax)", 2000, 3, "",":pinConfirm\nRock the mid night with your partner!\nAmount paid is :price"))
        dbItem.append(ItemData(4101, "Shopping", "Clothes", "Formal Trousher", 1999, 3, "", ":pinConfirm\nThank you for choosing Reliance Trends!\nAmount paid is :price"))
        dbItem.append(ItemData(4102, "Shopping", "Clothes", "Formal Shirt", 1499, 3, "", ":pinConfirm\nThank you for choosing Reliance Trends!\nAmount paid is :price"))
        dbItem.append(ItemData(4103, "Shopping", "Clothes", "Casual Trousher", 1599, 3, "", ":pinConfirm\nThank you for choosing Reliance Trends!\nAmount paid is :price"))
        dbItem.append(ItemData(4104, "Shopping", "Clothes", "Casual Shirt", 1399, 3, "", ":pinConfirm\nThank you for choosing Reliance Trends!\nAmount paid is :price"))
        dbItem.append(ItemData(4201, "Shopping", "Food", "South Indian Thali", 599, 3, "", ":pinConfirm\nThank you for choosing our services!\nAmount paid is :price"))
        dbItem.append(ItemData(4202, "Shopping", "Food", "North Indian Thali", 499, 3, "",":pinConfirm\nThank you for choosing our services!\nAmount paid is :price"))
        dbItem.append(ItemData(4203, "Shopping", "Food", "Chinese Thali", 399, 3, "",":pinConfirm\nThank you for choosing our services!\nAmount paid is :price"))
        return dbItem
    @staticmethod
    def addToItem(valueItem):
        with open(DbItemDataFile, 'ab') as output:
            pickle.dump(valueItem, output, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def updateItems(dbItem): #list Of Items
        with open(DbItemDataFile, 'wb') as output:
            for valueItem in dbItem:
                pickle.dump(valueItem, output, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def readItems():
        dbItem = []
        with open(DbItemDataFile, "rb") as f:
            while True:
                try:
                    dbItem.append(pickle.load(f))
                except EOFError:
                    break
        return dbItem
    @staticmethod
    def getDbCategory(dbItem):
        dbCat = []
        prevCatId=0
        for valueItem in dbItem:
            catId=valueItem.itemId//1000
            category = valueItem.category
            if prevCatId!=catId:
                dbCat.append(CategoryData(catId,category))
            prevCatId=catId
        return dbCat
    @staticmethod
    def getDbSubCategory(dbItem):
        dbSubCat = []
        prevSubCatId=0
        for valueItem in dbItem:
            subCatId=valueItem.itemId//100
            catId = valueItem.itemId // 1000
            subCategory = valueItem.subCategory
            if prevSubCatId!=subCatId:
                dbSubCat.append(SubCategoryData(subCatId,subCategory,catId))
            prevSubCatId=subCatId
        return dbSubCat
    @staticmethod
    def getItemById(dbItem, itemId):
        for valueItem in dbItem:
            if valueItem.itemId == itemId:
                return (True,valueItem)
        return (False,None)
