---
published: false
---
## APIv2

I'm excited to say, work has commenced on a rewrite of [Digital Collection's primary API[(https://github.com/WSULib/ouroboros/tree/9c29ba6d30ac68aa235a7560f2e8d39d65d53ed4/WSUDOR_API)(pinning this link to a commit before the API disappears as we know it).  I also use the term "API" a bit loosely here, as it has served almost exclusively for internal use, powering our decoupled front-end.  Now an API that is used wholly internally certainly qualifies under the myriad of API definitions out there.  Where I challenge that coveted title is the lack of consistency and documentation it has exhibited until this point.

And that's okay!  Which, if one hasn't noticed already, is a running theme around here.

The API grew piecemeal with the rest of the ecosystem.  Where once it queried Solr directly for an object's metadata, later it would retrieve that Solr doc via a [method buried in an Ouroboros content-type object](https://github.com/WSULib/ouroboros/blob/9c29ba6d30ac68aa235a7560f2e8d39d65d53ed4/WSUDOR_Manager/models.py#L388-L389).  Where once we would fire off multiple API functions to fire -- member of collections, related objects, comprehension of images, etc. -- later they were grouped under a [`singleObjectPackage` class](https://github.com/WSULib/ouroboros/blob/9c29ba6d30ac68aa235a7560f2e8d39d65d53ed4/WSUDOR_API/functions/packagedFunctions.py#L30) that aggregated and returned all that information in single, sprawling response.  It's come a long way, and has proved to be extremely versatile, reliable, and fun to build.

But [as mentioned in a previous post](http://grahamhukill.com/blog/2016/11/08/framework-v2-frontend.html), we are in the process of re-building / refreshing the front-end, and the opportunity presented itself to rework, refine, and wildly improve a meandering bit of code.
