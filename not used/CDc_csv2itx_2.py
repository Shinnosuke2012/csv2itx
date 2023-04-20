#B室のXRD（.txt）で出力されたファイルの.itxへの変換
# coding: utf-8
#python3 xrd_out2itx.py [入力ファイル名]

import sys
import os
args = sys.argv

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
fo.write("WAVES/D/O\tVoltage\tStepChargeCapacity\tStepDischargeCapacity\tStepChargeDischargeCapacity\tCycleTime\tStepTime\nBEGIN\n")
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
