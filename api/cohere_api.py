import cohere
import os
from dotenv import load_dotenv
from web_scraping import get_pd_df
from pca import get_pc
from twod_plot import generate_chart
import pandas as pd
import numpy as np
from cosine_similarity import get_similarity
from sklearn.cluster import KMeans
from word_cloud import word_cloud
load_dotenv()  # take environment variables from .env.

api_key = os.getenv('COHERE_API_KEY')
co = cohere.Client(api_key)


def cluster():
    link = "https://www.jair.org/index.php/jair/issue/archive"
    df = get_pd_df(link)
    df['title_embeds'] = co.embed(
        model='large',
        texts=df['title'].tolist()).embeddings
    embeds = np.array(df['title_embeds'].tolist())
    print(embeds)
    embeds_pca = get_pc(embeds, 2)
    df_pca = pd.concat([df, pd.DataFrame(embeds_pca)], axis=1)
    df_pca.columns = df_pca.columns.astype(str)
    print_similar(df_pca, embeds)

    df_clust = df_pca.copy()
    n_clusters = 5
    kmeans_model = KMeans(n_clusters=n_clusters, random_state=0)
    classes = kmeans_model.fit_predict(embeds).tolist()
    df_clust['cluster'] = (list(map(str, classes)))
    # word_cloud(df_clust, n_clusters)
    print(df_clust)


def print_similar(df_pca, embeds):
    sample = 200
    search_query = "Quantum computing"
    search_query_embeds = co.embed(
        model='large', texts=[search_query]).embeddings[0]
    similarity = get_similarity(search_query_embeds, embeds[:sample])
    print('Query:')
    print(search_query, '\n')
    print('Similar AI papers:')
    for idx, sim in similarity:
        if sim >= 0.30:
            df_pca.at[idx, 'similar'] = 'yes'
        else:
            df_pca.at[idx, 'similar'] = 'no'
        print(f'Similarity: {sim:.2f};', df_pca.iloc[idx]['title'])
