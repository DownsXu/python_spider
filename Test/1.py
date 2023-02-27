import turtle

def test1():
    str1 = input('输入人名')
    str2 = input('输入国家名字')
    print('世界那么大, {}想去{}看看。'.format(str1, str2))


def test2():
    n = input('请输入整数')
    sum = 0
    for i in range(int(n)):
        sum += i + 1
    print(sum)

def test3():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{} * {} = {:2}'.format(j, i, i * j), end=' ')
    print(' ')

def test4():



if __name__ == '__main__':
    test3()
