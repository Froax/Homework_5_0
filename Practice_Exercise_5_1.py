def convert(Celcius):
    far = ((Celcius * 1.8) + 32)
    return far

for x in range(-30, 41, 10):
        print(convert(x),(x))

