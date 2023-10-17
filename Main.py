import subprocess
from datetime import date


script_path1 = 'NewsScraperV1.py'
script_path2 = "CurrentTrends.py"

subprocess.run(['python', script_path1], check=True)
subprocess.run(['python', script_path2], check=True)


# Define the file paths
file1_path = "NewsScraped" + str(date.today()) + ".txt"
file2_path = "TrendingTopics" + str(date.today()) + ".txt"

# Open the first file
try:
    with open(file1_path, 'r') as file1:
        content1 = file1.read()
    with open(file2_path, 'r') as file2:
        content1 = file2.read()
except FileNotFoundError:
    print(f"File '{file1_path}' not found.")
    print(f"File '{file1_path}' not found.")
    

# Open the second file
try:
    with open(file2_path, 'r') as file2:
        content2 = file2.read()
except FileNotFoundError:
    print(f"File '{file2_path}' not found.")
    content2 = ''

# Print the contents of both files
print("Contents of file1:")
print(content1)

print("\nContents of file2:")
print(content2)
