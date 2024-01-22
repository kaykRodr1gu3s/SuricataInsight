import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
from tools import directory_helper
import os



class data_analysis:
    def __init__(self):
        self.cvs_file = directory_helper.directory(os.listdir()).dir_content

    def open_csv(self) -> pd.DataFrame:
        '''
        This function, will open the Suricata_datas.csv and transform in a pd.core.frame.DataFrame object
        '''
        list_df = []
        
        for csv in self.cvs_file:
            df = pd.read_csv(csv)
            list_df.append(df)
        return list_df

    def transform_data(self, pd_data: list) -> pd.DataFrame:
        '''
        The transform_data function will rename the column, and will parse the Time column for a datetime format.
        '''
        df_data = []
        for csv in pd_data:
            df = csv
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
            df_data.append(df)

        return df_data


    def counter_function(self, data: pd.DataFrame) -> list:
        '''
        This function will counter all the Alert Signature and will save in a list
        '''

        all_data = []
        for content in data:
            counter_Alert_Signature = Counter()
            ids = content['Alert Signature']
            counter_Alert_Signature.update(ids)
            counter_Alert_Signature = counter_Alert_Signature.most_common()

            Alert_Signature_name = []
            Alert_Signature_quantity = []

            for value in counter_Alert_Signature:
                content_data = []
                Alert_Signature_name.append(value[0])
                Alert_Signature_quantity.append(int(value[1]))

                content_data.append(Alert_Signature_name)
                content_data.append(Alert_Signature_quantity)
            all_data.append(content_data)
 
        return all_data 


    def plotting_datas(self, datas_for_plot : list):
        '''
        This function will plot all datas that are available, and save with the name Suricata_Datas.png
        '''
        os.chdir('..\\Visualization')
        csv_name = self.cvs_file
        for number, data in enumerate(datas_for_plot):
            plt.barh(data[0],data[1])
            plt.title('Graphic of alert')
            plt.xlabel('Alert Names')
            plt.ylabel('Quantity')
            plt.xticks(rotation=45, ha='right')
            if data[1][0] > 400:

                plt.subplots_adjust(left=0.4)
            else:
                plt.subplots_adjust(left=0.1)
            plt.grid(True)
            plt.tight_layout()
            plt.savefig(csv_name[number].split('.')[0], bbox_inches='tight')
            plt.show()
            

    def main(self):
        '''
        This function, will agroup all the function and initing all of them
        '''

        csv = self.open_csv()
        trans_data = self.transform_data(csv)
        counted_data = self.counter_function(trans_data)
        self.plotting_datas(counted_data)



datas = data_analysis()

datas.main()
