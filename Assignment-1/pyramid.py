# printing pyramid pattern
# Example : for height of the pyramid = 3
#   * 
#  ***
# *****
rows = int(input("Enter the height of the pyramid : "))
for i in range(1 , rows + 1):
    print(" " * (rows - i ) , "*"*(2*i - 1 ) , " " * (rows - i ))
    