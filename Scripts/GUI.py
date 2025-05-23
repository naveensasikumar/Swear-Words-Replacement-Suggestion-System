#!C:\Users\Naveen\AppData\Local\Programs\Python\Python38\python.exe
import cgi, cgitb
# Create instance of FieldStorage
print("Content-type:text/html\r\n")
form = cgi.FieldStorage()
# Get data from fields
text= str(form.getvalue('text'))
a=text.split()
b=[]
import joblib
tokenizer=joblib.load('tokenizer_2')
embedding_matrix=joblib.load('embedding')
from tensorflow import keras
model = keras.models.load_model('model_2')
from tensorflow.keras.preprocessing.sequence import pad_sequences
sequences = tokenizer.texts_to_sequences([text])
x = pad_sequences(sequences, maxlen = 20)
sentiment = model.predict(x)[0][0]
#print('sentiment')
#print(str(sentiment))
import pandas as pd
df=pd.read_csv("Swear Words Replacement.csv")
df.columns=['bad_words','food']
X=df['bad_words'].values.tolist()
y=df['food'].values.tolist()
if sentiment >= 0.5:
	for i in a:
		if i in X:
			c=X.index(i)
			d=y[c]
			b.append(d)
			text=text.replace(i,d)	
a=text.split()
print("")
print("")
print("")
print("")
print("<html><head><link rel='stylesheet' href='a.css'/></head><body bgcolor=yellow>")
print("<div id='container'>")
for x in a:
	if x in b:
		print("<li style='color:red;display:inline;'>"+x)
	else:
		print("<li  style='color:yellow;display:inline;'>"+x)

print("</p></div>")
print("</body></html>")