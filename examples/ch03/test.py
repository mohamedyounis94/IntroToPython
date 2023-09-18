import statistics

temp = [19.5,19.5,21.6,20.2,19.7,20.2,18.6,17.2,19.5]

mean = statistics.mean(temp)

median = statistics.median(temp)

mode = statistics.mode(temp)

print('The mean is:',mean,'\nThe median is:',median,'\nThe mode is:',mode)


temp.append(20.2)

try:
    mode = statistics.mode(temp)
    print("Mode after adding 10th day: ", mode)
except statistics.StatisticsError:
    print("No unique mode found after adding 10th day.")