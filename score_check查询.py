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
        for o in range(1, number_of_cols + 1):
            
            score_per.append(table.cell(i,k).value)
            k += 1
        score_list.append(score_per)
        number_of_students += 1
        score_per = []
        k=0
        i+=1

    
student_list = [row[0]for row in score_list]
print(student_list)
print("input a number list ahead")
print("please give the sutden's number")
student = int(input("Enter your input: "))
print("which subject?\n 1means Chinese,2meansMaths,3meansEnglish")
subject=int(input("Enter your input: "))
num=student_list.index(student)
print("the student's score is:")
print(score_list[num][subject])
print("thanks for useing")
#刚刚开始学python做的有点粗糙，比如说在错误的时候怎么停止程序或者在用完一次之后回到开始……大概要用for循环？
