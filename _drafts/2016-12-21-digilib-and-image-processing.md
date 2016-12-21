---
published: false
---

I am following a thread on the [IIIF](http://iiif.io/) [Google group forum](https://groups.google.com/forum/#!forum/iiif-discuss), ruminating on how IIIF and the Image API might support more advanced image processing.  I am probably mis-characterizing, or reading too much into the conversation a bit, but something interesting to me emerged from some of the early comments.

There was the acknowledgement that as stewards of digital images, looking to the future, it's likely that we will start undertaking image processing - OCR, classification, etc. -- on the images we have at our disposal.  Perhaps for metadata enrichment, digital humanities work, the possibilities are extensive.  IIIF, and the Image API, provide an excellent and standardized way to access images.  Image processing is helped by preparing images in particular ways, such as converting to grayscale to help detect nodes and edges, that IIIF might be able to help with.  What if the API, in addition to rotating, scaling, selecting, and some limited color options, could help facilitate image processing of our visual resources?

This conversation has been fascinating on many levels.  

Robert Casties responded to the thread, pointing out that the project [digilib](http://digilib.sourceforge.net/) has some methods and functionality that would do just such things.  I wasn't familiar with digilib, but what a neat project!  Appears to be out of Germany, dating back to the early to mid 2000's.  In many ways, it mirrors the IIIF ecosystem of image servers, and standardized APIs for requesting these images.  Details drift and overlap here and there, but it's devilishly similar to image servers such as [Loris](https://github.com/loris-imageserver/loris) (which we use here at Wayne) or [Canteloupe](https://medusa-project.github.io/cantaloupe/).