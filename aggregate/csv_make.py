import re
import os
import pandas as pd


def main(csv):
    base_dir = os.getcwd()
    data = pd.read_csv(r"{}".format(base_dir + csv),encoding="shift_jis")
    data = data.drop(["支払元","品目","メモ","お店","通貨","残高調整","通貨変換前の金額","集計の設定",], axis=1)
    data = data[data["方法"] != "balance"]
    data_sum = data["支出"]+data["収入"]+data["振替"]
    data2 = pd.DataFrame({"合計":data_sum})
    data = pd.concat([data, data2], axis=1)
    data = data.drop(["支出","収入","振替",],axis=1)
    data = data.reset_index(drop=True)
    return data

    
#main("\\zaim_201912.csv")