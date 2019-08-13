'''
@func: count the brace string's valid pair
@author: youxinyu
@date: 2018-09-05
'''


left_brace = '('
right_brace = ')'

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = [-1]
        maxlen = 0
        for i, c in enumerate(s):
            if(c == '('):
                stack.append(i)
            else:
                stack.pop()
                if(len(stack)):
                    print(stack[-1])
                    maxlen = max(maxlen, i-stack[-1])
                else:
                    stack.append(i)
        # print(stack)
        return maxlen


def count_brace(brace):
    brace = list(brace)
    return _count_brace(brace, len(brace)-1, 0)


def _count_brace(brace, range, count):
    have_left = False
    for i,c in enumerate(brace):
        print(i, c)
        if c == left_brace:
            have_left = True
        else:
            if have_left:
                count += 1
                brace.pop(i)
                brace.pop(i-1)
                return _count_brace(brace, len(brace)-1, count)
    return count

def main():
    
    # count = count_brace('(())()(())))()()')
    # print(count)
    print(Solution().longestValidParentheses('(())()(())))()()'))
    
if __name__ == '__main__':
    main()

