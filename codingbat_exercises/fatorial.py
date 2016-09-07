def fatorial(n):
    fat = 1
    for n in range(1, n + 1):
        fat = fat * n
    return fat

def fatorial_recursivo(n):
    return n * fatorial_recursivo(n - 1) if n > 0 else 1

def main():
    assert fatorial(1) == 1
    assert fatorial(2) == 2
    assert fatorial(3) == 6
    assert fatorial(5) == 120

    assert fatorial_recursivo(1) == 1
    assert fatorial_recursivo(2) == 2
    assert fatorial_recursivo(3) == 6
    assert fatorial_recursivo(5) == 120

if __name__ == '__main__':
    main()


