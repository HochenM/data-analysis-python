#Session 9
#Problem - Confusion matrix and metrics
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from docutils.languages.en import labels

#X = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#y_true = np.array([0,0,0,0,1,1,1,1,2,2,2,2,])
#y_predict = np.array([0,0,0,2,1,1,1,1,2,2,2,1])
#df = pd.DataFrame({'X':X,'y':y_true})
#df.columns=['ID',"Real_State"]
#print(df)
#df2 = pd.DataFrame({'X':X,'State':y_predict})
#print(df2)
#labels = [0,1,2]

#cm = np.zeros((len(labels),len(labels)))
#for i, it in enumerate(labels):
  #  for j, lp in enumerate(labels):
 #       cm[i,j]=np.sum((y_true == it) &(y_predict==lp))

#print(cm)
#TP = cm[0,0]
#FP = cm[1,0]
#FN = cm[0,1]






##############
###Part 2 - Use library to calculate TPR and...
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
#X = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#y_true = np.array([0,0,0,0,1,1,1,1,2,2,2,2,])
#y_predict = np.array([0,0,0,2,1,1,1,1,2,2,2,1])
# basic way
#dis = np.c_[X,y_true,y_predict]
#cm_conf = np.zeros((3,3))
#cm_conf = np.zeros((dis.shape[1],dis.shape[1]))
#labels = [0,1,2]
#labels = np.unique(y_true)
#for i,q in enumerate(labels):
  #  for j,w in enumerate(labels):
 #       cm_conf[i,j]= np.sum((y_true==q) & (y_predict==w))


#print(cm_conf)
#print('\n')



# Library
#cm = confusion_matrix(y_true, y_pred=y_predict)
#print(cm)
 # precision and recall and F1-Score
from sklearn.metrics import precision_score, recall_score
#precision= precision_score(y_true, y_predict,average='Macro')
#print(precision)
#recal = recall_score(y_true, y_predict,average='Macro')
#print(recal)
#cm = confusion_matrix(y_true, y_predict)
#print("Confusion matrix:\n", cm)

  #Precision
#precision = precision_score(y_true, y_predict, average='macro')
  #recall
#recall    = recall_score(y_true, y_predict, average='macro')
#print("Precision (macro):", precision)
#print("Recall    (macro):", recall)
  #F1-Score
#f1 = f1_score(y_true, y_predict, average='macro')
#print("F1 score (macro):", f1)


##########
#Part 2 - 9-2
#from sklearn.metrics import classification_report
#X = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#y_true = np.array([0,0,0,0,1,1,1,1,2,2,2,2,])
#y_predict = np.array([0,0,0,2,1,1,1,1,2,2,2,1])
#print(classification_report(y_true, y_predict))



##################### Extra points
#Hands on book: types of gd -sgd mini batch gd etc.
X = 2 * np.random.rand(100,1)
X_b = np.c_[np.ones((100,1)), X]
y = 4 + 3 * X + np.random.randn(100,1)
m = 100
epoch = 50
t0, t1 = 5,50
thetas = np.random.randn(2, 1)
def learning_schedule(t):
    return t0/ (t +t1)
for i in range(epoch):
    for j in range(m):
        random_index = np.random.randint(m)
        xi = X_b[random_index:random_index+1]
        yi = y[random_index]#:random_index+1]
        #why not xi = X_b[random_index] : because it supposes it as a 1D not 2d
        #xi = X_b[random_index].reshape(1, -1)
        #yi = y[random_index].reshape(1, -1)
        gradient = 2 * xi.T.dot(xi.dot(thetas)-yi)
        lr = learning_schedule(i * m +j)
        thetas = thetas - lr * gradient
print(thetas)
#print(xi.shape)
#print(xi)
#print(xi[0].shape)
#print(xi[0:1].shape)
#print(xi[0,0])
#print(xi[0,1])

#plot
X = 2 * np.random.rand(100,1)
X_b = np.c_[np.ones((100,1)), X]
y = 4 + 3 * X + np.random.randn(100,1)
m = 100
epoch = 50
t0, t1 = 5,50
thetas = np.random.randn(2, 1)
#plt.scatter(X,y)
X_new = np.array([[0],[2]])
x_new_b = np.c_[np.ones((2,1)), X_new]
def learning_schedule(t):
    return t0/ (t +t1)
for i in range(epoch):
    for j in range(m):
        random_index = np.random.randint(m)
        xi = X_b[random_index:random_index+1]
        yi = y[random_index]
        gradient = 2 * xi.T.dot(xi.dot(thetas)-yi)
        lr = learning_schedule(i * m +j)
        thetas = thetas - lr * gradient
        y_predict = x_new_b.dot(thetas)
        plt.scatter(X, y)
        plt.plot(X_new,y_predict)

plt.show()



