import os
import numpy as np
import pickle

DB_FILE = "./grade_db.pkl"
def read_db():
    grade_db={}
    if not os.path.exists(DB_FILE):
        return grade_db

    with open(DB_FILE, "rb", encoding="cp949") as f:
        #grade_db =[float(x) for x in f.readlines().split(",")] #txt 일때는 없애 스플릿
        grade_db= pickle.load(f)
        return grade_db

def write_db(grade_db):
    with open(DB_FILE,"wb") as fout:
        #for x in grade_db:
         #   fout.write(",".join(grade_db))
        pickle.dump(grade_db,fout)

def main():
    #grade_total=["프원실"=4.5,"토양학"=4.0]
    grade_total = read_db()

    print(f"현재까지 학점 목록은 {grade_total}입니다")
    while True:

        grade = float(input("학점을 입력해주세요."))
        if grade<0:#학점이 음수일 경우 입력을 중단
            break
        subject = input("과목명을 입력하세요.")
        #grade_total.append(grade)
        grade_total[subject] = grade

    print(f"현재까지 학점 목록은 {grade_total}입니다")
    print(f"평균 학점은 {np.average(list(grade_total.values())):2f}")

    write_db(grade_total)
#최고기록 같은 거를 기록, 전에 한 걸 볼 수 있음
#피크를 하면 리드 라이트 써도 상관 없음
if __name__ == "__main__":
    main()
