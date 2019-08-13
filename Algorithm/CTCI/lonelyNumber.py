'''
@author: youxinyu
@date: 2018-8-27
@Alg: Find lonely number
@Des: there are a list of numbers. 
All number will appear twice except one number, this number calls lonely.
@type: bit Manipulation
'''

def findLonelyNumber(num):
    result = int()
    for i in num:
        result = i ^ result
    return result

def main():
    print(findLonelyNumber([1,1,4,4,8,8,19,19,11]))

if __name__ == '__main__':
    main()

