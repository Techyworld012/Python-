# Nested loops are the loops inside the loops. The inner loop will be executed one time for each iteration of the outer loop.

for i in range(1, 4):  # outer loop

    for j in range(1, 11):  # inner loop

        print( j ,end ="")

    print()                  # printing a new line after each iteration of the outer loop