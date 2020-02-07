def burrowWheels(text):
	rotations = []
	for i in range(len(text)):
		char = text[i]
		rotations.append(text[i:] + text[:i])

	rotations = sorted(rotations)
	newStr = ''
	for permutation in rotations: 
		newStr += permutation[-1]

	return newStr

def main():
	with open('rosalind_ba9i.txt', 'r') as myfile:
		data = myfile.readlines()
	text = data[0].rstrip('\n')

	burrowWheeler = burrowWheels(text)

	print(burrowWheeler)


if __name__ == "__main__":
	main()