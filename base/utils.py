from io import BytesIO
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_chart(year_from, year_to, chart_type, show_results_of, compare_results_to, **kwargs):
    headers = ['STATISTIC', 'Statistic', 'YEAR', 'TLIST(Q1)', 'Quarter', 'C02343V02817', 'Area', 'UNIT', 'VALUE']
    df = pd.read_csv('HSQ06.20220517231225.csv', names=headers)
    df['STATISTIC'] = df['STATISTIC'].astype(str)
    df['Statistic'] = df['Statistic'].astype(str)
    df['YEAR'] = pd.to_numeric(df['YEAR'], errors='coerce')
    df['TLIST(Q1)'] = df['TLIST(Q1)'].astype(str)
    df['Quarter'] = df['Quarter'].astype(str)
    df['C02343V02817'] = df['C02343V02817'].astype(str)
    df['Area'] = df['Area'].astype(str)
    df['UNIT'] = df['UNIT'].astype(str)
    df['VALUE'] = pd.to_numeric(df['VALUE'], errors='coerce')

    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 4))
    year_from = float(year_from)
    year_to = float(year_to)
    key = 'YEAR'

    if chart_type == '#0':
        d = df.groupby(key, as_index=False)['VALUE'].mean()
        plt.bar(d[key], d['VALUE'])

        plt.title('House Prices from year 1975 to 2016')
        plt.xlabel('YEAR')
        plt.ylabel('Values in Euro')

    elif chart_type == '#1':

        df12 = df.query('YEAR >=@year_from and YEAR <=@year_to  and Area == @show_results_of').groupby(key, as_index=False)['VALUE'].mean()
        df13 = df.query('YEAR >=@year_from and YEAR <=@year_to  and Area == @compare_results_to').groupby(key, as_index=False)['VALUE'].mean()

        df16 = pd.merge(df12, df13, on='YEAR')
        colors2 = ['#448ee4', '#a9f971']

        df16.plot.bar(x='YEAR', color=colors2)

        plt.gca().legend((show_results_of, compare_results_to))
        plt.xticks(rotation=90)

        plt.title('House Prices from year '+str(year_from)+' to '+str(year_to)+'')
        plt.xlabel('YEAR')
        plt.ylabel('Values in Euro')

    elif chart_type == '#2':

        df12 = df.query('YEAR >=@year_from and YEAR <=@year_to  and Area == @show_results_of').groupby(key, as_index=False)['VALUE'].mean()
        df13 = df.query('YEAR >=@year_from and YEAR <=@year_to  and Area == @compare_results_to').groupby(key, as_index=False)['VALUE'].mean()

        df16 = pd.merge(df12, df13, on='YEAR')
        colors2 = ['#448ee4', '#a9f971']

        df16.plot(x='YEAR', color=colors2)

        plt.gca().legend((show_results_of, compare_results_to))
        plt.xticks(rotation=90)

        plt.title('House Prices from year '+str(year_from)+' to '+str(year_to)+'')
        plt.xlabel('YEAR')
        plt.ylabel('Values in Euro')

    else:
        print('ups... failed to identify the chart type')
    plt.tight_layout()
    chart = get_graph()
    return chart
