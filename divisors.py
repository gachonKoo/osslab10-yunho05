number = int(input("약수를 구할 숫자를 입력하세요: "))

divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print(f"{number}의 약수: {divisors}")
