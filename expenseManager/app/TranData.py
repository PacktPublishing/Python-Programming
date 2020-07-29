import pickle
class TranData:
	def __init__(self, tranId, cardId, cardNo,cardHolderName, tranDate, itemId, price):
		self.tranId=tranId;self.cardId=cardId;self.cardNo=cardNo;self.cardHolderName=cardHolderName;
		self.tranDate=tranDate;self.itemId=itemId;self.price=price;self.tranItem=None;self.isTranItem=False;
	def __repr__(self):
		return "%s- %s-%s-%s-%s-%s- %s"%(str(self.tranId),
				str(self.cardId),str(self.cardNo),self.cardHolderName, str(self.tranDate),str(self.itemId),
				str(self.price))
	def Category(self):
		return "" if not self.isTranItem else self.tranItem.category
	def SubCategory(self):
		return "" if not self.isTranItem else self.tranItem.subCategory
	def ItemName(self):
		return "" if not self.isTranItem else ("Bill" if self.tranItem.itemType==1 else self.tranItem.itemName)

DbTranDataFile="data/%s%s.dat"
class DbTranData:
	@staticmethod
	def getFileName(cardHolderName,cardNo):
		return DbTranDataFile%(cardHolderName,cardNo)
	@staticmethod
	def addToTran(valueTran):
		#print(valueTran)
		fname=DbTranData.getFileName(valueTran.cardHolderName,valueTran.cardNo)
		#print(fname)
		with open(fname, 'ab') as output:
			pickle.dump(valueTran, output, pickle.HIGHEST_PROTOCOL)
	@staticmethod
	def readTrans(valueCard,HasItem=False,dbItem=None):
		#print(valueCard)
		fname = DbTranData.getFileName(valueCard.name,valueCard.cardNo)
		from os import path
		if not path.exists(fname):
			f =open(fname, "wb")
			f.close()
		dbTran = []
		with open(fname, "rb") as f:
			while True:
				try:
					valueTran=pickle.load(f)
					if HasItem and (not valueTran.isTranItem):
						from ItemData import DbItemData
						vRes=DbItemData.getItemById(dbItem,valueTran.itemId)
						if vRes[0]:
							valueTran.isTranItem = True;valueTran.tranItem = vRes[1];
					dbTran.append(valueTran)
				except EOFError:
					break
		return dbTran

	@staticmethod
	def queryByDateRange(dbTran,fromDate,toDate):
		resTran=[]
		for valueTran in dbTran:
			if fromDate<=valueTran.tranDate and valueTran.tranDate<=toDate:
				resTran.append(valueTran)
		return resTran
	@staticmethod
	def queryAll(dbTran):
		resTran=[]
		for valueTran in dbTran:
			resTran.append(valueTran)
		return resTran
	@staticmethod
	def queryByAmount(dbTran,fromAmount,toAmount):
		resTran=[]
		for valueTran in dbTran:
			if fromAmount<=valueTran.price and valueTran.price<=toAmount:
				resTran.append(valueTran)
		return resTran
	@staticmethod
	def queryByCategory(dbTran,categoryId):
		resTran=[]
		for valueTran in dbTran:
			if valueTran.itemId//1000==categoryId:
				resTran.append(valueTran)
		return resTran
	@staticmethod
	def printTran(dbTran):
		from UtilGp import UtilGp
		print();UtilGp.linePrint('*')
		print('%-12s%-14s %-16s%-20s%14s'%('Date','Category','Sub Category','Item','Amount'))
		UtilGp.linePrint('*');print()
		for valueTran in dbTran:
			print('%-12s%-14s %-16s%-20s%14s ' % (UtilGp.dateToStr(valueTran.tranDate),
				valueTran.Category(), valueTran.SubCategory(),valueTran.ItemName(),
				'Rs.%7.2f' % (valueTran.price,)))
		if len(dbTran)==0:
			print("**No Data Found**")
		print();UtilGp.linePrint('*');print();