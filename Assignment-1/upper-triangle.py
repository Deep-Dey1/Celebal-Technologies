# printing upper triangular pattern
# Example : for height of the triangle = 3
# ***
#  **
#   *
rows = int(input("Enter the height of the upper trianlge : "))
for i in range(rows,0,-1):
    print(" "*(rows-i),"*"*i)
    