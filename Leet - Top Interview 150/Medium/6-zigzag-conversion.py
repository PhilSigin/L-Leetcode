"""
6. Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

My solution:
Runtime  39ms  Beats 96.45%
Memory 16.70MB Beats 50.52%


Another elegant solution

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        val=0
        dir=1
        rows = [[] for _ in range(numRows)]
        for char in s:
            rows[val].append(char)
            if val == 0:
                dir = 1
            elif val == numRows - 1:
                dir = -1
            val =val+ dir
        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)  


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows  < 2):
            return s
        arr = ['' for i in range(numRows)]
        direction = 'down'
        row = 0
        for i in s:
            arr[row] += i
            if row == numRows-1:
                direction = 'up'
            elif row == 0:
                direction = 'down'
            if(direction == 'down'):
                row += 1
            else:
                row -= 1
        return(''.join(arr))



"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or len(s) == 1:
            return s

        answer = ""

        l = len(s)

        main_step = (numRows-1) * 2

        def steps(cur_step):
            step_big = main_step - (cur_step*2)
            step_small = main_step - step_big
            return step_big, step_small

        for i in range (numRows):
            cur_pos = i
            step_big, step_small = steps(i)

            if (cur_pos < l):
                answer += s[cur_pos]

            else:
                return answer


            while True:

                if step_big != 0:
                    cur_pos += step_big
                    if (cur_pos < l):
                        answer += s[cur_pos]

                    else:
                        break


                if step_small != 0:
                    cur_pos += step_small
                    if (cur_pos < l):
                        answer += s[cur_pos]

                    else:
                        break

        return answer
