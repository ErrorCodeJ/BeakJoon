# 테스트 케이스의 개수 T를 입력받는다
T = int(input())

# T번 반복하며 A와 B를 입력받아 A+B를 출력
for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)