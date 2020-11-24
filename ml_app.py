# Core Pkgs
import streamlit as st 

# Utils
import numpy as np 
import joblib
import os

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

def scale_data(x):
	X = scaler.fit_transform(x)
	return X

age_dict = {'0-17': 1,'55+': 7,'26-35': 3,'46-50': 5,'51-55': 6,'36-45': 4,'18-25': 2}
gender_dict = {"Female":0,"Male":1}
marital_status_dict = {"Single":0,"Married":1}
city_dict = {'A': 0,'B': 1,'C': 2}


def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value 



# Load ML Models
@st.cache
def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


def run_ml():
	st.subheader("Black Friday Sales Predictor")
	col1,col2 = st.beta_columns(2)

	with col1:
		gender = st.radio("Gender",("Female","Male"))
		age = st.number_input("Age",1,75)
		occupation = st.number_input("Occupation",1,20)
		city_category = st.selectbox("City Category",["A","B","C"])
		stay_in_current_city = st.number_input("No of Years of Stay in Current City",1,10)
	
	with col2:
		marital_status = st.radio("Marital Status",("Single","Married"))
		product_category_1 = st.number_input("Product 1",1,20)
		product_category_2 = st.number_input("Product 2",1,20)
		product_category_3 = st.number_input("Product 3",1,20)

	selected_options = {'Gender':gender,'Age':age,'Occupation':occupation, 'City_Category':city_category,
	'Stay_In_Current_City_Years':stay_in_current_city, 'Marital_Status':marital_status, 'Product_Category_1':product_category_1,
	'Product_Category_2':product_category_2, 'Product_Category_3':product_category_3}


	gender_en = get_value(gender,gender_dict)
	city_category_en = get_value(city_category,city_dict)
	marital_status_en = get_value(marital_status,marital_status_dict)
	single_sample = [gender_en,age,occupation,city_category_en,stay_in_current_city,marital_status_en,product_category_1,product_category_2,product_category_2]
	# st.write(single_sample)
	st.write(selected_options)

	if st.button("Predict"):
		# scaled_sample = scale_data(np.array(single_sample).reshape(1,-1))
		# st.write(scaled_sample)
		sample = np.array(single_sample).reshape(1,-1)
		model = load_model("models/lr2_bf_sales_model_23_oct.pkl")
		prediction = model.predict(sample)

		st.info("Predicted Purchase")
		st.write("Purchased:${}".format(prediction[0]))
		st.balloons()