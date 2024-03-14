import pandas as pd
from collections import Counter
from tools import plot
from tools import directory_helper



class data_analysis:
    def __init__(self):
        self.cvs_file = directory_helper.directory().dir_content

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
                                df_columns_name[3]: 'Source Port', df_columns_name[3]: 'IP Destination',df_columns_name[4]: 'Destination Port', 
                                df_columns_name[5] :'Event Type', df_columns_name[6] : 'Severity', df_columns_name[7]: 'Alert Signature'
                                }, inplace=True)
            df.loc[-1] = df_columns_name
            df.index = df.index + 1
            df = df.sort_index()

            df['Time'] = df['Time'].apply(lambda time: time.split('.')[0])
            df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%dT%H:%M:%S')

            for csv_name in self.cvs_file:
                directory_helper.directory.new_csv_folder()
                df.to_csv(csv_name + ".csv")
            
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

    def main(self):
        '''
        This function, will agroup all the function and initing all of them
        '''  
        csv = self.open_csv()
        trans_data = self.transform_data(csv)
        counted_data = self.counter_function(trans_data)
        plotting = plot.plotting()

        plotting.plotting_datas(counted_data, self.cvs_file)

datas = data_analysis()
datas.main()