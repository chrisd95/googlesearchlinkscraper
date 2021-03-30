import csv
from googlesearch import search

# Query parameters
query_depth = 100

# Input queries from csv
with open('queries.csv', newline='') as file:
    reader = csv.reader(file)
    queries = list(reader)


for query in queries:
    # Output files
    with open(query[0] + ".csv", 'a',  newline='') as search_results_file:
        writer = csv.writer(search_results_file)
        for i in search(query[0], tld="com", num=query_depth, stop=query_depth, pause=2):
            writer.writerow([i])
