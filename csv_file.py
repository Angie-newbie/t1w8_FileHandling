import csv

total_goals = 0
with open('euro_cup_matches.csv') as file:
    # read the heading
    content = csv.DictReader(file)
    for row in content:
        total_goals += int(row['Score A']) + int(row['Score B'])
print(f'Total goals in tournament so far is {total_goals}')

    # headings = file.readline().strip()
    # columns = headings.split(',')
    # print(columns)

#  matches = [
#     {
#          'Team A': 'Portugal',
#         'Team B': 'Spain',
#         'Score A': 1,
#         'Score B': 1,
#         'Date': '2024-04-15'
#     }, 
#     {
#          'Team A': 'Germany',
#         'Team B': 'Spain',
#         'Score A': 1,
#         'Score B': 1,
#         'Date': '2024-04-15'
#     }
# ]

with open('new_matches.csv', 'w') as file:
    writer = csv.DictWriter(file, ['Team A', 'Team B', 'Score A', 'Score B', 'Date'])
    writer.writeheader()
    writer.writerow({
        'Team A': 'Portugal',
        'Team B': 'Spain',
        'Score A': 1,
        'Score B': 1,
        'Date': '2024-04-15'
        })
    
