The goal of this project is to learn how to make a simple article recommendation engine using word2vec. In particular, we're going to use a "database" from Stanford's GloVe project trained on a dump of Wikipedia. The project involves reading in a database of word vectors and a corpus of text articles then organizing them into a handy table (list of lists) for processing.

Around the recommendation engine, we are going to build a web server that displays a list of BBC articles for URL http://localhost:5000 (testing) or whatever the IP address is of your Amazon server (deployment):

Clicking on one of those articles takes you to an article page that shows the text of the article as well as a list of five recommended articles:


![alt text](https://github.com/AditiSharmaUSFCA/Recommending-Articles/blob/master/article.png)
