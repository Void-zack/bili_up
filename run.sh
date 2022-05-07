biliUID="688219229"
scrapy crawl bili_up -a UID=${biliUID}
python3 ./bili_up_wordcloud.py ${biliUID}
