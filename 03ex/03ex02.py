#link: https://www.youtube.com/watch?v=KJN3-7HH6yk

sh = input("enter hours: ")
sr = input("enter rates: ")

try: 
    fh = float(sh)
    fr = float(sr)
except: 
    print('error, please enter numeric input')
    quit()

print(fh, fr)
if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr

print("float pay:", xp)
