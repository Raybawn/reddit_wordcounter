# Wallstreetbets Wordcount
A small project to get familiar with Python, SQL and visualization.

The project uses PRAW to collect data. These are then filtered and cleaned, NLP is used for this. 
With it I remove stopwords like "the", "a", "and", etc. I also strip out any emojis from the texts.

I convert the filtered list of words into a DataFrame to facilitate visualization with Seaborn. 
I add the sum of the individual words to the DataFrame and sort them by number.

Finally, I create a barplot with Seaborn, this plot uses the newest 1000 posts from 30.05.22:

![Figure_1](https://user-images.githubusercontent.com/32166093/171032473-64d1ca94-3948-43bf-be7c-a9c3225970fc.png)

The learned skills here will be great for future projects in the realm of data analysis. It was a fun little exercise!
