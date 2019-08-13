#!/usr/bin/env python
import sys
def decomp(text, start=0, times=1):
	l = []
	for i in text:
		
		if i == "]":
			s = ""
			n = 0
			i = 0
			while l[-1] != "[":
				s += (l.pop())

			if l[-1] == "[":
				l.pop()
				while len(l) != 0 and l[-1].isdigit():
					n += (10**i) * int(l.pop())
					i += 1
			
			s = s * n
			
			for i in s[::-1]:
				l.append(i)
	
		else:
			l.append(i)

	return "".join(l)

def decomp2(text, start=0, times=1):
	l = []
	for i in text:
		if i != "]":
			l.append(i)
		else:
			s = ""
			n = 0
			i = 0
			while l[-1] != "[":
				s += (l.pop())

			if l[-1] == "[":
				l.pop()
				while len(l) != 0 and l[-1].isdigit():
					n += (10**i) * int(l.pop())
					i += 1
			
			s = s * n
			for i in s[::-1]:
				l.append(i)
	return "".join(l)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = [['', 1, '']]
        a = n = ''
        for c in s:
            if c.isalpha():
                a += c
            elif c.isdigit():
                n += c
            elif c == '[':
                stack.append([a, int(n), ''])
                a = n = ''
            else:
                p, t, b = stack.pop()
                stack[-1][-1] += p + t * (b + a)
                a = ''
        return stack.pop()[-1] + a

if __name__ == "__main__":
	s = "2[abc3[v]]y"
	print(decomp(s))
	print(Solution().decodeString(s))
    # abcvvvabcvvvy

# #!/usr/bin/env python
# import sys
# def decomp(text, start=0, times=1):
#     """
#     Iterate over and decompress the compressed string.
#     This approach makes use of nested Python iterators, which is a very clean way
#     of expressing expansion of nested iterated items.
#     Args:
#         text: The entire string to decompress.  It's unobvious, but nice
#           to have the whole string plus an index; this allows any error
#           detection code to report the absolute index of a problematic
#           character.
#         start: The starting index within 'text'.  We decompress from
#           'start' up through the matching close-brace or end-of-string.
#         times: The number of times to repeat decompression.
#     """
# # Repeat iteration over our sub-chunk N times.
# for _ in xrange(times):
#     i = start
#     # Until we hit the end of the string, or end of our chunk...
#     while i < len(text) and text[i] != ']':
#         # Emit letters as themselves.
#         if text[i].islower():
#             yield text[i]
#     # If it's not a letter, it must be digit(s).  Convert to integer.
#     else:
#         sub_times = 0
#         while text[i].isdigit():
#             sub_times = sub_times * 10 + int(text[i])
#             i += 1
#         i += 1  # Skip past open-bracket
#         # Start an iterator over the sub-chunk.
#         for item in decomp(text, i, sub_times):
#             # Iterator generates many characters, and then at the very end,
#             # it generates an integer.  Provide characters up to our caller,
#             # and use the integer to advance our index 'i' to end-of-chunk.
#             if isinstance(item, basestring):
#                 yield item
#             else:
#                 i = item
#         # Advance 'i' to the next letter, or skip the close-bracket, whichever.
#         i += 1
# # Don't emit the trailing integer if we are doing the outermost call.  This
# # test could be moved to the decompress() call instead; we would check there
# # to see if the result item was basestring or int, just as we do above, but
# # I suspect that check would be more expensive than a simple integer
# # comparison here, where the type is known.
# if start > 0:
#     yield i
# def decompress(text):
#     # We could wrap 'text' to add a leading '1[' and trailing ']' to allow a
#     # little bit of simplification in the logic in decomp(), but the
#     # simplification would lead to harder-to-read code, as well as requiring
#     # O(n) additional time, and a temporary requirement for O(n + 3) additional
#     # space during the copy operation.
#     #
#     # This is O(decompressed-length) for speed (probably), and up to
#     # O(compressed-length/4) for additional storage.  In this implementation,
#     # the storage requirement is well-disguised: It appears on the function call
#     # stack, rather than in declared variables.  E.g., consider a worst-case
#     # input of: 1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[xx]]]]]]]]]]]]]]]]]]]]
#     # which would require a stack depth of 20.
#     #
#     # The (probably) for the big-O depends on how well Python implements
#     # resumption of nested iteration.  At worst, the string above would require
#     # a full stack descent, then ascent for *each* of the two 'x' characters,
#     # for a total of O(n^2) time.  Another very well-hidden possible cost.
#     for letter in decomp(text):
#         sys.stdout.write(letter)
#     sys.stdout.write('
# ')
#     if __name__ == '__main__':
#         decompress(sys.argv[1])


# # This reference program is provided by @jiuzhang.com
# # Copyright is reserved. Please indicate the source for forwarding

# class Solution:
#     """
#     @param s: an expression includes numbers, letters and brackets
#     @return: a string
#     """
#     def expressionExpand(self, s):
#         stack = []
#         for c in s:
#             if c != ']':
#                 stack.append(c)
#                 continue
                
#             strs = []
#             while stack and stack[-1] != '[':
#                 strs.append(stack.pop())
            
#             # skip '['
#             stack.pop()
            
#             repeats = 0
#             base = 1
#             while stack and stack[-1].isdigit():
#                 repeats += (ord(stack.pop()) - ord('0')) * base
#                 base *= 10
#             stack.append(''.join(reversed(strs)) * repeats)
        
#         return ''.join(stack)