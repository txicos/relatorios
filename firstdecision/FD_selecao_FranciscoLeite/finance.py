import pandas
import datetime
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('agg')


vix_df = pandas.read_csv("vix-daily.csv")

print(vix_df.head(6))

print(vix_df.info())

vix_df_stats = vix_df.describe()

print(vix_df_stats)


vix_df['DATE'] = pandas.to_datetime(vix_df['DATE'])

vix_df['Volatility Range'] = vix_df['HIGH'] - vix_df['LOW']

vix_df.set_index('DATE', inplace=True)

vix_df_avrg = vix_df.groupby([(vix_df.index.year), (vix_df.index.month)]).mean()

vix_df_avrg = vix_df.groupby(pandas.Grouper(freq="M")).mean()

vix_df_avrg_close = vix_df_avrg['CLOSE']

plt.figure()
vix_df_avrg_close.plot(y='CLOSE', use_index=True)


plt.savefig("close.png", dpi=300, transparent=True)

now = datetime.datetime.now()
formatted_date = now.strftime('%y%m%d_%H%M')

file_name = "finance"+formatted_date+".parquet"

vix_df_avrg.to_parquet(file_name)
