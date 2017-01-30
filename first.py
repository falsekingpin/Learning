import pandas as pd
import quandl,math,datetime
import numpy as np
from sklearn import preprocessing,cross_validation,svm
from sklearn.linear_model import LinearRegression
from nltk.chunk.util import accuracy
import matplotlib.pyplot as plt
from matplotlib import style
from datetime import date
import time
 
style.use('ggplot') 

df=quandl.get('BSE/BOM500825')

df=df[['Open','High','Low','Close']]
df['Hl_PCT']=(df['High']-df['Low'])/ df['Low'] * 100
df['PCT_change']=(df['Close']-df['Open'])/ df['Open'] * 100

df=df[['Close','Hl_PCT','PCT_change']]

forecast_col='Close'
df.fillna(-9999, inplace=True)

forecast_out=int(math.ceil(0.001*len(df)))
print forecast_out

df['label']=df[forecast_col].shift(-forecast_out)

X=np.array(df.drop(['label'],1))
X=preprocessing.scale(X)
X_lately=X[-forecast_out:]
X=X[:-forecast_out]


df.dropna(inplace=True)
y=np.array(df['label'])

X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2)

clf=LinearRegression(n_jobs=-1)
clf.fit(X, y)
accuracy = clf.score(X, y)
print accuracy 

forecast_set=clf.predict( X_lately)

df['forecast']=np.nan

last_date = df.iloc[-1].name
last_unix = time.mktime(last_date.timetuple())
one_day=86400
next_unix=last_unix+one_day

for i in forecast_set:
    next_date=datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]
    
df['Close'].plot()
df['forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

