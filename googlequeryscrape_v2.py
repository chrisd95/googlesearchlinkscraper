import csv
from googlesearch import search

# Query parameters

# From 1 to 100
results_per_page = 100

# From 1 to X
total_results = 1000


# Input queries from csv
with open('./input/queries.csv', newline='') as file:
    reader = csv.reader(file)
    queries = list(reader)


for query in queries:
    # Output files
    with open("./output/" + query[0] + ".csv", 'a',  newline='') as search_results_file:
        writer = csv.writer(search_results_file)
        for i in range(total_results // results_per_page):
            for j in search(query[0], tld="com", num=results_per_page, stop=None, start=i*results_per_page, pause=10):
                writer.writerow([j])
