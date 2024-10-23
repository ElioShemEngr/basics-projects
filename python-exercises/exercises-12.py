print("Grade Calculator")
print()
nameOfExam = input("Name of Exam: ")
print()
maxScore = int(input("Max. possible score: "))
print()
yourScore = int(input("Your Score: "))
print()

#Final Score
finalScorePercent = ( yourScore * 100 ) / maxScore

print("In the exam of ",nameOfExam, " you got ", finalScorePercent ,"%" )
if finalScorePercent >= 90 and finalScorePercent <= 100:
  print("Your letter score is an A+")
elif finalScorePercent >= 80 and finalScorePercent <= 89:
  print("Your letter grade is an A-.")
elif finalScorePercent >= 70 and finalScorePercent <= 79:
  print("Your letter score is a B.")
elif finalScorePercent >= 60 and finalScorePercent <= 69:
  print("Your letter grade is a C.")
elif finalScorePercent >= 50 and finalScorePercent <= 59:
  print("Your letter grade is a D.")
elif finalScorePercent <= 49:
  print("Your letter grade is a U.")
else: 
  print("Error in the values introduced!")
