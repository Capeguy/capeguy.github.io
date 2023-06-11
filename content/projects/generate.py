import csv
from datetime import datetime

with open('certifications.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        date_issued = datetime.strptime(row['Date Issued'], '%B %d, %Y').strftime('%Y-%m-%d')
        skills = row['Skills'].split(', ')
        filename = row['CourseName'].replace(' ', '_').replace('/', '_') + '.md'
        with open(filename, 'w') as f:
            f.write('---\n')
            f.write(f"date: '{date_issued}'\n")
            f.write(f"title: '{row['CourseName']}'\n")
            f.write(f"external: '{row['URL']}'\n")
            f.write('tech:\n')
            for skill in skills:
                f.write(f"  - {skill}\n")
            f.write(f"company: {row['Institution']}\n")
            f.write('showInProjects: false\n')
            f.write('---\n')