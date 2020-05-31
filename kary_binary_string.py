def kary_binary_string(n, k, list):
    if n < 1:
        print(list)
        return
    for i in range(k):
        list[n-1] = i
        kary_binary_string(n-1, k, list)


if __name__ == "__main__":
    kary_binary_string(3, 3, [0]*3)
