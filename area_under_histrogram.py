"""Given a histogram , we need to find area of largest rectangle that can be made by joining each bar
    """


def area_under_hist():
    numbers = input("Input Histogram Heights")
    print("\n")
    histogram = [int(x) for x in numbers.strip().split(",")]
    stack = list()
    max_area = 0
    index = 0
    while index < len(histogram):
        if len(stack) == 0 or histogram[stack[-1]] < (histogram[index]):
            stack.append((index))
            index += 1
        else:
            top = stack.pop()
            area = (histogram[top] *
                    ((index - stack[-1] - 1) if stack else index))
            print(index)
            max_area = max(max_area, area)

    print(stack)
    while stack:
        top = stack.pop()
        area = (histogram[top]*((index - stack[-1] - 1) if stack else index))
        max_area = max(max_area, area)

    print(max_area)


if __name__ == '__main__':
    area_under_hist()
