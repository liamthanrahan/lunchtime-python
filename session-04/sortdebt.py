import csv
from operator import itemgetter, attrgetter, methodcaller

def sorted_debt(file_path):
    # your code here
    # do not round your debts in this exercise!
    debts = []
    #leave a 'u' in front of the keys in the dictionary you return
    with open(file_path, 'rU') as csvfile:
        csvData = csv.DictReader(csvfile)
        for row in csvData:
            job_number = int(row['Job Number'])
            debt = float(row['Debt'])
            debts.append({u'job_number': job_number, u'debt': debt})
    return sorted(debts, key=lambda item: item[u'debt'], reverse=True)

# print(sorted_debt('./debts.csv'))

# [
#     {u'job_number': 260405, u'debt': 33209.61},
#     {u'job_number': 233405, u'debt': 22209.16},
#     {u'job_number': 260565, u'debt': 339.10}
# ]