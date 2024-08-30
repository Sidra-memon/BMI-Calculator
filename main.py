# BMI calcutor
height=int(input("enter height"))
weight=int(input("enter weight"))
BMI=weight/height**2
if BMI < 18.5:
  print("your are underweight")
elif BMI < 25:
  print("your are ok")
elif BMI < 30:
  print("you are overweight")
else:
 print("your are obese")