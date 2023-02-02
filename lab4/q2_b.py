import pandas as pd

from IPython.display import Javascript
display(Javascript('google.colab.output.setIframeHeight(0, true, {maxHeight: 5000})'))

pd.set_option('display.expand_frame_repr', False)         # to prevent breaking of columns

df = pd.read_csv("Avocado_Dataset.csv", parse_dates =["Date"], index_col ="Date")
monthly_resampled_data = df.resample('M').mean()
print(monthly_resampled_data)
print('\n\n\n\n\n\n')


yearly_resampled_data = df.resample('12M').mean()
print(yearly_resampled_data)