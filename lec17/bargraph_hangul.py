import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.rcParams['font.family'] = ['NanumGothic', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
    fig, ax = plt.subplots(figsize=(15, 6)) #사이즈 조절
    year = [str(x+2001) for x in range(20)] #20개
    rain = np.random.rand(20) * 200 + 1000 #20개 1000-1200사이
    ax.bar(year, rain, color="b") #(x축, y축) 이렃게 해라
    ax.set_ylabel("연평균강우량(mm)")
    #fig.savefig("./bar_rain.png")
    plt.show()
if __name__ == "__main__":
    main()

    #이거 복붙해서 과제하기