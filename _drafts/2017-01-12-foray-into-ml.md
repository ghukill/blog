---
published: false
---
In everything gloriously complex, it can be difficult to ascertain when you've reached a level of understanding that might merit debrief and reflection.  In my forays into machine learning, this is probably as good a point as any.

I've been interested in Machine Learning for quite some time now.  Since I first started stumbling on ImageNet and how it helped image processors classify images, to actual tinkering with an Alpha release of Google Vision, through the heady days of self-driving cars, and backing up even further, initial go's at deriving meaning and topics from text with Python libraries like [NLTK](http://www.nltk.org/).

"Quite some time," being relative.  It's a rapidly developing area of computer science, philosophy, mathematics, humanities, and their intersections.

Recently I've embarked on a project to try and derive topics from a corpus of academic articles in PDF form (around 700 of them), then by re-submitting one to the model, asking what other articles are "similar".  After quite a bit of trial and error, researching these emerging areas, and honing in on workflows that I might actually whiddle into working, I'm thrilled to have some results coming back that are -- genuinly -- spine-tingling.  

The guts of this project falls on the python library, [gensim](https://radimrehurek.com/gensim/).  A masterful library meant to humanize the multi-dimensional math that underpins machine learning (and I use that term loosely here).  

The rough sketch is thus:

1. Point this little tool (called `atm`, for "article topic modeling", and the way it _dispenses_ fun things to think about) at a dropbox folder with API credentials
2. Downloads the entire directory, in this case, ~700 articles
3. Create a bag of words for each document
4. Strip of [stopwords](https://en.wikipedia.org/wiki/Stop_words) and punctuation (poorly at this point, I might add)
5. Then the fun part: create a Latent Dirichlet Allocation (LDA) model with gensim
6. Index ~100 topics that are suggested by this model, for this given corpus
7. Finally, query the model with a document (in this case, an article from the corpus) for similarity to other documents in the corpus

The results are other documents in the corpus, and a percentile on topical vectors that match the article.  I should stop myself here: the details are still forming, and while I'm getting a good grasp on relatively low-level how this works, that's fodder for another post.  At this point, the rough sketches.

Below are the results of a query, run through a [Jupyter](https://jupyter.org/) notebook of atm:

![Screen Shot 2017-01-12 at 3.41.16 PM.png]({{site.baseurl}}/assets/images/Screen Shot 2017-01-12 at 3.41.16 PM.png)


