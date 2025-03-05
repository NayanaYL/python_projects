weight=int(input('whats your weight in kg'))
height=(float(input('what is your height in meter')))
bmi=weight/height**2
if bmi<16:
    print('under weight(severe thinness)')
elif 16<bmi>16:
    print('under weight(moderate thinness)')
elif 17<bmi>18.4:
    print('underweight (mild thinness)')
elif 18.5<bmi>24.9:
    print('normal range')
elif 25<bmi>29.9:
    print('overweight(pre-obesed')
else:
    print("obesed")
