
class CoinChange:
	
	# M - total amount and v[] coins
	def naiveApproach(self, M, v, index):
		
		if M < 0: return 0
		if M == 0: return 1
	
		if index == len(v): return 0
		
		return self.naiveApproach(M-v[index], v, index) + self.naiveApproach(M, v, index+1)
	
	# M - total amount and v[] coins
	def dynamicProgrammingApproach(self, coins, M):
	
		dpTable = [[0 for i in range(M+1)] for coin in range(len(coins)+1) ]
		
		for i in range(len(coins)+1):
			dpTable[i][0] = 1
		for coinIdx in range(1, len(coins)+1):
			for val in range(1, M+1):
				if coins[coinIdx-1] > M:
					dpTable[coinIdx][val] = dpTable[coinIdx-1][val] 
				else:
					dpTable[coinIdx][val] = dpTable[coinIdx-1][val] + dpTable[coinIdx][val-coins[coinIdx-1]]
		print(dpTable[-1][-1])


if __name__ == "__main__":

	M = 1000
	coins = [1,2,3]

	coinChange = CoinChange()
	coinChange.dynamicProgrammingApproach(coins,M)
	
	
	
		
	