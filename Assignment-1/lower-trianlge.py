# printing lower triangular pattern
# Example : for height of the triangle = 3
# *
# **
# ***
rows = int(input("Enter the height of the lower trianlge : "))
for i in range(1,rows+1):
    print("*"*i)