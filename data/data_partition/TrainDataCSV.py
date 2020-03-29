import pandas as pd

Normal =  ['Normal(' + str(i+1) + ').png' for i in range(133)]
Benign= ['Benign(' + str(i+1) + ').png' for i in range(437)]
Malignant = ['Malignant(' + str(i+1) + ').png' for i in range(210)]

OldFileId = Normal + Benign + Malignant
NewFileId = [str(i) + '.png' for i in range(780)]

NormalLabel = [0 for i in range(133)]
BenignLabel = [1 for i in range(437)]
MalignantLabel = [2 for i in range(210)]

Labels = NormalLabel +  BenignLabel +  MalignantLabel

data = {'Old File ID' : OldFileId,
        'New File ID' : NewFileId,
        'Label' : Labels}

df = pd.DataFrame(data)
df.to_csv(r'E:\Academic\Thesis\data\TrainingData.csv' , index = False , header = True)