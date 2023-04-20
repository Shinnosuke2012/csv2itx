import argparse
import pathlib
from script.data_modification import modify_data
from script.csv2itx import csv2itx

parser = argparse.ArgumentParser(description='argument parser')
num = len(list(pathlib.Path("data").glob("*")))

parser.add_argument('-arg1')
parser.add_argument('-arg2')
parser.add_argument('-arg3')
parser.add_argument('-arg4')
args = parser.parse_args()

for i in range(num):
    parent_dir = f"data/cycle{i+1}"
    parent_dir = pathlib.Path(parent_dir)

    for j,path in enumerate(list(parent_dir.glob("*.csv"))):
        print(f"{i+1}/{num}")
        print(path)

        #質量の値等は実験によって変わる
        modify_data(import_path=path,
                    mass_mc=float(args.arg1),
                    mass_sm=float(args.arg2),
                    mass_ele=float(args.arg3),
                    mass_gr=float(args.arg4),
                    save_path=str(parent_dir)+f"/modified_data{j+1}.txt")
        csv2itx(path=str(parent_dir)+f"/modified_data{j+1}.txt")
        print("done.")
        print("-"*20)
