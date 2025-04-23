N, M = map(int, input().split())
pwd_dict = dict()

for _ in range(N):
	site, pwd = input().split()
	pwd_dict[site] = pwd

for _ in range(M):
	print(pwd_dict[input()])