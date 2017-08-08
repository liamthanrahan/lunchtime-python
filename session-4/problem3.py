import csv
# with open("debts.csv", 'rU') as csvfile:
#     csvData = csv.DictReader(csvfile)
#     for row in csvData:
#         job_number = int(row['Job Number'])
#         debt = float(row['Debt']
#         print(job_number, round(debt, 2))

def biggest_debt(file_path):
    job_number = 0
    debt = 0
    with open(file_path, 'rU') as csvfile:
        csvData = csv.DictReader(csvfile)
        for row in csvData:
            curr_debt = float(row['Debt'])
            if curr_debt >= debt:
                job_number = int(row['Job Number'])
                debt = curr_debt
    # your code here
    return {u'job_number': job_number, u'debt': round(debt, 2)}

# print(biggest_debt("debts.csv"))
