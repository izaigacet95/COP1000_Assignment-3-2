# Function: This program determines if a student will be admitted or rejected.
# Input: Interactive
# Output: Accept or Reject

# Step 2: Write the interactive input statements to retrieve:
testScoreString = input("Enter the student's test score: ")
classRankString = input("Enter the student's class rank: ")

# Step 3: Write the statements to convert the string representation of a student’s test score and class rank to the integer data type
testScore = int(testScoreString)
classRank = int(classRankString)

# Test using admission requirements and print Accept or Reject
if testScore >= 90:
    if classRank >= 25:
        print("Accept")
    else:
        print("Reject")
else:
    if testScore >= 80:
        if classRank >= 50:
            print("Accept")
        else:
            print("Reject")
    else:
        if testScore >= 70:
            if classRank >= 75:
                print("Accept")
            else:
                print("Reject")
        else:
            print("Reject")
