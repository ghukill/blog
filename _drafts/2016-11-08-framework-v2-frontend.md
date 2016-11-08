---
published: false
---
## Choosing a framework for our v2 Digital Collections front-end

We are currently in the midsts of refreshing our [Digital Collections front-end](https://digital.library.wayne.edu/digitalcollections/).  It has been a workhorse for us, still functions, and still looks respectable, but the foundation is beginning to crack as we push the original design and corners of spaghetti code beyond their original visions.

The front-end was visually imagined back in 2012-2013.  At the time, our "back-end" consisted of nothing more than raw Solr endpoints and some hacked together scripts that returned more complex queries from Fedora Commons, specifically for RDF queries.  Javascript grew in the front-end like weeds, with functions and files springing up whenever new functionality was introduced:

* user login and authentication


We are starting to hone in on using a PHP framework.  Considering Slim and Lumen at this point.  Why a PHP framework?  Why not Flask to augment the other python components in the stack?


It's a combination of reasons.


First, PHP is a language more commonly used here in the libraries.  More people know it now, and though you could debate this a bit, it's probable that anyone coming in later will at least be familiar with PHP.  Perhaps you could say the same about Python, but as long as the website is PHP based, we'll have people "in shop" who know PHP.  Perhaps the same can't be said for Python


Second, we would like to keep front-end and back-end cleanly separated if possible.  An initial thought

