# 1、随机生成100个数，采用快速排序法进行排序，并输出生成的随机数组和排序后的有序数组

import random

# 快速排序算法
def quick_sort(alist, start, end):

    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)


if __name__ == '__main__':
    # 生成随即数组
    random_list = []
    for i in range(0, 100):
        random_list.append(random.randint(0, 1000))  # 随即数组添加随机数
    quick_sort(random_list, 0, len(random_list) - 1)  # 对随机数组进行快排
    print(random_list)  # 打印结果
    #结果
    #[7, 14, 52, 91, 91, 97, 100, 100, 103, 106, 115, 125, 127, 132, 140,
    # 158, 163, 166, 169, 190, 191, 193, 201, 212, 230, 240, 241, 245,
    # 256, 266, 268, 269, 277, 280, 283, 344, 364, 371, 378, 378, 386,
    # 399, 400, 402, 402, 418, 425, 429, 441, 459, 488, 501, 523, 524,
    # 530, 544, 554, 581, 582, 604, 611, 615, 633, 661, 680, 701, 705,
    # 725, 736, 753, 764, 765, 766, 773, 780, 797, 800, 806, 822, 829,
    # 830, 836, 843, 856, 873, 875, 881, 883, 886, 903, 931, 936, 938,
    # 949, 951, 952, 957, 960, 994, 997]

