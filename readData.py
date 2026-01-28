s = ["high","low","high"]
m = ["high", "high", "low"]
t = ["low", "high", "low"]
w = ["high", "low", "low"]
th = ["low", "high", "high"]
readings = t + w + th + m + s
lcount = readings.count("low")
hcount = readings.count("high")
if lcount > hcount:
    print("Water your plants on Friday 💦🪴")
else:
    print("Do not water your plants on Friday ❌💦🪴")