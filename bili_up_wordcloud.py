import sys
import wordcloud
import pandas as pd
UID = sys.argv[1]
tags = pd.read_csv(f'UID-{UID}.csv', header=None)
tags.columns=['tag']
wtags = tags.groupby('tag').size()
wc= wordcloud.WordCloud(font_path="NotoSerifCJK-Bold.ttc",
                        background_color="white",
                        width =1920,height= 1080,margin= 10 ).generate_from_frequencies(wtags)
wc.to_file(f'UID-{UID}-词云.png')