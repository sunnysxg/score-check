import xlrd

score_list = []
score_per = []
k=0

if __name__ == '__main__':

    data = xlrd.open_workbook('score.xlsx')
    table = data.sheet_by_index(0)

    # �õ�����������������������ڽ�������ѭ����ȡ
    number_of_rows = table.nrows
    number_of_cols = table.ncols
    number_of_students = 0

    # ѭ����������ѧ���ɼ���ÿ��ѭ��ѧ����+1��append�����ɼ���ӵ�score_list�б���
    for i in range(1, number_of_rows):
        for o in range(1, number_of_cols):
            k += 1
            score_per.append(table.cell(i,k).value)
            
        score_list.append(score_per)
        number_of_students += 1
        score_per = []
        k=0
        i+=1

    print('����֮ǰ:')
    print(score_list)
    for i in range(0, len(score_list)):
        for j in range(0,len(score_list)-i-1):
            if score_list[j] > score_list[j+1]:
                t = score_list[j]
                score_list[j] = score_list[j+1]
                score_list[j+1] = t

    print('��������֮��:')
    print(score_list)
