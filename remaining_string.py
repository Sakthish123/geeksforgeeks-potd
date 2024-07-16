class Solution:
	def printString(self, s, ch, count):
		for i in range(len(s)):
		    if(ch==s[i]):
		        count-=1
		    if(count==0):
		        if(i==len(s)-1):
		            return ""
		        return s[i+1:]
        return ""
