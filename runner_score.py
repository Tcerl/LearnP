# Step 1: Input the number of scores
n = int(input("Enter the number of scores: "))

# Step 2: Input the scores as a list
a = list(map(int, input("Enter the scores separated by space: ").split()))

# Step 3: Find the maximum score and remove all instances of it from the list
max_score = max(a)
while max_score in a:
    a.remove(max_score)

# Step 4: The next maximum in the remaining list is the runner-up score
runner_up_score = max(a)

# Print the runner-up score
print("The runner-up score is:", runner_up_score)
