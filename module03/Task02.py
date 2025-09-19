x = 30 # Try x = 3 and x = 30
y = None
for i in range(10):
    if i%2 == 0:
        x += i
        print(x,i)
    if x >= 11 and x < 20:
        y=x*i
        print(x,y)
    else: 
        y = x + i
        print(x,y)
    while x < 10:
         x = x + 1
         print(x,y)
    if y > 20:
         break
         print(x,y)
    if y > 10:
         print(x,y,i)
         continue
         print(x,y,i)
    x = x + 1
    print(x,y,i)
print(x, y, i)
