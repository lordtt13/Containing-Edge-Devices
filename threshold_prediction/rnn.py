# Recurrent Neural Network




import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset=pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
training=dataset.iloc[:,1:2].values

X_train = []
y_train = []
for i in range(30,338):
    X_train.append(training[i-30:i, 0])
    y_train.append(training[i, 0])
X_train, y_train = np.array(X_train), np.array(y_train)


X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))



from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

regressor = Sequential()

regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))


regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

regressor.add(Dense(units = 1))


regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')


regressor.fit(X_train, y_train, epochs = 100, batch_size = 32)






plt.plot(X_train,y_train, color = 'red', label = 'humidity time series')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted  ')

plt.xlabel('Time')

plt.legend()
plt.show()
