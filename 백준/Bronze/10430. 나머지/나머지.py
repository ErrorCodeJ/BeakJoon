# A, B, C를 입력받는다
A, B, C = map(int, input().split())

# (A + B) % C
print((A + B) % C)

# ((A % C) + (B % C)) % C
print(((A % C) + (B % C)) % C)

# (A × B) % C
print((A * B) % C)

# ((A % C) × (B % C)) % C
print(((A % C) * (B % C)) % C)