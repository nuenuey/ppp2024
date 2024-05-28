import matplotlib.pyplot as plt
import numpy as np
def main():

    tmax = np.random.rand(30) * 15 + 15 #numpy를 랜덤하는데 난수를 30개 만들어줌(15-30사이 숫자를 30개 줌)
    tmin = tmax - (np.random.rand(30) * 5 + 5)
    #숫자를 30개 30개 만듦

    plt.plot(tmax, color="r", label="최고기온") #선그래프를 그려줌 (30개 점을 이은 선그래프)
    plt.plot(tmin, color="b", label="최저기온")
   #두개의 선그래프 그러짐

    plt.ylabel("기온(℃)")#y축 이름
    plt.legend()#색깔에 대한 이름 그러줌
    plt.show()#로컬시 그려짐
    #plt.savefig("./line_temp.png")#파일로 저장
