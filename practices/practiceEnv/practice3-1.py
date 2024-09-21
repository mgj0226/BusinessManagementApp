def is_valid_taiwan_id(id_number):
    if len(id_number) != 10:
        return False

    # 台灣地區代碼對應數值
    letters = 'ABCDEFGHJKLMNPQRSTUVXYWZIO'
    if id_number[0] not in letters:
        return False

    # 將首字母轉換為數字
    letter_value = letters.index(id_number[0]) + 10
    id_numbers = [int(x) for x in str(letter_value)] + [int(x) for x in id_number[1:]]

    # 加權計算
    weights = [1, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    checksum = sum(w * n for w, n in zip(weights, id_numbers))

    # 驗證結果
    return checksum % 10 == 0

ids = ['A154285748', 'B127231725', 'C256572407', 'D232773770', 'E240211835']
for id_number in ids:
    print(f'{id_number}: {"合法" if is_valid_taiwan_id(id_number) else "不合法"}')

def enCode():
    pw = "MF GIHAB QYTV YTK"
    pwList = pw.split(" ")
    for i in pwList:
        ordLetters = [ord(x) for x in i]
        #convert int to str
        outPut = [str(x) for x in ordLetters]
        print("".join(outPut))
        #check the output
        # print("".join([chr(x) for x in ordLetters]))

def deCode():
    pw = "65666768.6970717273.74757677.78798081.82838485.8687888990"
    pwList = pw.split(".")
    msgs = []

    for i in pwList:
        intLetters = [int(i[j:j+2]) for j in range(0, len(i), 2)]
        msg = [chr(x) for x in intLetters]
        joinMsg = "".join(msg)
        msgs.append(joinMsg)

    # Join the decoded messages with a space
    final_msg = " ".join(msgs)
    print(final_msg)

enCode()
# deCode()


# Question 1
# 利用Python計算由2010年3月2日中午12點15分0秒起算，經過145天10小時又3分鐘之後的時間為何? 你的回答應該使用這個格式: YYYY-MM-DD HH:MM:SS，也就是年月日時分秒。
import datetime
start_time = datetime.datetime(2010, 3, 2, 12, 15, 0)
delta = datetime.timedelta(days=145, hours=10, minutes=3)
end_time = start_time + delta
print(end_time.strftime('%Y-%m-%d %H:%M:%S'))