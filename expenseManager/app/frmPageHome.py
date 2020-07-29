from UtilGp import UtilGp
class Home:
	@staticmethod
	def show():
		UtilGp.title('Main Menu')
		print("\n%s\n"%(UtilGp.centerText("SBI Credit Cards... Make Your Life Easy."),))
		print("Loading...\r",end="")
		UtilGp.sleep(2)
		print("1. Apply for Credit Card")
		print("2. Shopping")
		print("3. My Trasactions")
		choice = int(input("Please Enter Your Choice:"))
		return choice



