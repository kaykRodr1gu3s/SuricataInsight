import os
from matplotlib import pyplot as plt


class plotting:

    def plotting_datas(self, datas_for_plot : list, csv_name: list):
        '''
        This function will plot all datas that are available, and save with the name csv_name.png
        '''
        os.chdir('..//Visualization')


        for number, data in enumerate(datas_for_plot):
            plt.barh(data[0],data[1])
            plt.title('Graphic of alert')
            plt.xlabel('Alert Names')
            plt.ylabel('Quantity')

            if data[1][0] > 300:
                plt.subplots_adjust(left=0.5)
                plt.xticks(rotation=45, ha='right')
                plt.grid(True)

            else:
                plt.subplots_adjust(left=0.6)

            plt.savefig(csv_name[number].split('.')[0])
            plt.show()



