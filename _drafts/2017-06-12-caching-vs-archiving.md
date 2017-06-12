---
published: false
---
A strange thought today while working with a colleague on tuning caching for our digital collections with [Varnish](https://varnish-cache.org/).

We have been working to cache thumbnails and single item pages, and in the process, and I just about physically tripped on the interesting difference between caching website resources, and archiving a rendered version of the website.

To cache a single item page, we have been experimenting with using python to make headless, HTTP requests to our front-end PHP framework, [Slim](https://www.slimframework.com/).  I had delighted that a single request would put into motion the reconciling work that Slim does for a single item page, including a couple of API calls to our backend, and then save that rendering as a static HTML response for future visits.  Awesome.  

But on testing today, we noticed that a "preview" image was not cached, and would load the first time.  Actually, a handful of things were not cached.  Anything that the browser requested, after our front-end framework had delivered its payload, had not been cached in that early item page caching.  Thinking it through, this is expected!  But it was interesting, and got the wheels turning...

What if we were to use a headless browser to render the page, something like [Selenium](http://selenium-python.readthedocs.io/), or [Splash](https://github.com/scrapinghub/splash), one of my favorites from the wonderful people at [ScrapingHub](https://scrapinghub.com/).  Or the myriad of other headless browser options out there.  What would happen then?  It was thinking this through, that it became clear it would work for caching the entirety of the page, but not in the way I had originally anticipated.

When I think of headless browsers, and the amazing things they do, one product is the HTML of the page, fully formed even after Javascript Ajax calls (which are incredibly common now).  However, I had not deeply considered what happens to other resources like images which are pulled in via `<img>` tags.  What do headless browsers do with these?  Are they content to leave them as-is?  or pull in the binary bits and drop those where the image would have landed?  Interesting in its own right, there was more!

By firing off a headless browser for a single item page -- that contains at least one additional image request via an `<img>` tag -- that should trigger the HTTP request needed for Varnish to cache that URL.  So, if one were to load that single item page after a headless browser already had, one would *not* receieve the entirety of the page pre-rendered like headless browsers provide, but would instead just be delighted with the virtually instant response of any HTTP requests the page needed.  

Which introduces this interesting area between raw, completely unrendered pages and archived instances (like WARC files).  If we cache each HTTP request the page requires, the only thing we leave to the browser is to actually put all the pieces together as a whole (including firing javascript).  

I realize as I type this out, that some of the nuance of the insight may be lost without more discussion, but suffice it to say, caching is an interesting and ceaselessly beguiling beast.
