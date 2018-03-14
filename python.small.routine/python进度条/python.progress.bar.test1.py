import sys
import time


def view_bar(num, total=100):
    rate = num / total
    rate_num = int(rate * 100)
    # 输出进度数字
    # bar = '%s' % (rate_num)

    # 输出进度百分比: %% 表示打印单个百分号
    # bar = '%s%%' % (rate_num)

    # 添加进度条，此时在一行内打印输出。例如: [=====]10%
    # bar = '[%s]%s%%' % ('='*num, rate_num)

    # 添加进度条，每行打印一条进度条。
    # \n 表示将光标移动到下一行，并不移动到首位
    #bar = '[%s]%s%%\n' % ('='*num, rate_num)

    # 添加进度条，在一行内进度条递增
    # \r 表示将光标移动到当前行的首位而不换行
    #bar = '\r[%s]%s%%' % ('=' * num, rate_num)

    # 进度条长度固定不变,进度条递增，同时百分比变化
    bar = '\r[%s%s]%s%%' % ('=' * num, ' '*(total - num), rate_num)
    sys.stdout.write(bar)
    sys.stdout.flush()


if __name__ == '__main__':
    for i in range(101):
        time.sleep(0.5)
        view_bar(i)

