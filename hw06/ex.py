def add(x,y): #함수이름
    return x+y #계산식

print(add(3,4))
#-----------------
def add(x,y): 
    return x+y

if __name__=="__main__":
    print(add(3,4))

def f(x):
    x+1
#--------------------------------------------
def f2c(temp_f):
    return  (temp_f - 32)*5/9


temp_f = int(input("화씨온도를 입력하시오"))
print("{}F => {}C" .format(temp_f,f2c(temp_f)))