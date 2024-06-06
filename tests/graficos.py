'''GERADO PELO CHATGPT'''

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import glob

csv_files = glob.glob('results_*.csv')

dfs = []

for file in csv_files:
    if 'reversed' not in file and 'summary' not in file:
        try:
            print(f"Reading file {file}")
            df = pd.read_csv(file)
            if df.empty:
                print(f"File {file} is empty. Skipping.")
                continue
            file_info = file.split('_')
            algorithm = file_info[1] + '_' + file_info[2]
            size = int(file_info[3])
            list_type = file_info[4].split('.')[0]
            if list_type in ['random', 'sorted']:
                df['Algorithm'] = algorithm
                df['Size'] = size
                df['List Type'] = list_type
                dfs.append(df)
        except pd.errors.EmptyDataError:
            print(f"File {file} is empty or invalid. Skipping.")
        except Exception as e:
            print(f"An error occurred while reading file {file}: {e}")

# Concatenar todos os DataFrames em um único DataFrame
if dfs:
    df_all = pd.concat(dfs, ignore_index=True)

    # Calcular as médias para comparações, trocas e tempo por algoritmo, tamanho e tipo de lista
    df_summary = df_all.groupby(['Algorithm', 'Size', 'List Type']).agg(
        Avg_Comparisons=('Comparisons', 'mean'),
        Avg_Swaps=('Swaps', 'mean'),
        Avg_Time=('Time', 'mean')
    ).reset_index()

    # Listas únicas de tamanhos e tipos
    sizes = df_summary['Size'].unique()
    list_types = ['random', 'sorted']

    # Definir cores consistentes para cada algoritmo
    algorithm_colors = {
        'bubble_sort': 'red',
        'selection_sort': 'blue',
        'insertion_sort': 'green',
        'merge_sort': 'orange',
        'quick_sort': 'purple',
        'heap_sort': 'brown'
    }

    def save_figure(fig, filename):
        fig.write_html(filename)

    fig = make_subplots(
        rows=len(sizes), cols=len(list_types),
        subplot_titles=[f"{lt} - {size}" for size in sizes for lt in list_types],
        horizontal_spacing=0.1
    )

    for i, size in enumerate(sizes):
        for j, list_type in enumerate(list_types):
            df_filtered = df_summary[(df_summary['Size'] == size) & (df_summary['List Type'] == list_type)]
            for algorithm in df_filtered['Algorithm'].unique():
                df_algo = df_filtered[df_filtered['Algorithm'] == algorithm]
                fig.add_trace(
                    go.Scatter(x=[size], y=df_algo['Avg_Comparisons'], mode='lines+markers', name=algorithm,
                               line=dict(color=algorithm_colors[algorithm]), marker=dict(size=10), legendgroup=algorithm, showlegend=(i == 0 and j == 0)),
                    row=i+1, col=j+1
                )

    fig.update_layout(title_text='Average Comparisons by Algorithm, Size, and List Type', height=1000, width=1200,
                      template='plotly_dark')
    fig.update_xaxes(title_text='List Size')
    fig.update_yaxes(title_text='Avg Comparisons')
    save_figure(fig, 'avg_comparisons.html')

    fig = make_subplots(
        rows=len(sizes), cols=len(list_types),
        subplot_titles=[f"{lt} - {size}" for size in sizes for lt in list_types],
        horizontal_spacing=0.1
    )

    for i, size in enumerate(sizes):
        for j, list_type in enumerate(list_types):
            df_filtered = df_summary[(df_summary['Size'] == size) & (df_summary['List Type'] == list_type)]
            for algorithm in df_filtered['Algorithm'].unique():
                df_algo = df_filtered[df_filtered['Algorithm'] == algorithm]
                fig.add_trace(
                    go.Scatter(x=[size], y=df_algo['Avg_Swaps'], mode='lines+markers', name=algorithm,
                               line=dict(color=algorithm_colors[algorithm]), marker=dict(size=10), legendgroup=algorithm, showlegend=(i == 0 and j == 0)),
                    row=i+1, col=j+1
                )

    fig.update_layout(title_text='Average Swaps by Algorithm, Size, and List Type', height=1000, width=1200,
                      template='plotly_dark')
    fig.update_xaxes(title_text='List Size')
    fig.update_yaxes(title_text='Avg Swaps')
    save_figure(fig, 'avg_swaps.html')

    fig = make_subplots(
        rows=len(sizes), cols=len(list_types),
        subplot_titles=[f"{lt} - {size}" for size in sizes for lt in list_types],
        horizontal_spacing=0.1
    )

    for i, size in enumerate(sizes):
        for j, list_type in enumerate(list_types):
            df_filtered = df_summary[(df_summary['Size'] == size) & (df_summary['List Type'] == list_type)]
            for algorithm in df_filtered['Algorithm'].unique():
                df_algo = df_filtered[df_filtered['Algorithm'] == algorithm]
                fig.add_trace(
                    go.Scatter(x=[size], y=df_algo['Avg_Time'], mode='lines+markers', name=algorithm,
                               line=dict(color=algorithm_colors[algorithm]), marker=dict(size=10), legendgroup=algorithm, showlegend=(i == 0 and j == 0)),
                    row=i+1, col=j+1
                )

    fig.update_layout(title_text='Average Time by Algorithm, Size, and List Type', height=1000, width=1200,
                      template='plotly_dark')
    fig.update_xaxes(title_text='List Size')
    fig.update_yaxes(title_text='Avg Time (s)')
    save_figure(fig, 'avg_time.html')
else:
    print("No valid data found in the CSV files.")
