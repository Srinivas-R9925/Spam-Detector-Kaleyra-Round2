import seaborn as sn
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix


def Format(dataset):
    dataset.drop(columns='Unnamed: 0', inplace=True) 
    dataset['length'] = dataset['SMS'].apply(len) 
    # dataset['label'] = dataset['label'].map({'ham': 0, 'spam': 1}, inplace=True) 
    
def VizHistogram(dataset):
    dataset['length'].plot(bins=100, kind='hist', cmap='coolwarm') 
    dataset.hist(column='length', by='label', bins=100, figsize=(12,4)) 
    
def VizWordCloud(dataset,cat):
    words = ' '.join(list(dataset[dataset['label'] == cat]['SMS']))
    wordCloud = WordCloud(width=512, height=512).generate(words)
    plt.figure(figsize=(10,8), facecolor='k')
    plt.imshow(wordCloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    
def VizReport(clreport, cm, ax):
    print(clreport)
    dfCM = pd.DataFrame(cm, index=[['actual','actual'],['ham','spam']], columns=[['predicted','predicted'],['ham','spam']])
    sn.heatmap(dfCM, annot=True, annot_kws={"size": 16}, fmt='g', ax=ax)
    

def TextProcess(sms):
    noPunctuationSMS = [c for c in sms if c not in string.punctuation] 
    noPunctuationSMS = ''.join(noPunctuationSMS) # on reforme le message
    return [word for word in noPunctuationSMS.split() if word.lower() not in stopwords.words('english')] 


def Predict(dataset, model='NB'):

    smsTrain, smsTest, labelTrain, labelTest = train_test_split(dataset['SMS'], dataset['label'], test_size=0.25)

    pipeline = Pipeline([
        ('bow', CountVectorizer(analyzer=TextProcess)),
        ('tfidf', TfidfTransformer()),
        ('classifier', MultinomialNB()),
        ])
           
    
    pipeline.fit(smsTrain, labelTrain) # fitting
    predictions = pipeline.predict(smsTest) # prediction
    predVStrue = [predictions,labelTest]
    
    return(predVStrue, classification_report(predictions, labelTest), confusion_matrix(labelTest,predictions))



def Predict_A_Message(Message):

    data = pd.read_csv("spam_data.csv",encoding='latin-1')
    data=data.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
    data=data.rename(columns={"v1":"label","v2":"text"})
    data.tail()
    data['label_num'] = data.label.map({'ham':0, 'spam':1})

    X_train,X_test,y_train,y_test = train_test_split(data["text"],data["label"], test_size = 0.2, random_state = 10)

    Predict_Text = [Message]

    vect = CountVectorizer()
    vect.fit(X_train)#bag of words
    X_train_df = vect.transform(X_train)#creates the vector array for train data
    X_test_df=vect.transform(X_test)#creates the vector array for test data

    Predict_Text_DF = vect.transform(Predict_Text)

    prediction = dict()

    model = MultinomialNB()
    model.fit(X_train_df,y_train)
    prediction["Result"] = model.predict(Predict_Text_DF)
    
    Pred = ' '.join([str(elem) for elem in prediction["Result"]])
    
    print(Pred)
    
    if(Pred=='spam'):
        return 1
    elif(Pred=='ham'):
        return 0



    
    
    
