def findBestPrice(a, b, c1, c2, n):
    p2 = 0
    for i in range(n + 1):
        p1 = (a + b * p2 + c2) / 2
        p2 = (a + b * p1 + c1) / 2
    print("%0.2f %0.2f" % (p1, p2))

findBestPrice(9246,0.75,900,1023,2)