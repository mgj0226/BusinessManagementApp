import os
"""
進貨價格是 c 元
賣給客人的零售價則是 r 元
單日需求量 D 是隨機的
估計明天的單日需求量會落在 0 和 N 之間
Pr(D=i)=pi，i=0,1,...,N
訂貨量 q
π(q)=rE[min{q,D}]-cq
min{q,D} 是明天的銷售量 (q 和 D 的最小值)
E[min{q,D}] 是預期銷售量 (q 和 D 的最小值的期望值)
rE[min{q,D}] 是預期銷售收益
cq 則是必須付給報社的進貨成本

c, r, N, p0, 01, pN, q

if c = 2, r = 10
i : Pr(D=xi)
0 : 0.06
1 : 0.15
2 : 0.22
3 : 0.22
4 : 0.17
5 : 0.10
6 : 0.05
7 : 0.02
8 : 0.01
"""
def main():
    while True:
        c = input("Enter the purchase price: ")
        if c == "done":
            print("Goodbye!")
            break
        else:
            c = int(c)
        r = int(input("Enter the retail price: "))
        N = int(input("Enter the maximum demand: "))
        q = int(input("Enter the order quantity: "))
        p = {}
        for i in range( N + 1 ):
            p[i] = float(input(f"Enter the probability of demand {i} : ")) /100
        # calculate the expected sales
        E = 0
        for i in p:
            E += min(q, i) * p[i]
        # calculate the expected profit(無條件捨去到整數)
        profit = int(r * E - c * q)
        print(profit)
        continue

def test():
    c = 2
    r = 10
    N = 8
    q = 6
    p = {0: 0.06, 1: 0.15, 2: 0.22, 3: 0.22, 4: 0.17, 5: 0.10, 6: 0.05, 7: 0.02, 8: 0.01}
    E = 0
    for i in p:
        E += min(q, i) * p[i]
    profit = int(r * E - c * q)
    print(profit)
    return profit

# test()
# main()

"""
題目敘述
在本題中，我們承接第一題的報童問題，但現在我們不想根據給定的一個存貨量去計算預期利潤；我們想要找出能最大化預期利潤的最佳訂貨量 
𝑞
∗
q 
∗
 ，以及在此訂貨量之下能得到的預期利潤 
𝜋
(
𝑞
∗
)
π(q 
∗
 ) 無條件捨去到整數位。以第一題的例子而言，就是 4 跟 18（請自己試著算算看）。如果有數個訂貨量會導致一模一樣的預期利潤（是預期利潤一樣，不是無條件捨去之後一樣！），請用比較小的那一個當最佳訂貨量。

輸入輸出格式
在每筆測試資料中，會有 
𝑁
+
4
N+4 列，每一列都有一個數字。第一列的整數是單位進貨成本 
𝑐
c、第二列的整數是單位零售價格 
𝑟
r、第三列的整數是需求的可能個數 
𝑁
N、第四列開始的小數則依序是賣出零份、一份直到 
𝑁
N 份報紙的機率（也就是說對於 
𝑖
=
4
,
5
,
.
.
.
,
𝑁
+
4
i=4,5,...,N+4，第 
𝑖
i 列記錄的是賣出 
𝑖
−
4
i−4 份報紙的機率）。已知 
𝑐
c 會落在 1 到 100 之間（包含 1 跟 100）、
𝑟
r 會落在 1 到 100 之間（包含 1 跟 100）、
𝑟
r 不會比 
𝑐
c 小、
𝑁
N 一定會是 8。此外，對於 
𝑖
=
0
,
1
,
.
.
.
,
𝑁
i=0,1,...,N，
𝑝
𝑖
p 
i
​
  會介於 0 到 1 之間（包含 0 跟 1）、最多只有兩位小數，並且滿足 
∑
𝑖
=
0
𝑁
𝑝
𝑖
=
1
∑ 
i=0
N
​
 p 
i
​
 =1。

讀入這些資料之後，你會計算最佳訂購量 
𝑞
∗
q 
∗
 ，以及在此訂購量下的預期利潤無條件捨去到整數 
⌊
𝜋
(
𝑞
∗
)
⌋
⌊π(q 
∗
 )⌋，並且在兩者中間用一個空格隔開。
"""

def advanceMain():
    while True:
        c = input("Enter the purchase price: ")
        if c == "done":
            print("Goodbye!")
            break
        else:
            c = int(c)
        r = int(input("Enter the retail price: "))
        N = int(input("Enter the maximum demand: "))
        p = {}
        for i in range( N + 1 ):
            p[i] = float(input(f"Enter the probability of demand {i} : ")) /100
        # calculate q and profit
        max_profit = 0
        best_q = 0
        for q in range(1, 101):
            E = 0
            for i in p:
                E += min(q, i) * p[i]
            profit = int(r * E - c * q)
            if profit > max_profit:
                max_profit = profit
                best_q = q
        print(best_q, max_profit)
        continue

# advanceMain()

# 進階題目2
# s is salvage value
#c = data from line 1
#r = data from line 2
#N = data from line 3
#s = data from line 4
#pN = data from lineN - 5
def advanceMain2():
    data = []
    fname = "data.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, fname)
    # print(f"Constructed file path: {file_path}")

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    try:
        with open(file_path, "r") as file:
            data = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return

    data = [line.strip() for line in data]
    data = [(i) for i in data]

    # for line in hfile:
    #     data.append(line.strip())
    # data = [int(i) for i in data]


    c = int(data[0])
    r = int(data[1])
    N = int(data[2])
    s = int(data[3])
    p = {}
    for i in range( N + 1 ):
        p[i] = float(data[i + 4])
    # print(c, r, N, s, p)

    # calculate q and profit
    max_profit = 0
    best_q = 0
    for q in range(1, N + 1):
        E = 0
        for i in p:
            E += min(q, i) * p[i]
        l = q - E
        profit = int(r * E - c * q + s * l)
        if profit > max_profit:
            max_profit = profit
            best_q = q
    print(best_q, max_profit)


"""
如果你訂兩份報紙（q=2），
有 6% 的機率會賣掉零份（因為沒人想買），這種情況下你會賺 0−4+2=−2 元；有 15% 的機率會賣掉一份（如果恰好有一個人想買），這種情況下你會賺 10−4+1=7 元；
有 79% 的機率會賣掉兩份（只要有兩個以上的人想買），這種情況下你會賺 20−4=16 元。你的預期利潤是 (−2)×0.06+7×0.15+16×0.79=13.57 元
"""
def advanceMain2test():
    c = 2
    r = 10
    N = 10
    s = 1
    p = {0: 0.06, 1: 0.15, 2: 0.22, 3: 0.22, 4: 0.17, 5: 0.10, 6: 0.05, 7: 0.02, 8: 0.01, 9: 0.0, 10: 0.0}
    max_profit = 0
    best_q = 0
    for q in range(1, N + 1):
        E = 0
        for i in p:
            E += min(q, i) * p[i]
        l = q - E
        profit = int(r * E - c * q + s * l)
        if profit > max_profit:
            max_profit = profit
            best_q = q
    print(best_q, max_profit)

advanceMain2()