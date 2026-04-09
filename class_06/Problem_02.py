def check(n):
      j=len(n)
      for i in range (len(n)//2):
          if n[i]!=n[j-1]:
              return False
          j-=1
      return True

print(check("A man, a plan, a canal: Panama"))