import pandas as pd 
import matplotlib.pyplot as plt
import requests 
import streamlit as st 
import random
from bs4 import BeautifulSoup as bs
pd.set_option("display.max_columns", None)


@st.cache()
def search_df():
	url = requests.get("https://www.espn.com/mlb/team/stats/_/name/wsh")
	soup = bs(url.content, "html.parser")#features="lxml")
	box = soup.find_all('table')
	orig_df = pd.read_html(str(box))[3]
	name_df = pd.read_html(str(box))[2]
	search_df = pd.concat([name_df, orig_df], axis = 1)
	print(search_df.info())
	return search_df



def run_stream():
	grab_df = search_df()
	st.title('Washington Nationals MLB Stats Explorer')
	st.markdown('''
	Description: This app allows Washington Nationals fans to turn MLB ESPN data
	into chart form! It displays the chart above the raw data.
	* *Data Source: ESPN.
	* *Chart Source: Justin & You!

	''')
	st.sidebar.header('* Create Chart Below *')
	select_field = st.sidebar.selectbox('PICK A STAT', list(search_df().columns))
	#select_stats = st.sidebar.selectbox('PLAYER OPS', list(search_df().OPS))
	#combo_df = pd.concat([grab_df['Name'], grab_df[{inquiry}]], axis = 1 )
		
	
	patterns = ["*o*","oxo"", *x*x",
	        "o+o", "xx", "\\o\\o",
	         "\\*\\*"]
 

	choice_patterns = random.choice(patterns)

	text_font = {'family': 'monospace',
	        'color':  'darkred',
	        'style': 'oblique',
	        'weight': 'black',
	        'size': 14,
	        }

	big_font = {'family': 'sans-serif',
	        'color':  'grey',
	        'style': 'oblique',
	        'weight': 'black',
	        'size': 14,
	        }
	small_font = {'family': 'monospace',
	        'color':  'black',
	        'style': 'oblique',
	        'weight': 'black',
	        'size': 8,
	        }

	combo_df = grab_df.sort_values(by = select_field, ascending = False, ignore_index = True)
	results = pd.concat([grab_df['Name'], grab_df[select_field]], axis = 1)

	if select_field == 'GP':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_1 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "GAMES PLAYED",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_1(rect_1):
			for rect in rect_1:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_1(rect_1[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'AB':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_2 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "AT BATS",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_2(rect_2):
			for rect in rect_2:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_2(rect_2[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'RC':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_3 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "RUNS CREATED",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_3(rect_3):
			for rect in rect_3:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_3(rect_3[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'RC/27':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_4 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "RUNS CREATED PER 27 OUTS",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_4(rect_4):
			for rect in rect_4:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_4(rect_4[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'BB/PA':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_5 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "WALK PER PLATE APPEARANCE",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_5(rect_5):
			for rect in rect_5:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_5(rect_5[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'BB/K':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_6 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "WALK PER STRIKEOUT",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_6(rect_6):
			for rect in rect_6:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_6(rect_6[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'ISOP':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_7 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "ISOLATED POWER",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_7(rect_7):
			for rect in rect_7:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_7(rect_7[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'SECA':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_8 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "SECONDARY AVERAGE",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_8(rect_8):
			for rect in rect_8:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_8(rect_8[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'P/PA':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_20 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "PITCHES PER PLATE APPEARANCE",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_20(rect_20):
			for rect in rect_20:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_20(rect_20[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	
	elif select_field == 'XBH':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_9 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "EXTRA BASE HITS",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_9(rect_9):
			for rect in rect_9:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_9(rect_9[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'PA':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_10 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "PLATE APPEARANCES",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_10(rect_10):
			for rect in rect_10:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_10(rect_10[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'AB/HR':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_11 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "AT BATS PER HR",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_11(rect_11):
			for rect in rect_11:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_11(rect_11[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'AVG':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_12 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "AVERAGE",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_12(rect_12):
			for rect in rect_12:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_12(rect_12[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'OBP':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_13 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "ON BASE PERCENTAGE",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_13(rect_13):
			for rect in rect_13:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_13(rect_13[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'SLG':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_14 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "SLUGGING",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_14(rect_14):
			for rect in rect_14:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_14(rect_14[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)
	elif select_field == 'OPS':
		fig, ax = plt.subplots(figsize = (9,6), dpi = 300) 
		rect_15 = ax.bar(results['Name'], height =  results[select_field],
		        width=0.3, edgecolor='red', alpha = .7,
		        label = "ON BASE PLUS SLUGGING",
		        hatch = choice_patterns)
		ax.set_title("WASHINGTON NATIONALS 2021 SEASON\nADVANCED STATS",
        fontdict = text_font)
		ax.tick_params(axis = "both", pad = 1, labelrotation = 0,
		        labelcolor = "grey",  direction='out',
		        which = "major", labelsize = "large", colors = "r")
		ax.set_xticks(results['Name']) 
		ax.set_xticklabels(results['Name'], rotation = 'vertical',
		        fontdict = small_font)
		def autolabel_15(rect_15):
			for rect in rect_15:
				aheight = rect.get_height()
				height = round(aheight, 3)
				ax.annotate('{}'.format(height),
				xy=(rect.get_x() + rect.get_width() - .7, height),
				xytext=(rect.get_x(), rect.get_width() / 2),
				textcoords="offset points", ha='center', va='bottom')
		autolabel_15(rect_15[::4])
		ax.grid()
		ax.legend(loc = "lower left")
		st.pyplot(fig)

		
		
	st.dataframe(combo_df)


if __name__ == "__main__":
	run_stream()
	
