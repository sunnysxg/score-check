import xlrd

score_list = []
score_per = []
k=0

if __name__ == '__main__':

    data = xlrd.open_workbook('score.xlsx')
    table = data.sheet_by_index(0)

    # 得到工作表的行数和列数，便于接下来的循环读取
    number_of_rows = table.nrows
    number_of_cols = table.ncols
    number_of_students = 0

    # 循环读入所有学生成绩，每次循环学生数+1，append即将成绩添加到score_list列表中
    for i in range(1, number_of_rows):
        for o in range(1, number_of_cols):
            k += 1
            score_per.append(table.cell(i,k).value)
            
        score_list.append(score_per)
        number_of_students += 1
        score_per = []
        k=0
        i+=1

    print('排序之前:')
    print(score_list)
    for i in range(0, len(score_list)):
        for j in range(0,len(score_list)-i-1):
            if score_list[j] > score_list[j+1]:
                t = score_list[j]
                score_list[j] = score_list[j+1]
                score_list[j+1] = t

    print('升序排序之后:')
    print(score_list)
