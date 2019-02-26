'''
 * Created by filip on 20/02/2019
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def __init__():
    print("Hello ML, wassup")

    #for i in range( 1 , 10 ) :
    #    print("My cool i is: " + str(i))

    data = pd.read_csv("D:\Downloads\MeetingReport.csv")

    print(data.head())

    #print(data.columns)

    # print(data)

    # languages = data['Language']

    # print(languages)

    lang_vals = data['Language'].value_counts()
    lang_vals_length = len(lang_vals)

    print(lang_vals)
    print(lang_vals[1])

    #data["lang_cat"] = np.where(data['Language'] == lang_vals[lang_vals_length - 1] or lang_vals[lang_vals_length - 2 ]
     #                           or lang_vals[lang_vals_length - 3], "other", data['Language'])
    # for lan in lang_vals[:3]:


      #  .plot.pie()
  #  plt.show()

__init__()
