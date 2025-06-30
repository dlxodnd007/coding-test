def recursive(n, r, c):

	# base case
    if n == 0: 
        return 0

    half = 2 ** (n - 1)
    area = half * half


    # 1번 사각형
    if r < half and c < half:
        return recursive(n - 1, r, c)

    # 2번 사각형
    elif r < half and c >= half:
        return area + recursive(n - 1, r, c - half)

    # 3번 사각형
    elif r >= half and c < half:
        return 2 * area + recursive(n - 1, r - half, c)

    # 4번 사각형
    else:
        return 3 * area + recursive(n - 1, r - half, c - half)

N, R, C = map(int, input().split())
print(recursive(N, R, C))