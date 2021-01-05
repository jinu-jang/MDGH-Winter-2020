# -*- coding: utf-8 -*-

# 다음과 같은 삼각형을 출력하시오
# 예시1) level == 4
#  *
#  **
#  ***
#  ****
#
# 예시2) level == 2
#  *
#  **
def leftTriangle(level):
    pass

# 예시1) level == 4
#     *
#    **
#   ***
#  ****
#
# 예시2) level == 2
#   *
#  **
def rightTriangle(level):
    pass

# 예시1) level == 4
#     *
#    ***
#   *****
#  *******
#
# 예시2) level == 2
#     *
#    ***
def equiTriangle(level):
    pass

################
## 보너스 문제 ##
################

# 다음과 같은 사각형을 출력하시오
# 예시1) width == 4, height == 1
#  ****
#
# 예시2) width == 2, height == 6
#  **
#  **
#  **
#  **
#  **
#  **
def rectangle(width, height):
    pass

# 다음과 같은 사각형을 위 rectangle 함수를 사용하여 출력하시오
# 예시1) size == 4
#  ****
#  ****
#  ****
#  ****
#
# 예시2) size == 2
#  **
#  **
def square(size):
    pass

# 다음과 같은 삼각형을 출력하시오
# 예시1) level == 4
#  1
#  12
#  123
#  1234
#
# 예시2) level == 2
#  1
#  12
def numberTriangle(level):
    pass

####################
## 이하 실행 코드  ##
####################
import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('python3 week1.py <원하는 함수> <원하는 매개변수>\n형식으로 넣어주세요')

    elif sys.argv[1] == 'left':
        leftTriangle(int(sys.argv[2]))
    elif sys.argv[1] == 'right':
        rightTriangle(int(sys.argv[2]))
    elif sys.argv[1] == 'equi':
        equiTriangle(int(sys.argv[2]))
    elif sys.argv[1] == 'rect':
        if len(sys.argv) < 4:
            print('python3 week1.py rect <width> <height>\n형식으로 넣어주세요')
        else:
            rectangle(int(sys.argv[2]), int(sys.argv[3]))
    elif sys.argv[1] == 'square':
        square(int(sys.argv[2]))
    elif sys.argv[1] == 'number':
        numberTriangle(int(sys.argv[2]))
    else:
        print('left, right, equi, rect, square, number 중 하나를 선택해주세요!')
