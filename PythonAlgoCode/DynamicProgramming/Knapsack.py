
class Knapsack:
	
	def __init__(self, numOfItems, capacityOfKnapsack, weightOfItems, profitOfItems):
		self.numOfItems = numOfItems
		self.capacityOfKnapsack = capacityOfKnapsack
		self.weightOfItems = weightOfItems
		self.profitOfItems = profitOfItems
		self.dpTable = [[0 for w in self.capacityOfKnapsack+1] for i in numOfItems+1]
	
	def dynamicProgrammingApproach(self):
		
		# no need to initialize because there are 0s by default !!!
		for w in range(1, capacityOfKnapsack+1):
			for n in range(1,numOfItems+1):
				#Don't take
				notTakingItem = self.dpTable[n-1][w]

				# take item
				prevItemWeight = w - weightOfItems[n]

				takingItem = 0
				#check if item can fit bag. if prev item weight is -ve means bag cant fit!
				if prevItemWeight >= 0:
					# check if value of prev item inside bag
					prevVal = self.dpTable[n-1][prevItemWeight]
					currentVal = self.profitOfItems[n]
					takingItem = currentVal + prevVal
				self.dpTable[n][w] = max(takingItem, notTakingItem)


	def showResult(self):

		print("Total benefit: %d" % self.dpTable[self.numOfItems][self.capacityOfKnapsack])
		
		w = self.capacityOfKnapsack		
		for n in range(self.numOfItems,0,-1):

			if self.dpTable[n][w] !=0 and self.dpTable[n][w] != self.dpTable[n-1][w]:
				print("We take item #%d" % n )
				w = w - self.weightOfItems[n]

if __name__ == "__main__":

	numOfItems = 4
	capacityOfKnapsack = 7
	weightOfItems = [0,1,3,4,5]
	profitOfItems = [0,1,4,5,7]
	

	knapsack = Knapsack(numOfItems, capacityOfKnapsack, weightOfItems, profitOfItems)
	knapsack.dynamicProgrammingApproach()
	knapsack.showResult()
	
	
	
		
	