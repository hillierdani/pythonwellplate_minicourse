import wellmap
import matplotlib.pyplot as plt
import pandas as pd

wellmap.show('./data/20221007_CR_AB9_short.toml', attrs=None, color='rainbow')
#to visualize the plate, the matplotlib is needed
plt.show()

def load_lum(path):
    return (pd
            .read_csv(path, sep=";")
            .rename(columns={'Lum': 'row'})
            .melt(
                    id_vars=['row'],
                    var_name='col',
                    value_name='Lum',
            )
    )
data = load_lum('./data/20221007_CR_AB9.csv')
data

labels = wellmap.load('./data/20221007_CR_AB9_short.toml')

df = pd.merge(labels, data)
print(df)





# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
