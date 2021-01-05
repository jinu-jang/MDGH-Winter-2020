import subprocess
import sys
from os import linesep

tests = [('leftTriangle(1)', 'left', '1', f'*{linesep}'),
         ('leftTriangle(3)', 'left', '3', f'*{linesep}**{linesep}***{linesep}'),
         ('rightTriangle(2)', 'right', '2', f' *{linesep}**{linesep}'),
         ('rightTriangle(4)', 'right', '4', f'   *{linesep}  **{linesep} ***{linesep}****{linesep}'),
         ('equiTriangle(4)', 'equi', '4', f'   *{linesep}  ***{linesep} *****{linesep}*******{linesep}'),
         ('rectangle(6, 3)', 'rect', '6', '3', f'******{linesep}******{linesep}******{linesep}'),
         ('square(5)', 'square', '5', f'*****{linesep}*****{linesep}*****{linesep}*****{linesep}*****{linesep}'),
         ('numberTriangle(5)', 'number', '5', f'1{linesep}12{linesep}123{linesep}1234{linesep}12345{linesep}'),
         ]

correct = 0

for t in tests:
    result = subprocess.run(['python3', sys.argv[1], *t[1:-1]],
                        stdout=subprocess.PIPE) \
                    .stdout \
                    .decode('utf-8')
    if (result == t[-1]):
        print(f'{t[0]} 통과')
        correct += 1
    else:
        print(f'{t[0]} 틀림. 다시 확인해봐요.')

print(f"\n==== {correct}/{len(tests)} 통과 ====")
if (correct == len(tests)):
    print("축하 축하!")
else:
    print("조금만 더 노력해봐요")
