# 1 cup = 250 ml

def convert(cups):
    ml =round(float(cups) * 250)
    return ml

print ("This program will convert cups to ml")
cups = raw_input("how many cups? ")

milliliters = convert(cups)
print (cups + " cups is equal to " + str(milliliters) + " ml")
