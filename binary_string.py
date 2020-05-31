def binary_string(n, list):
    if n < 1:
        print(list)
        return
    list[n-1] = 0
    binary_string(n-1, list)
    list[n-1] = 1
    binary_string(n-1, list)


if __name__ == "__main__":
    binary_string(3, [0]*3)
