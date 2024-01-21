import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
from tools import directory_helper
import os

a = directory_helper.directory(os.listdir())
print(a.dir_content)


class data_visualization:

    def open_csv(self) -> pd.DataFrame:
        '''
        This function, will open the Suricata_datas.csv and transform in a pd.core.frame.DataFrame object
        '''

        return pd.read_csv('Suricata_Datas.csv')


    def transform_data(self, pd_data) -> pd.DataFrame:
        '''
        The transform_data function will rename the column, and will parse the Time column for a datetime format.
        '''

        df = pd_data
        df_columns_name = df.columns.to_list()

        df.rename(columns={
            df_columns_name[0]: 'Time', df_columns_name[1]: 'IP Source', df_columns_name[2]: 'Port Source',
                            df_columns_name[3]: 'Sorce Port', df_columns_name[3]: 'IP Destination',df_columns_name[4]: 'Destination Port', 
                            df_columns_name[5] :'Event Type', df_columns_name[6] : 'Severity', df_columns_name[7]: 'Alert Signature'
                            }, inplace=True)

        df.loc[-1] = df_columns_name
        df.index = df.index + 1
        df = df.sort_index()

        df['Time'] = df['Time'].apply(lambda time: time.split('.')[0])
        df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%dT%H:%M:%S')

        return df


    def counter_function(self, data: pd.DataFrame) -> list:
        '''
        This function will counter all the Alert Signature and will save in a list
        '''
        counter_Alert_Signature = Counter()

        counter_Alert_Signature
        counter_Alert_Signature.update(data['Alert Signature'])
        counter_Alert_Signature = counter_Alert_Signature.most_common()

        all_data = []
        Alert_Signature_name = []
        Alert_Signature_quantity = []

        for value in counter_Alert_Signature:
            Alert_Signature_name.append(value[0])
            Alert_Signature_quantity.append(value[1])

        all_data.append(Alert_Signature_name)
        all_data.append(Alert_Signature_quantity)
        
        return all_data 


    def plotting_datas(self, datas_for_plot : list):
        '''
        This function will plot all datas that are available, and save with the name Suricata_Datas.png
        '''

        plt.barh(datas_for_plot[0],datas_for_plot[1])
        plt.title('Graphic of alert')
        plt.xlabel('Alert Names')
        plt.ylabel('Quantity')
        plt.xticks(rotation=45, ha='right')
        plt.subplots_adjust(left=0.4)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('Graphic.png', bbox_inches='tight')
        plt.show()
        
    def main(self):
        csv = self.open_csv()
        trans_data = self.transform_data(csv)
        counted_data = self.counter_function(trans_data)
        self.plotting_datas(counted_data)



a = data_visualization()
a.main()