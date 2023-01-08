def missing_char(str, n):
  j=0
  str1=''
  for i in range(0,len(str)):
    if i==n:
      continue
    str1[j]=str[i]
    j+=1
  return str1      
missing_char('kitten',4)