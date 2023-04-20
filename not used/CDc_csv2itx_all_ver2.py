import re, os, glob, shutil, argparse
import sys
import os
import glob
args = sys.argv
# def change():
#   csv2itx()
# done

def csv2itx(a,b,c,d):
  print(args[1])

  ifname = args[1]    #入力ファイル名
  ofname = ifname[:-4] + ".itx"   #出力ファイルの拡張子をitxに
  basename = os.path.basename(ifname)
  newname = basename[:-4]
  lines = []          #ファイルをただ一行ずつ読み込んだだけ

  fi = open(ifname, 'r', encoding='SHIFT-JIS')
  import re
  i=0
  #write
  fo = open(ofname, 'w', encoding='SHIFT-JIS')
  fo.write("IGOR\n")
  fo.write('X NewDataFolder/S/O root:\''+newname)
  fo.write('\'\n')
  fo.write("WAVES/D/O\tVoltage\t RawStepChargeCapacity\t RawStepDischargeCapacity\tCycleTime\tStepTime\tNormalizedStepChargeCapacity\tNormalizedStepDischargeCapacity\nBEGIN\n")
  for line in fi:
    i=i+1
    if i>=3:
      list=line.split(",")
      Voltage=list[1]
      Raw_Step_charge_capacity=list[6]
      Raw_Step_discharge_capacity=list[7]
      Cycle_time=list[11]
      Step_time=list[13]
      NormalizedStepChargeCapacity=Raw_Step_charge_capacity*(float(b)+float(c)+float(d))/float(a)
      NormalizedStepDischargeCapacity=Raw_Step_discharge_capacity*(float(b)+float(c)+float(d))/float(a)
      fo.write(str(Voltage)+'\t'+str(Raw_Step_charge_capacity)+'\t'+str(Raw_Step_discharge_capacity)+'\t'+str(Cycle_time)+'\t'+str(Step_time)+'\t'+str(NormalizedStepChargeCapacity)+'\t'+str(NormalizedStepDischargeCapacity))
    fo.write('\n')
  fo.write('END')
  #fo.write('\n')
  #fo.write('X AppNormPatt()')	#itx内にマクロも書き込みたい場合は#を消す
  fo.close



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
  # for file in `\find . -maxdepth 1 -type f -name '*.csv'`; do
  # for file in f:
    for '*.csv' in glob.glob('./test/*.txt'):
      if '*.csv' in file:
      csv2itx(float(a),float(b),float(c),float(d))
      print(args[1])

          # ifname = args[1]    #入力ファイル名
          # ofname = ifname[:-4] + ".itx"   #出力ファイルの拡張子をitxに
          # basename = os.path.basename(ifname)
          # newname = basename[:-4]
          # lines = []          #ファイルをただ一行ずつ読み込んだだけ

          # fi = open(ifname, 'r', encoding='SHIFT-JIS')
          # import re
          # i=0
          # #write
          # fo = open(ofname, 'w', encoding='SHIFT-JIS')
          # fo.write("IGOR\n")
          # fo.write('X NewDataFolder/S/O root:\''+newname)
          # fo.write('\'\n')
          # fo.write("WAVES/D/O\tVoltage\t RawStepChargeCapacity\t RawStepDischargeCapacity\tCycleTime\tStepTime\tNormalizedStepChargeCapacity\tNormalizedStepDischargeCapacity\nBEGIN\n")
          # for line in fi:
          #   i=i+1
          #   if i>=3:
          #     list=line.split(",")
          #     Voltage=list[1]
          #     Raw_Step_charge_capacity=list[6]
          #     Raw_Step_discharge_capacity=list[7]
          #     Cycle_time=list[11]
          #     Step_time=list[13]
          #     NormalizedStepChargeCapacity=Raw_Step_charge_capacity*(float(b)+float(c)+float(d))/float(a)
          #     NormalizedStepDischargeCapacity=Raw_Step_discharge_capacity*(float(b)+float(c)+float(d))/float(a)
          #     fo.write(str(Voltage)+'\t'+str(Raw_Step_charge_capacity)+'\t'+str(Raw_Step_discharge_capacity)+'\t'+str(Cycle_time)+'\t'+str(Step_time)+'\t'+str(NormalizedStepChargeCapacity)+'\t'+str(NormalizedStepDischargeCapacity))
          #   fo.write('\n')
          # fo.write('END')
          # #fo.write('\n')
          # #fo.write('X AppNormPatt()')	#itx内にマクロも書き込みたい場合は#を消す
          # fo.close
  os.chdir('../')