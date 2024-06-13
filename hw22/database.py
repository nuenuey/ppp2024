import os
import numpy as np
import pickle

DB_FILE = "./grade_db.pkl"
#놀이공원 이용제한
#110cm 이상 탑승가능

def read_db():
    grade_db={}
    if not os.path.exists(DB_FILE):
        return grade_db

    with open(DB_FILE, "rb") as f:
        #grade_db =[float(x) for x in f.readlines().split(",")] #txt 일때는 없애 스플릿
        grade_db= pickle.load(f)
        return grade_db

def write_db(grade_db):
    with open(DB_FILE,"wb") as fout:
        #for x in grade_db:
         #   fout.write(",".join(grade_db))
        pickle.dump(grade_db,fout)

def main():
    user_db_total = read_db()

    #print(f" {grade_total}입니다")
    while True:

        height = float(input("스페인해적선입니다! 저희는 안전상의 이유로 키 제한이 있습니다. 키를 입력해주세요."))
        if height== -1:
            break

        if height < 110:  # 110cm 이하 입력을 중단
            print("죄송합니다. 키가 110cm 이상이어야 탑승가능합니다.")
            continue

        name = input("이름을 입력해주세요: ") #110 이상
        user_db_total[name] = height
        print(f"반갑습니다 {name}님, 입장하셨습니다.")

    print(f"현재까지 입장한 명단: {user_db_total}입니다")
    print(f"총 {len(user_db_total)}명이 입장했습니다.")

    write_db(user_db_total)

   # print(f"닻을 올려라 박수 준비! 하나, 둘, 하나, 둘, 셋, 넷~ 스페인해적선 출발합니다. {np.average(list(grade_total.values())):2f}")


#최고기록 같은 거를 기록, 전에 한 걸 볼 수 있음
#피크를 하면 리드 라이트 써도 상관 없음
if __name__ == "__main__":
    main()
