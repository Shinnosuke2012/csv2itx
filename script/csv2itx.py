import pathlib

def csv2itx(path)->None:
    """convert csv file to itx file
    Args
        path(str):参照するcsvファイルのpath

    """
    input_path = pathlib.Path(path)
    output_path = pathlib.Path(str(input_path).replace(".txt",".itx"))

    input_file = open(input_path, 'r',encoding='utf-8')
    output_file = open(output_path, 'w',encoding='utf-8')
    output_file.write("IGOR\n")
    output_file.write('X NewDataFolder/S/O root:\''+input_path.stem)
    output_file.write('\'\n')
    output_file.write("WAVES/D/O\tVoltage\tStep_charge\tStep_discharge\tStep_charge_discharge\tCycle\tStep\nBEGIN\n")

    for line in input_file:
        splited_line = line.replace(' ','\t')
        output_file.write(splited_line)
    output_file.write('END')
    output_file.write('\n')
    # output_file.close

# csv2itx(path='data/cycle1/modified_data.csv')
