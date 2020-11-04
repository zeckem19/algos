
class RodCutting:
	
	def __init__(self, lengthOfRod, prices, section_lengths):
		self.lengthOfRod = lengthOfRod
		self.prices = prices
		self.sectls = section_lengths
		self.dp = [[0 for lengths in range(self.lengthOfRod+1)] for types in self.sectls]
	
	def dynamicProgrammingApproach(self):
		for sl in range(1, len(self.sectls)):
			for sell_length in range(1, self.lengthOfRod+1):
				if sl > lengthOfRod:
					self.dp[sl][sell_length] = self.dp[sl-1][sell_length]
				else:
					if sl > sell_length:
						cut = 0
					else:
						cut = self.prices[sl] + self.dp[sl][sell_length - sl]
					dont_cut = self.dp[sl-1][sell_length]
					self.dp[sl][sell_length] = max(cut, dont_cut)
		return self.dp
		
	def showResults(self):
	
		print("Max profit is: $%d" % self.dp[len(self.prices)-1][self.lengthOfRod])
	
		columnIndex = self.lengthOfRod
		rowIndex = len(self.prices)-1
		
		while columnIndex > 0 or rowIndex > 0:
			
			if self.dp[rowIndex][columnIndex] == self.dp[rowIndex-1][columnIndex]:
				rowIndex = rowIndex - 1
			else:
				print("We make cut: ", rowIndex,"m")
				columnIndex = columnIndex - rowIndex
		
if __name__ == "__main__":

	lengthOfRod = 10
	section_lengths = [0,1,2,3,4]
	prices = [0,1,5,8,10]


	rodCutting = RodCutting(lengthOfRod, prices, section_lengths)
	print(rodCutting.dynamicProgrammingApproach())
	# rodCutting.showResults()
	
	
	
		
	