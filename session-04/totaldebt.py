import csv

def total_debt(file_path):
    total = 0
    with open(file_path, 'rU') as csvfile:
        csvData = csv.DictReader(csvfile)
        for row in csvData:
            job_number = int(row['Job Number'])
            debt = float(row['Debt'])
            total += debt
            # print(job_number, round(debt, 2))
    return round(total, 2)

# print(total_debt('./debts.csv'))
