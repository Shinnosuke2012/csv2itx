#入力データのうちいくつか理論計算を行い、その結果を出力する
import pathlib
import numpy as np

def modify_data(import_path:str,mass_mc:float,mass_sm:float,mass_ele:float,mass_gr:float,save_path:str)->None:
    """入力CSVデータから理論容量を計算する
    Args
        path(str):参照するcsvfileのpath
        mass_mc(float):合剤の質量
        mass_sm(float):サンプルの質量
        mass_ele(float):電極の質量
        mass_gr(float):グラファイトの質量

    """
    path = pathlib.Path(import_path)
    data_csv = np.genfromtxt(path,delimiter=",",skip_header=2,encoding="shift_jis")
    data_csv = data_csv[:,[1,6,7,8,11,13]]

    ratio_mc = mass_sm/(mass_sm + mass_ele + mass_gr)
    data_csv[:,1] = data_csv[:,1]/(ratio_mc*mass_mc)
    data_csv[:,2] = data_csv[:,2]/(ratio_mc*mass_mc)

    # print(data_csv)
    np.savetxt(save_path,data_csv, delimiter=" ")

# data_path = "data/cycle1/Data_Exp-CCDischarge-1_dat1.csv"
# modify_data(path=data_path,mass_mc=1,mass_sm=2,mass_ele=3,mass_gr=4)
