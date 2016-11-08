---
published: false
---
## Choosing a framework for our v2 Digital Collections front-end

We are currently in the midsts of refreshing our [Digital Collections front-end](https://digital.library.wayne.edu/digitalcollections/).  It has been a workhorse for us, still functions, and still looks respectable, but the foundation is beginning to crack as we push the original design and corners of spaghetti code beyond their original visions.

The front-end was visually imagined back in 2012-2013.  At the time, our "back-end" consisted of nothing more than raw Solr endpoints and some hacked together scripts that returned more complex queries from Fedora Commons, specifically for RDF queries.  Javascript grew in the front-end like weeds, with functions and files springing up whenever new functionality was introduced:

* user login and authentication
* iteratively improved search
* full-text vs. structured metadata refinement
* improvement of facets
* collection browsing
* serials browsing and interfaces
* inter-linked learning objects
* introduction of hierarchical content types such as archival materials and serials
* and the list goes on...

I'm proud of what we've built, something that is remarkably usable and cohesive given the breakneck pace of change and learning that ran parallel.  It has survived entire re-imaginings of how digital objects are structured, a full-fledged API on the back-end that powers it, migration of servers, introduction of vagrant provisioning, you name it.  

But its time has come.  As we push into more digital objects, we've started to notice some performance hits that are a result of inefficient JS tangles and approaches.  Our initial approach was a "lightweight" JS front-end that relied heavily on AJAX calls to retrieve information from our back-end API, that was drawn on the page with jQuery-Mustache templating.  We've made a handful of improvements that keep it humming along, but any substantial changes would require reworking a *lot* of ugly JS code.  And I can say that, because we wrote it all.

The visual style is also feeling a bit dated, or perhaps if but only stale.  It needs a refresh there too.  

And there was the *very* important issue of sustainability.  We knew the ins and outs of the JS code, but it wasn't easy, and near impossible to document in a lucid fashion.

So, the time was right.  We have at our disposal someone who is going to put together front-end wireframes that we can use to wire up and implement.  The next big decision: **what kind of organization and/or framework for the front-end?**

We spent a bit of time going round and round, discussing the pros and cons of emerging JS, Python, and other frameworks.  It is worth noting, all being simulataneously congnizant that we may migrate to a more turn-key solution down the road, if projects like Hydra-in-a-Box provide a truly whole-kit-and-kaboodle option.  Another goal, briefly alluded to, is sustainability in a front-end; something that can be worked on, improved, fixed, and loved for some time.

I can't believe I'm typing this, but **we are starting to hone in on using a PHP framework**.  Considering [Slim](http://www.slimframework.com/) and [Lumen](https://lumen.laravel.com/) at this point.  Why a PHP framework?  Why not Flask to augment the other python components in the stack?

For a combination of reasons.

First, **PHP is a language commonly used here in the libraries**.  More people know it now, and though you could debate this a bit, it's probable that anyone coming in later will at least be familiar with PHP.  Perhaps you could say the same about Python, but **as long as the website is PHP based, we'll have people "in shop" who know PHP**.  Perhaps the same can't be said for Python.  And that's important.

Second, **we would like to keep front-end and back-end cleanly separated**.  At our initial wireframing meeting, the individual creating a working wireframe leveraging our quirky and undocumented API.  That was amazing!  And it reinforced the idea that **treating our collections as data**, maybe even first and foremost.  Front-ends will come and go, amaze and disgust, but our underlying, highly-organized digital objects will remain.  An organized API for access to those materials means a multitude of front-end interfaces are possible, migration down the road is easier, and it opens up access to all kinds of different.














