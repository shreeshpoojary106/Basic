i = 0
j = 0

for i in range(12):
    for j in range(15):
        if((i == 0 or i == 11) and (j == 0 or j == 1 or j == 2 or j == 3 or j == 4 or j == 5 or j == 6 or j == 8 or j == 9 or j == 10 or j == 11 or j == 12 or j == 13 or j == 14)):
            print("  ",end="")
        elif((i == 1 or i == 10) and (j == 0 or j == 1 or j == 2 or j == 3 or j == 4 or j == 5 or j == 9 or j == 10 or j == 11 or j == 12 or j == 13 or j == 14)):
            print("  ",end="")
        elif((i == 2 or i == 9) and (j == 0 or j == 1 or j == 2 or j == 3 or j == 4 or j == 10 or j == 11 or j == 12 or j == 13 or j == 14)):
            print("  ",end="")
        elif((i == 4 or i == 7) and (j == 0 or j == 14)):
            print("  ",end="")
        elif((i == 5 or i == 6) and (j == 0 or j == 1 or j == 13 or j == 14)):
            print("  ",end="")
        else:
            print(" *",end="")

        j += 1

    i += 1
    print("\n")

