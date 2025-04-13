def is_palindrom(S):
	for left in range(len(S)):
		right = len(S) - left - 1
		if S[left] != S[right]:
			return False
	return True


def is_pseudo_palindrome(S):
	for left in range(len(S)):
		right = len(S) - left - 1
		if S[left] != S[right]:
			S1 = S[:left] + S[left + 1 :]
			S2 = S[:right] + S[right + 1 :]
			if is_palindrom(S1) or is_palindrom(S2):
				return True
			else:
				return False

def solve():

	S = input()

	if is_palindrom(S):
		print(0)
		return

	if is_pseudo_palindrome(S):
		print(1)
		return

	print(2)

T = int(input())

for _ in range(T):
	solve()