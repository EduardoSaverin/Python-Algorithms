def tower_of_hanoi(n,from_,to_,aux_):
    if n == 1:
        print(f"Move Disk 1 from {from_} to {to_}")
        return
    tower_of_hanoi(n-1,from_, aux_, to_)
    print(f"Move Disk {n} from {from_} to {to_}")
    tower_of_hanoi(n-1, aux_, to_, from_)

if __name__ == "__main__":
    tower_of_hanoi(4,'A', 'C', 'B')