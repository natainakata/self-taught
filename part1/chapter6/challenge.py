line = "カミュ"
print(line[0])
print(line[1])
print(line[2])

input1 = input("入力1: ")
input2 = input("入力2: ")

print("私は昨日{}を書いて、{}に送った！".format(input1, input2))
print("aldous Huxley was born in 1894.".capitalize())
whenlist = "どこで？ だれが？ いつ？".split(" ")
print(whenlist)

lists = ["The", "fox", "jumped", "over", "the", "fence", "."]
item = lists.pop()
print(" ".join(lists) + item)

print("Hermingway".index("m"))
print('禁断の二度打ち"二度打ち"')
print("three" + " three " + "three")
three = "three " * 3
three = three.strip()
print(three)

string = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"
index = string.index("、")
print(string[:index])
