#Question on string
# take input and print middle 3 characters,last 2 characters
food= input("Enter your favourite food:")
mid=len(food)//2
middle3=food[mid-1:mid+2]
print("The middle 3characters:",middle3)
last2=food[-2:]
print("The last 2characters:",last2)

