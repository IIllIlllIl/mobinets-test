import pypinyin
import passage
import numpy

frequency = {}
var = []
total = 0
variance = 0


# 不带声调的(style=pypinyin.NORMAL)
def f(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    return s


# 带声调的(默认)
def f2(word):
    s = ''
    # heteronym=True开启多音字
    for i in pypinyin.pinyin(word, heteronym=True):
        s = s + ''.join(i) + " "
    return s


def v():
    global variance
    for i in frequency:
        var.append(frequency[i])
    variance = numpy.var(var)


if __name__ == "__main__":
    # 统计字频
    s = f(passage.p1)
    for i in s:
        if i.isalpha():
            total += 1
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
    v()

    # 计算统计量
    print(frequency)
    print(total)
    print(variance)


