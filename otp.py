from random import randint

for i in range(0,5):
  otp = randint(1000000, 99999999)
  print(f"{i+1}. your 8-digit OTP is: {otp}")
