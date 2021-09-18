import json
text = []
attibutes = []
f = open('F:\\UIR\\github\\9.18\\ccks_task1_train(1).json', 'r', encoding="utf-8")
fw = open("ccks_task1_train(11).txt", "w", encoding="UTF-8")
for jsonstr in f.readlines():         # 读取所有行,每行是一个字符串
    jsonstr = json.loads(jsonstr)     # 将josn字符串转化为dict字典
    text = jsonstr['text']            # 写入一个列表
    attributes = jsonstr['attributes']
    for i in range(len(text)):  # len
        temp = 0
        for j in attributes:
            if temp == len(attributes) - 1:
                x = text[i] + ' O' + '\n'
                fw.write(x)
                break
            if j['start'] == i:       # ner[i['entity'][j]] = 'B-' + i['type']
                x = text[i] + ' B-' + j['type'] + '\n'
                fw.write(x)
                break
            elif j['start'] < i <= j['end']:
                x = text[i] + ' I-' + j['type'] + '\n'
                fw.write(x)
                break
            temp += 1
    fw.write('\n')