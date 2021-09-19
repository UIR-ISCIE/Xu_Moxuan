open_file = open('F:\\UIR\\9.19\\BIOtag(ccks_task1).txt', 'r', encoding="utf-8")  # 源文件
diff_line = open_file.readlines()
count = 0
for i in diff_line:
    if i == '\n':
        count += 1
    if count < 3500:
        with open('F:\\UIR\\9.19\\train.txt', 'a', encoding="utf-8") as temp1:
            temp1.write(i)
    elif 3500 <= count < 4000:
        with open('F:\\UIR\\9.19\\dev.txt', 'a', encoding="utf-8") as temp2:
            temp2.write(i)
    else:
        with open('F:\\UIR\\9.19\\test.txt', 'a', encoding="utf-8") as temp3:
            temp3.write(i)


# print(line_list)
# temp = 0
# for i in f.readline():
#     if i == '/n':
#         temp += 1
#         if i < 3500:
