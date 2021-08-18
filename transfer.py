# 将2500个常用汉字重新编码，缩短字符长度的同时，平衡各个字母使用频率
import pypinyin
import character as c

trans = {}
order = ['v', 'r', 'k', 'p', 'w', 'f', 'q', 't', 'm', 'e', 'b', 'd', 'o',
         'x', 'c', 'l', 's', 'j', 'y', 'z', 'h', 'g', 'u', 'a', 'i', 'n']
visited = {'v': 0, 'r': 0, 'k': 0, 'p': 0, 'w': 0, 'f': 0, 'q': 0, 'm': 0,
           't': 0, 'b': 0, 'd': 0, 'x': 0, 'l': 0, 'c': 0, 'y': 0, 's': 0,
           'j': 0, 'z': 0, 'e': 0, 'o': 0, 'h': 0, 'g': 0, 'u': 0, 'a': 0,
           'i': 0, 'n': 0}


# 不带声调的(style=pypinyin.NORMAL)
def f(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s


# 编码常用字
def init():
    char = c.s.split('\n')
    for ch in char:
        first = f(ch)[0]
        if visited[first] == 0:
            trans[ch] = first
        elif visited[first] <= 26:
            trans[ch] = first + order[visited[first] - 1]
        else:
            trans[ch] = first + order[int((visited[first] - 1) / 26)] + order[(visited[first] - 1) % 26]
        visited[first] += 1
        if int((visited[first] - 1) / 26) == 1:
            visited[first] += 4
        if (visited[first] - 1) % 26 == 1:
            visited[first] += 8
        if int((visited[first] - 1) / 26) == 2:
            visited[first] += 2
        if (visited[first] - 1) % 26 == 2:
            visited[first] += 4
        if int((visited[first] - 1) / 26) == 3:
            visited[first] += 1
        if (visited[first] - 1) % 26 == 3:
            visited[first] += 2
        if (visited[first] - 1) % 26 == 4:
            visited[first] += 1

# 计数
# for i in c.s:
#     if f(i)[0].isalpha():
#         visited[f(i)[0]] += 1
#
# for i in c.s1:
#     for x in f(i):
#         if x.isalpha():
#             visited[x] += 1
#
# d_order = sorted(visited.items(), key=lambda x: x[1], reverse=False)
# for i in d_order:
#     print(i)
