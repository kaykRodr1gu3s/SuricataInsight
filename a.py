import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

    

df = pd.read_csv('Suricata_datas.csv')
df_columns_name = df.columns.to_list()


plt.style.use('fivethirtyeight')
df.rename(columns={df_columns_name[0]: 'Time', df_columns_name[1]: 'IP Source', df_columns_name[2]: 'Port Source', df_columns_name[3]: 'Sorce Port', df_columns_name[3]: 'IP Destination',
                    df_columns_name[4]: 'Destination Port', df_columns_name[5] :'Event Type', df_columns_name[6] : 'Severity', df_columns_name[7]: 'Alert Signature'}, inplace=True)




df.loc[-1] = df_columns_name
df.index = df.index + 1
df = df.sort_index()



df['Time'] = df['Time'].apply(lambda time: time.split('.')[0])



df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%dT%H:%M:%S')


counter_Alert_Signature = Counter()

counter_Alert_Signature
counter_Alert_Signature.update(df['Alert Signature'])

counter_Alert_Signature = counter_Alert_Signature.most_common()

Alert_Signature_name = []
Alert_Signature_quantity = []
for value in counter_Alert_Signature:
    Alert_Signature_name.append(value[0])
    Alert_Signature_quantity.append(value[1])


plt.barh(Alert_Signature_name,Alert_Signature_quantity)
plt.xticks(rotation=45, ha='right')
plt.subplots_adjust(left=0.4)
# plt.grid(True)
plt.tight_layout()




plt.show()