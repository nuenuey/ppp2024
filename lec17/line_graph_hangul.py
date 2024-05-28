import matplotlib.pyplot as plt
import numpy as np
def main():
    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
    #한글로 쓰고 싶을 때


    tmax = np.random.rand(30) * 15 + 15 #numpy를 랜덤하는데 난수를 30개 만들어줌(15-30사이 숫자를 30개 줌)
    tmin = tmax - (np.random.rand(30) * 5 + 5) #숫자를 30개 30개 만듦

    plt.plot(tmax, color="r", label="최고기온")
    plt.plot(tmin, color="b", label="최저기온")
    #그래프가 2개그려짐

    plt.ylabel("기온(℃)") #y축이름
    plt.legend()
    plt.show()
    #plt.savefig("./line_temp_hangul.png")
if __name__ == "__main__":
    main()