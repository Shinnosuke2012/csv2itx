#B室のXRD（.txt）で出力されたファイルの.itxへの変換
# coding: utf-8
#python3 xrd_out2itx.py [入力ファイル名]

import sys
import os
args = sys.argv
def sum(a,b,c,d,i):

print(args[1])

ifname = args[1]    #入力ファイル名
ofname = ifname[:-4] + ".itx"   #出力ファイルの拡張子をitxに
basename = os.path.basename(ifname)
newname = basename[:-4]


#測定データ抽出
#*****TGの出力ファイルはエンコーディングがShift-JIS*****
# fi = open(ifname, encoding = 'Shift-JIS', mode = 'r')
# input_list = []
# for input_line in tqdm(fi, desc = 'Reading Measurement Data Progress : ', leave = 0):
# 	if r.match(input_line):
# 		splitted_list = input_line.split()
# 		del splitted_list[2:4]
# 		del splitted_list[3]
# 		input_list.append(splitted_list)
# 	if re.match('サンプル重量', input_line):
# 		sample_weight_list = input_line.split()
# 		sample_weight = sample_weight_list[1]

#pandasで加工
# df = pd.DataFrame(input_list, dtype = float, columns = ['Time', 'WeightChange_notCorr', 'SampleTemperature'])
# df['WeightChange_background'] = bg_ds
# df['SampleWeight'] = float(sample_weight)
# df['SampleWeightChange'] = df['SampleWeight'] + df['WeightChange_notCorr'] - df['WeightChange_background']
# df['WeightChangeRate'] = df['SampleWeightChange'] / df['SampleWeight'] *100
# input_list = df.values.tolist()
# df.to_excel(str(os.path.splitext(basename)[0]) + '.xlsx')



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
		fo.write(str(Voltage)+'\t'+str(Raw_Step_charge_capacity)+'\t'+str(Raw_Step_discharge_capacity)+'\t'+str(Cycle_time)+'\t'+str(Step_time)'\t'+str(NormalizedStepChargeCapacity)'\t'+str(NormalizedStepDischargeCapacity))
	fo.write('\n')
fo.write('END')
#fo.write('\n')
#fo.write('X AppNormPatt()')	#itx内にマクロも書き込みたい場合は#を消す
fo.close
