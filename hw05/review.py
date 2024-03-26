#별
n=5
for i in range(n):
    star=i+1
    print("*" * star)

#for i in range(n):
 #   for j in range(i+1):
  #       print("*",end="")
   # print()

for i in range(n):
   num_star=i+1
   num_space=n - num_star
   print(" " * num_star + "*" * num_star)

