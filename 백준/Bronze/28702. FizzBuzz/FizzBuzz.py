for i in range(3):
	x = input()

	if x not in ['FizzBuzz', 'Fizz', 'Buzz']:
		ans = int(x) + 3 - i

		if ans % 15 == 0:
			print('FizzBuzz')
		elif ans % 3 == 0:
			print('Fizz')
		elif ans % 5 == 0:
			print('Buzz')
		else:
			print(ans)

		break
