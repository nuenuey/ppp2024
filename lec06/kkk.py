eat_fruit_dic={"딸기"}





total_cal =0
idx= 0
for eat_fruit, eat_gram in eat_fruits_dic.item():
    for fruits in cal:
        if eat_fruit == fruits:
            total_cal += cal[fruits] * eat_gram
