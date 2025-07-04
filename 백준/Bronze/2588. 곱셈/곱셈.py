# 두 세 자리 자연수를 입력받는다
A = int(input())
B = int(input())

# B의 각 자릿수 추출
digit1 = B % 10        # 일의 자리
digit2 = (B // 10) % 10  # 십의 자리
digit3 = B // 100      # 백의 자리

# (3): A × B의 일의 자리
print(A * digit1)

# (4): A × B의 십의 자리
print(A * digit2)

# (5): A × B의 백의 자리
print(A * digit3)

# (6): A × B 전체 곱셈 결과
print(A * B)