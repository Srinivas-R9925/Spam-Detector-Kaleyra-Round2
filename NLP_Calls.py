import pandas as pd
import matplotlib.pyplot as plt

from NLP import VizHistogram, VizWordCloud, Format, Predict, VizReport

dataset = pd.read_csv('spam.csv', encoding='latin-1')

Format(dataset)

VizHistogram(dataset)
VizWordCloud(dataset, 'spam')
VizWordCloud(dataset, 'ham')

[predictedLabelsNB,trueLabelsNB], classificationReportNB, confusionMatrixNB = Predict(dataset,'NB')

fig, (ax1,ax2) = plt.subplots(1,2)

print('NB: \n')
VizReport(classificationReportNB, confusionMatrixNB, ax=ax1)

plt.show()