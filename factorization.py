def printNumberFactors(x):
    print(f'Number factors of {x}:', end = " ")
    divisor = 2
    while x != 1:
        if x % divisor == 0:
            print(f"{divisor}", end = " ")
            x /= divisor
        else:
            divisor += 1

def main():
    x = int(input())
    printNumberFactors(x)

main()