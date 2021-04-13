def swapFiledata():
    input("what is the name of the new file you want to swap: ")
    input("what is the name of the file you want to swap it with: ")

    with open('C:\Users\ansen\Desktop\Liam coding\C-98 project', 'r') as a:
        data_a = a.read()

    with open('C:\Users\ansen\Desktop\Liam coding\C98', 'r') as b:
        data_b = b.read

    with open('C:\Users\ansen\Desktop\Liam coding\C-98 project', 'w') as a:
        a.write(data_b)

    with open('C:\Users\ansen\Desktop\Liam coding\C98', 'b') as b:
        b.write(data_a)


swapFiledata()