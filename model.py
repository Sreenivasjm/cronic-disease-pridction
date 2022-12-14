from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
import numpy as np
import pandas as pd
import pickle
import os
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
root = os.path.dirname(__file__)
path_df = os.path.join(root, 'dataset/Chronic_final.csv')
data = pd.read_csv(path_df)
cat_cols = ['Age','BP','specific_gravity','Albumin','sugar','Blood_Gluc_rand','Blood_Urea','Serum_Cr','sodium','potassium','hemoglobin',
        'packed_cell_volume','wbc_cnt','htn','diabetes','CAD','apetite','pedal_edema']
X = data.iloc[:, :-1].values
y = data.iloc[:, 18].values
print(X[0:1]) 
#print(data['BP'].head()) 
#print(data['class'].head()) 
Labelx=LabelEncoder()
X[:,13]=Labelx.fit_transform(X[:,13])
X[:,14]=Labelx.fit_transform(X[:,14])
X[:,15]=Labelx.fit_transform(X[:,15])
X[:,16]=Labelx.fit_transform(X[:,16])
X[:,17]=Labelx.fit_transform(X[:,17])


X_train, X_test, Y_train, Y_test = train_test_split(X,y, test_size=0.25)
print("fffffff")
print(X_train[0:1]) 
print(Y_train[0:10])
print("test")
print(X_test[0:1])
print(Y_test[0:1])

#X_train = scaler.fit_transform(X_train)
#X_test = scaler.fit_transform(X_test)

clf = RandomForestClassifier()

# Training the classifier
clf.fit(X_train, Y_train)
#print(X_test[0:1])
#print(clf.predict(X_test[0:1]))

# Testing model accuracy. Average is taken as test set is very small hence accuracy varies a lot everytime the model is trained
acc = 0
acc_binary = 0
for i in range(0, 20):
    Y_hat = clf.predict(X_test)
    Y_hat_bin = Y_hat>0
    Y_test_bin = Y_test>0
    acc = acc + accuracy_score(Y_hat, Y_test)
    acc_binary = acc_binary +accuracy_score(Y_hat_bin, Y_test_bin)

print("Average test Accuracy:{}".format(acc/20))
print("Average binary accuracy:{}".format(acc_binary/20))

# Saving the trained model for inference
model_path = os.path.join(root, 'dataset/rfc.sav')
joblib.dump(clf, model_path)

# Saving the scaler object
scaler_path = os.path.join(root, 'dataset/scaler.pkl')
with open(scaler_path, 'wb') as scaler_file:
    pickle.dump(Labelx, scaler_file)

scaler_path = os.path.join(os.path.dirname(__file__), 'dataset/scaler.pkl')
scaler = None
with open(scaler_path, 'rb') as f:
    scaler = pickle.load(f)

a=64
b=60
c=1.02
d=0
e=0
g=106
h=27	
i=0.7	
j=150	
k=3.3	
l=14.4	
m=42	
n=8100	
o="no"	
p="no"	
q="no"	
r="good"	
s="no"	
t=1
check = np.array([a,b,c,d,e,g,h,i,j,k,l,m,n,o,p,q,r,s]).reshape(1, -1)

Labe=LabelEncoder()
check[:,13]=Labe.fit_transform(check[:,13])
check[:,14]=Labe.fit_transform(check[:,14])
check[:,15]=Labe.fit_transform(check[:,15])
check[:,16]=Labe.fit_transform(check[:,16])
check[:,17]=Labe.fit_transform(check[:,17])
model_path = os.path.join(os.path.dirname(__file__), 'dataset/rfc.sav')

clf = joblib.load(model_path)
B_pred = clf.predict(check[[0]])
if B_pred == 1:
    print("cronical kidney disease detected")
if B_pred == 0:
    print("No disease detected")
