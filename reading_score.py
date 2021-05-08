import plotly.figure_factory as ff 
import statistics
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

reading_scoreList  = df["reading score"]



mean = sum(reading_scoreList)/len(reading_scoreList)
print("reading score mean:", mean)

median = statistics.median(reading_scoreList)
print("reading score Median is: ", median)

mode = statistics.mode(reading_scoreList)
print("reading score mode is:",mode)

std_dev = statistics.stdev(reading_scoreList)
print("Standard Deviation for reading score  is: ",std_dev)

first_std_dev_start,first_std_dev_end = mean-std_dev,mean + std_dev
second_std_dev_start,second_std_dev_end = mean- (2 * std_dev),mean + (2 * std_dev)
third_std_dev_start,third_std_dev_end = mean- (3 * std_dev),mean + (3 * std_dev)


list_data_within_1_std_dev = [result for result in reading_scoreList if result > first_std_dev_start and result < first_std_dev_end]

list_data_within_2_std_dev = [result for result in reading_scoreList if result > second_std_dev_start and result < second_std_dev_end]

list_data_within_3_std_dev = [result for result in reading_scoreList if result > third_std_dev_start and result < third_std_dev_end]

print("{}% of data lies within 1 standard deviation".format(
    len(list_data_within_1_std_dev) * 100.0/len(reading_scoreList) 
))

print("{}% of data lies within 2 standard deviation".format(
    len(list_data_within_2_std_dev) * 100.0/len(reading_scoreList) 
))

print("{}% of data lies within 3 standard deviation".format(
    len(list_data_within_3_std_dev) * 100.0/len(reading_scoreList) 
))


