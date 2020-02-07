def DPChange(money, coins):
	minimumCoins = {}
	minimumCoins[0] = 0
	for m in range(1, money+1):
		minimumCoins[m] = money 
		for i in range(len(coins)):
			if m >= coins[i]:
				if minimumCoins[m-coins[i]]+1 < minimumCoins[m]:
					minimumCoins[m] = minimumCoins[m-coins[i]] + 1

	return minimumCoins[money]

def main():
	with open('rosalind_ba5a.txt', 'r') as myfile:
		data = myfile.readlines()
	money = int(data[0])
	coins = data[1]
	coins = coins.rstrip('\n')
	coins = coins.split(",")
	for i in range(len(coins)):
		coins[i] = int(coins[i])
		
	minCoins = DPChange(money, coins)
	print(minCoins)
 
if __name__ == "__main__":
	main()