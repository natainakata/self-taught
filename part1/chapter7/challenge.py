list = ["ウォーキング・デッド", "アントラージュ", "ザ・ソプラノズ", "ヴァンパイア・ダイアリーズ"]
for i in list:
    print(i)

for i in range(25, 51):
    print(i)

i = 0
for movie in list:
    print(i)
    print(movie)
    i += 1

answer = [4, 10, 64]
while True:
    try:
        query = input("数字を当ててね(qを入力で終了): ")
        if query == "q":
            break
        else:
            query = int(query)
            if query in answer:
                print("正解")
            else:
                print("不正解")
    except ValueError:
        print("数字を入力するか、qで終了します。")
        continue

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
out = []

for i in list1:
    for j in list2:
        out.append(i * j)

print(out)
