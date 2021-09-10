import random

def get_ai_code():
	numbers = list(range(10))
	random.shuffle(numbers)

	code = numbers[:4]

	return code


if __name__ == '__main__':
	ai_code = get_ai_code()
	print(ai_code)
