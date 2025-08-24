
def removeOutermostParentheses(self, s: str) -> str:
   count = 0
   ans = []
   for ch in s:
       if ch == '(':
           if count != 0:
               ans.append(ch)
           count += 1
       else:
           count -= 1
           if count != 0:
               ans.append(ch)
   return ''.join(ans)


if __name__ == "__main__":
   s = input()
   ans = removeOutermostParentheses(s)
   print(ans)
