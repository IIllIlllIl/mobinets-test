import pypinyin
import passage
import numpy
import matplotlib.pyplot as plt

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


# 计算方差
def v():
    for i in frequency:
        frequency[i] = frequency[i] / total
    global variance
    for i in frequency:
        var.append(frequency[i])
    variance = numpy.var(var) * 100


# 填充绘图数组
def samplemat(dims):
    a = numpy.zeros(dims)
    for i in range(min(dims)):
        a[0, i] = 0
    if "a" in frequency:
        a[0, 0] = frequency['a']
    if "b" in frequency:
        a[0, 1] = frequency['b']
    if "c" in frequency:
        a[0, 2] = frequency['c']
    if "d" in frequency:
        a[0, 3] = frequency['d']
    if "e" in frequency:
        a[0, 4] = frequency['e']
    if "f" in frequency:
        a[0, 5] = frequency['f']
    if "g" in frequency:
        a[0, 6] = frequency['g']
    if "h" in frequency:
        a[0, 7] = frequency['h']
    if "i" in frequency:
        a[0, 8] = frequency['i']
    if "j" in frequency:
        a[0, 9] = frequency['j']
    if "k" in frequency:
        a[0, 10] = frequency['k']
    if "l" in frequency:
        a[0, 11] = frequency['l']
    if "m" in frequency:
        a[0, 12] = frequency['m']
    if "n" in frequency:
        a[0, 13] = frequency['n']
    if "o" in frequency:
        a[0, 14] = frequency['o']
    if "p" in frequency:
        a[0, 15] = frequency['p']
    if "q" in frequency:
        a[0, 16] = frequency['q']
    if "r" in frequency:
        a[0, 17] = frequency['r']
    if "s" in frequency:
        a[0, 18] = frequency['s']
    if "t" in frequency:
        a[0, 19] = frequency['t']
    if "u" in frequency:
        a[0, 20] = frequency['u']
    if "v" in frequency:
        a[0, 21] = frequency['v']
    if "w" in frequency:
        a[0, 22] = frequency['w']
    if "x" in frequency:
        a[0, 23] = frequency['x']
    if "y" in frequency:
        a[0, 24] = frequency['y']
    if "z" in frequency:
        a[0, 25] = frequency['z']
    return a


# 绘图
def show(t):
    dimlist = [(1, 26)]
    for d in dimlist:
        plt.matshow(samplemat(d))
        plt.title(t)
    plt.colorbar()
    plt.show()


# 输出统计量及热力图
def output(t):
    global total, variance
    print(t, ':')
    # print(frequency)
    print('total = ', total)
    print('variance = ', variance)
    show(t)


# 优化
def optimized():
    global total, variance

    show('optimized')


if __name__ == "__main__":
    # 统计字频
    s = f(passage.p)
    for i in s:
        if i.isalpha():
            total += 1
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
    v()

    # 计算统计量 绘制热力图
    output('origin')

    # optimized()


