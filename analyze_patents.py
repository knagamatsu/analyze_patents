import pandas as pd
import matplotlib.pyplot as plt


def main():    
    # file_name = '機械学習_製造_合成_特許.CSV'
    file_name = '機械学習_特許.CSV'
    
    df = pd.read_csv(file_name, encoding='shift-jis', parse_dates=True, index_col='出願日')
    df['count'] = 1
    df_group = df.resample('Y').sum()
    save_file_name = './results/' + file_name.replace('CSV', '')    
        
    plot_line(df_group, save_file_name)
    analyze_applocant(df, save_file_name)


def plot_line(df, save_file_name):
    plt.rcParams['font.size']=14
    plt.rcParams['font.family']='MS Gothic'
    fig, ax = plt.subplots(dpi=300)
    ax.plot(df.index, df['count'])
    ax.set_title('出願件数')
    ax.set_xlabel('出願日')
    ax.set_ylabel('件数(件)')
    plt.tight_layout()
    fig.savefig(f'{save_file_name}_line_plot.png')
    plt.show()


def analyze_applocant(df, save_file_name):
    bar_length = 20
    df_group = df.groupby('出願人').sum().sort_values('count')
    df_group.index = df_group.index.str[:10]
    df_group = df_group[-bar_length:]
    
    plt.rcParams['font.size']=14
    plt.rcParams['font.family']='MS Gothic'
    
    fig, ax = plt.subplots(figsize=(6,6), dpi=300)
    ax.barh(df_group.index, df_group['count'])
    ax.set_title('出願件数')
    ax.set_xlabel('出願件数(件)')
    plt.tight_layout()
    fig.savefig(f'{save_file_name}_企業ランキング.png')
    plt.show()
    
    
if __name__ == '__main__':
    main()

