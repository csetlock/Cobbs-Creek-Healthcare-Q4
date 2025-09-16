# Carter Setlock
# Coding Assessment for Cobb Creek Healthcare

# Start Time: 2:05 PM
# End Time: 


# Question 1 Answer
# The command 'git reset --hard HEAD~2' essentially resets the repository to the state that it was in 2 commits prior.
# The command deletes the previous 2 commits and discards all changes in the working directory.


# Queston 2 Answer
# -rwxr-xr-x
# Conversion to Octal Notation:
# r (Read) = 4, w (Write) = 2, x (Execute) = 1
# rwx = 7, r-x = 5, r-x = 5
# 755
# Permissions:
# Owner - rwx: Has permissions to Read, Write, Execute
# Group - r-x: Has permissions to Read, Execute
# Others - r-x: Has permissions to Read, Execute


# Question 3

data = [98.6, 92.46, 82.45, 97.07, 96.16, 93.1, 80.51, 97.19, 90.56, 67.88, 83.74, 93.15,
70.27, 97.88, 93.38, 77.59, 76.85, 88.19, 70.91, 94.85, 93.1, 72.02, 65.1, 73.65,
70.52, 84.1, 76.4, 65.37, 80.56, 69.96, 79.61, 73.24, 89.84, 75.41, 94.17, 77.59,
73.08, 64.57, 65.72, 65.36, 90.52, 83.55, 76.29, 88.57, 93.46, 66.39, 75.8, 99.52,
86.32, 69.51, 73.44, 76.22, 71.33, 62.05, 99.7, 80.02, 73.68, 93.14, 74.24, 80.7,
96.47, 85.42, 87.3, 85.27, 81.07, 87.11, 83.59, 65.31, 78.74, 69.48, 62.7, 88.88,
78.87, 89.39, 88.75, 77.29, 73.03, 76.64, 62.93, 98.89, 59.53, 94.54, 90.95, 79.49,
88.84, 73.03, 58.19, 76.71, 87.32, 67.27, 97.54, 92.63, 91.25, 60.09, 99.31, 74.21,
76.38, 87.48]

def question3(data):
    mean = sum(data) / len(data)
    
    # std_dev
    var = 0
    for x in data:
        var += (x - mean) ** 2
    var /= (len(data) - 1)
    std_dev = var ** 0.5
    
    # Hint
    threshold = mean - 2 * std_dev # <- (58.7328)
    
    return len([x for x in data if x >= threshold]) # I believe there may be a typo with returning the value of *87* on the document.

print(question3(data))


