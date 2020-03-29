import pandas as pd
import math

TrainingData = pd.read_csv('E:\Academic\Thesis\data\TrainingDataShuffle.csv')

TrainCSV = pd.DataFrame(columns = ['Old File ID' , 'New File ID' , 'Label'])
TestCSV = pd.DataFrame(columns = ['Old File ID' , 'New File ID' , 'Label'])

Normal = 133
Benign = 437
Malignant = 210

normalCount = 0
benignCount = 0
malignantCount = 0

TestSetPCT = 0.2

TestIdx = 0
TrainIdx = 0

for i in range(780):
    if TrainingData.iloc[i][2] == 0:
        if normalCount < math.floor(Normal * TestSetPCT):
            TestCSV.loc[TrainingData.index[TestIdx]] = TrainingData.iloc[i]
            TestIdx += 1
            normalCount += 1
        else:
            TrainCSV.loc[TrainingData.index[TrainIdx]] = TrainingData.iloc[i]
            TrainIdx += 1
            normalCount += 1
            
    elif TrainingData.iloc[i][2] == 1:
        if benignCount < math.floor(Benign * TestSetPCT):
            TestCSV.loc[TrainingData.index[TestIdx]] = TrainingData.iloc[i]
            TestIdx += 1
            benignCount += 1
        else:
            TrainCSV.loc[TrainingData.index[TrainIdx]] = TrainingData.iloc[i]
            TrainIdx += 1
            benignCount += 1
            
    elif TrainingData.iloc[i][2] == 2:
        if malignantCount < math.floor(Malignant * TestSetPCT):
            TestCSV.loc[TrainingData.index[TestIdx]] = TrainingData.iloc[i]
            TestIdx += 1
            malignantCount += 1
        else:
            TrainCSV.loc[TrainingData.index[TrainIdx]] = TrainingData.iloc[i]
            TrainIdx += 1
            malignantCount += 1
            
    

print(i+1)
print(TrainIdx)
print(TestIdx)

print('Normal Count is: ' , normalCount)
print('Benign Count is: ' , benignCount)
print('Malignant Count is: ' , malignantCount)

TrainCSV.to_csv(r'E:\Academic\Thesis\data\TrainCSV.csv' , index = False , header = True)
TestCSV.to_csv(r'E:\Academic\Thesis\data\TestCSV.csv' , index = False , header = True)