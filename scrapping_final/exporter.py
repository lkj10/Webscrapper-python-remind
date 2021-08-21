import csv

def save_to_file(jobs, word):
    file = open(f"{word}.csv", mode = 'w')
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        try:
            writer.writerow(list(job.values()))
        except:
            pass
    return "Download completed!"