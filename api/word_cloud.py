from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)


def word_cloud(df_clust, n_clusters):
    for n in range(n_clusters):
        df_wordcloud = df_clust.loc[df_clust['cluster'] == str(n)]
        text = " ".join(i for i in df_wordcloud.title)
        wordcloud = WordCloud(width=800, height=800,
                              background_color='white',
                              stopwords=stopwords,
                              min_font_size=10).generate(text)
        plt.figure(figsize=(8, 8), facecolor=None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)

        plt.show()

    # manually create the labels for the clusters  after looking at top words in each cluster
    df_clust['cluster'] = df_clust['cluster'].replace(["0", '1', '2', '3', '4'], [
                                                      'Quantum Computing', 'Election Manipulation', 'Bio informatics', 'Language Models', 'Explainable AI'])
