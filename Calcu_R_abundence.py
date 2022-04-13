#本脚本用于将转换不同样本中微生物的TPM丰度为一种比例丰度
#相对丰度=（TPM丰度/样本中所有TPM丰度总和）*1000
import xlwt
import xlrd

path = ''#操作文件文件夹的绝对路径
filename = ''#操作文件文件名
rf = xlrd.open_workbook(path + filename)
rf_sheet = rf.sheet_by_index(0)
nrows = rf_sheet.nrows
ncols = rf_sheet.ncols

f = xlwt.Workbook()
f_sheet: object = f.add_sheet('sheet1', cell_overwrite_ok=True)

tox_names = rf_sheet.col_values(0, 0, nrows)
n = 0
for tox in tox_names:
    f_sheet.write(n, 0, tox)
    n += 1

for i in range(1, ncols):
    one_sample_conp = rf_sheet.col_values(i, 0, nrows)

    sum = 0
    for s in one_sample_conp:
        sum += s

    r = 0
    for s in one_sample_conp:
        r_abundance = s/sum*1000
        f_sheet.write(r, i, r_abundance)
        r += 1

f.save(path+'')#保存文件名