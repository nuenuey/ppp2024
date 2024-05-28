import matplotlib.pyplot as plt
import numpy as np
def main():
    dices = np.random.randint(1, 7, size=100) # random 모듈과 다름
    print(dices)
    plt.hist(dices, bins=6, color="r") #검은색은 k
    plt.show()
    #plt.savefig("./hisrogram.png") #show가 있는채로 저장하면 빈칸이 저장됨

if __name__ == "__main__":
    main()