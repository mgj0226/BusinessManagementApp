"""
data from fname="midterm2"
data format is SubmissionID,StudentID,Problem,Status,Score,CodeLength,SubmissionTime
Only Problem, Status and SubmissionTime are needed
There are 4 problems: 1,2,3,4
There are 5 kinds of status: Accepted, Compile Error, Runtime Error, Time Limit Exceed, Wrong Answer
Count number of each status for each problem within a time period XX:XX:XX XX:XX:XX
The outcome format should be X X X X X;X X X X X;X X X X X;X X X X X;
"""

import datetime
import os

class Problems:
    def __init__(self, time_period):
        self.time_period = time_period
        self.status_counts = {problem: {status: 0 for status in ["Accepted", "Compile Error", "Runtime Error", "Time Limit Exceed", "Wrong Answer"]} for problem in range(1, 5)}

    def parse_time(self, time_str):
        return datetime.datetime.strptime(time_str.strip(), "%H:%M:%S")

    def is_within_time_period(self, submission_time):
        start_time, end_time = self.time_period.split()
        start_time = self.parse_time(start_time)
        end_time = self.parse_time(end_time)
        submission_time = self.parse_time(submission_time)
        return start_time <= submission_time <= end_time

    def process_data(self, data):
        for line in data:
            parts = line.strip().split(',')
            problem = int(parts[2])
            status = parts[3]
            submission_time = parts[6]
            if self.is_within_time_period(submission_time):
                self.status_counts[problem][status] += 1

    def format_output(self):
        output = []
        for problem in range(1, 5):
            counts = [str(self.status_counts[problem][status]) for status in ["Accepted", "Compile Error", "Runtime Error", "Time Limit Exceed", "Wrong Answer"]]
            output.append(' '.join(counts))
        return ';'.join(output) + ';'

# Example usage:
time_period = "09:20:20 12:20:20"
problems = Problems(time_period)

# get data from file
data = []
# Use an absolute path to the file
fname = "midterm2.csv"

# Print the current working directory for debugging
# print(f"Current working directory: {os.path.abspath(os.getcwd())}")

# Check if the file exists in the specified path
if not os.path.isfile(fname):
    print(f"File {fname} not found in the specified path.")
else:
    with open(fname, 'r') as file:
        data = file.readlines()

    # Skip the header line
    problems.process_data(data[1:])
    output = problems.format_output()
    print(output)