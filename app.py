
import streamlit as st

st.header("Flower Classification")


sepal_length = st.number_input("sepal_length number  between : 4.3 to max 7.9")
sepal_width = st.number_input("sepal_width  number between   : 2.0 to max 4.4")
petal_length = st.number_input("petal_length  number between : 1.0  to max 6.9")
petal_width = st.number_input("petal_width number between    : 0.1 to max 2.5")

import pickle
from sklearn import *
# some time later...
 
# load the model from disk
loaded_model = pickle.load(open('irisflower_model.sav', 'rb'))
#result = loaded_model.score(x_test, y_test)
#print(result)
if st.button("Submit"):
    if sepal_length == 0 and sepal_width==0 and petal_length==0 and petal_width==0 :
        st.write("**enter something** inside all of the cell ")
    # elif sepal_width==0 :
    #     st.write("**enter something**")
    # elif petal_length==0 :
    #     st.write("**enter something**")
    # elif petal_width==0:
    #     st.write("**enter something**")
    else:
        result = loaded_model.predict([[sepal_length,sepal_width,petal_length,petal_width]])
        out = str(result)
        st.write("**The Flower type is  : **",out)
