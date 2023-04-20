import re, os, glob, shutil, argparse
# 移動先のフォルダ名入力
Name = input('Enter folder name : ')
# 理論容量計算用の数値入力
a = input('Compound weight(g) : ')
b = input('Sample weight(g) : ')
c = input('LiBH4 weight(g) : ')
d = input('Carbon weight(g) : ')

# フォルダ内の各サイクルごとのフォルダ名入手
filelist = []
for f in os.listdir(Name):
  if os.path.isdir(os.path.join(Name, f)):
    filelist.append(f)
    
# 変換用プログラム実行
os.chdir(Name)
for f in filelist:
  os.chdir(f)
  os.system("../.././CDc_csv_3.sh")
  os.chdir('../')