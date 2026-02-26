#python function to find the maximum sum of a subarray in a given list of integers
def subarray(numbers):
    current_sum=numbers[0]
    max_sum=numbers[0]

    for num in numbers[1:]:
        current_sum=max(num,current_sum+num)
        max_sum=max(max_sum,current_sum)

    return max_sum

#Ask the user to input numbers
user=input("Enter numbers separated by spaces: ")

numbers=user.split()#converts the string into a list
numbers=[int(num)for num in numbers]

result=subarray(numbers)
print("The maximum subarray sum is: ",result)