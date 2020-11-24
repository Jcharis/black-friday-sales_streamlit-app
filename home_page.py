import streamlit as st 
import pandas as pd 

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
from wordcloud import WordCloud


@st.cache
def load_data(data):
	df = pd.read_csv(data)
	return df

def run_home_page():
	df = load_data("data/thanksgiving_in_multi_lang.csv")
	# st.dataframe(df)

	
	with st.beta_expander("Happy Thanksgiving Day",expanded=True):
		day_text = " ".join(df['Day'].tolist())
		mywordcloud = WordCloud().generate(day_text)
		fig = plt.figure()
		plt.imshow(mywordcloud,interpolation='bilinear')
		plt.axis('off')
		st.pyplot(fig)


	lang_list = df['Language'].unique().tolist()
	lang_choice = st.sidebar.selectbox("Lang",lang_list)


	if lang_choice:
		thank_word = df[df["Language"] == lang_choice].iloc[0].Word
		thank_day = df[df["Language"] == lang_choice].iloc[0].Day
		st.info("How to Say Happy Thanksgiving in {}".format(lang_choice))
		st.write({"lang":lang_choice,"word":thank_word,"day":thank_day})

	
	name = st.text_input("Name","Streamlit")
	bgcolor = st.beta_color_picker("")
	modified_name = "From {0} {0} {0}".format(name)
	updated_text = []
	updated_text.append(modified_name)
	updated_text.extend(df['Word'].tolist())
	# st.write(updated_text)
	new_text = " ".join(updated_text)


	with st.beta_expander("Thanksgiving From {}".format(name)):
		
		mywordcloud = WordCloud(background_color=bgcolor).generate(new_text)
		fig = plt.figure()
		plt.imshow(mywordcloud,interpolation='bilinear')
		plt.axis('off')
		st.pyplot(fig)



