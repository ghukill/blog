---
published: false
---
We're getting into advanced search.  With topic modeling and other alt-metadata searching around the corner, we want to make sure we've got real estate established in the new front-end for the digital collections we've been working on, for unique / beta / interesting / experiemental search options and interfaces.  

So, decided to start wiring up an "advanced search" page to augment our poweful, but relatively simple search page.  Like anything interesting, this candy bar has split higher up than expected, and I'm left chewing much more nougat than anticipated.  Great adventure

A first step -- er, middling step -- was to investigate what "advanced search" looks like in other online, search interfaces.  Both surprising, and unsurprising for reasons hopefully touched on later, the world of "advanced search" has shrunk in the age of facets and intelligent, powerful, omnipotent back-end search engines such as Solr.  The days of crafting the perfect boolean search are dwindling as other search strategies become more popular.  This is not to discount a single, surgical search.  Not at all.  For literature reviews, or general prudent thoroughness, a well-crafted, complex search is still incredibly powerful.  And is actually still possible through many single-searchbox interfaces.

Take Google for example.  With keywords, you can define quite particular searches.

Search only websites on `digital.library.wayne.edu`:

    site:digital.library.wayne.edu winter czar

Or even limiting words:

    seattle -space needle
    
But many users don't know these little tricks.  Since the dawn of online search interfaces, there have often been accompanying "advanced search" interfaces that provide a handful of boxes and inputs that users can use to refine their search.  Our own [library catalog](http://elibrary.wayne.edu/search/X) is a nice example:

![Screen Shot 2017-01-17 at 2.09.05 PM.png]({{site.baseurl}}/assets/images/Screen Shot 2017-01-17 at 2.09.05 PM.png)

But as I started to dig into what other advanced search interfaces looked like for digital collections or archives, I started to notice a trend.  Something I'm referring to as the **mighty three** in my internal running monologue.  They are variations on the following four "advanced" search options:

* all / any these words
* this exact word or phrase
* none of these words



    

