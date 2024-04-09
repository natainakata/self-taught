#!/usr/bin/env python


musician = ["T.M.Revolution", "Team Grimore", "xi", "BlackY"]
traveled = [(35.709, 139.7319), (35.1814, 136.9063), (35.4437, 139.638)]
my_identify = {"身長": "173cm", "好きな作家": "ダイハード・テイルズ", "好きな色": "黒"}

print(musician)
print(traveled)
print(my_identify)

guess = input("キーを入力してください: ")

if guess in my_identify:
    print(my_identify[guess])
else:
    print("キーがない")


music = {"T.M.Revolution": ["INVOKE", "Meteor", "Ignited"]}
print(music)

sosuu = {1, 3, 5, 7, 11, 13, 17}
print(sosuu)
