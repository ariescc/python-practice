from xlwt import *
import random

file = Workbook(encoding = 'utf-8')

table = file.add_sheet('aaa')

def randNum():
    numa = random.randint(0, 10)
    numb = random.randint(0, 10)
    numc = random.randint(0, 10)
    numd = random.randint(0, 10)

    maxium = max(numa, numb, numc, numd)
    minium = min(numa, numb, numc, numd)

    scorea = numa
    scoreb = numb
    scorec = numc

    res = ""
    res = str(numa) + " " + str(numb) + " " + str(numc) + " " + str(numd) + " " + str(scorea) + " " + str(scoreb) + " " + str(scorec)

    return res

if __name__ == '__main__':
    for row in range(60):
        tmp = randNum()
        resp = tmp.split(" ")
        for col in range(7):
            table.write(row, col, resp[col])

    file.save('Q:\\mcm\\result.xls')