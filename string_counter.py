#!/usr/bin/env python3


"""空白を含めた文字列をカウントする
"""


def string_counter(args_str):
    """空白を含めた文字列をカウントして返す

    param:
        args_str: 空白を含めた文字列

    return value:
        res: args_strにlen()を適用して代入した変数
    """

    res = len(args_str)
    return res

if __name__ == '__main__':
    print('空白を含めた文字列をカウント: 終了はq, またはQキー')
    print('>>> ', end='')
    while True:
        enter_str = input()

        if enter_str == 'q' or enter_str == 'Q':
            print('終了')
            break

        print(string_counter(enter_str))
        print('>>> ', end='')
