---
published: false
---
_I'm going to go on the record as saying I don't know if "opinionation" is a word, but I'd sure like it to be._

One of the most difficult, interesting, and complex things we deal with when building out a Digital Collections platform is representing information from digital objects in a meangingful way on the "front-end", access system.  In end-to-end frameworks like Rails or Django, there is often tight coupling between models and views.  If you give a model an attribute like `title`, it's relatively easy when rendering a page to say something along the lines of, `object.title` to place the title.

We do things a bit differently.  One of our goals from the beginning of this long and wild ride, has been a distinct and purposeful disconnect between our "back-end" and "front-end".  We use an in-house built API to communicate with our front-end, that renders relevant information to the page.  But in a situation like this, where coupling is a bit looser, where does one house opinions or translations from back-end, database fields to front-end, human readable information?  Where is the Solr field `rels_isMemberOfCollection` translated to `Collection`?  

Our solution in our v1 system was to have the front-end query the back-end _every page load_, requesting a hash of values to help translate.  It looked something like this:

```info:fedora/CM:AllImage
:
"AllImage"
info:fedora/CM:Archive
:
"Archive"
info:fedora/CM:Audio
:
"Audio"
info:fedora/CM:Collection
:
"Collection"
info:fedora/CM:Container
:
"Container"
info:fedora/CM:ContentModel
:
"ContentModel"
info:fedora/CM:Document
:
"Document"
info:fedora/CM:HierarchicalFiles
:
"HierarchicalFiles"
info:fedora/CM:Image
:
"Image"
info:fedora/CM:Issue
:
"Issue"
info:fedora/CM:LearningObject
:
"Learning Object"
info:fedora/CM:Serial
:
"Serial"
info:fedora/CM:Video
:
"Video"
info:fedora/CM:Volume
:
"Volume"
info:fedora/CM:WSUebook
:
"WSUebook"
info:fedora/wayne:collectionAmericanPressman
:
"American Pressman"
info:fedora/wayne:collectionCFAI
:
"Changing Face of the Auto Industry"
info:fedora/wayne:collectionDFQ
:
"Detroit Focus Quarterly"
info:fedora/wayne:collectionDPLAOAI
:
"DPLA OAI-PMH"
info:fedora/wayne:collectionDSJ
:
"The Detroit Sunday Journal"
info:fedora/wayne:collectionDennisCooper
:
"Dennis Glen Cooper Collection"
info:fedora/wayne:collectionDigDressColl
:
"Digital Dress Collection"
info:fedora/wayne:collectionHeartTransplant
:
"First U.S. Human-to-Human Heart Transplant"
info:fedora/wayne:collectionHermanMiller
:
"Herman Miller Consortium Collection"
info:fedora/wayne:collectionLincolnLetters
:
"The Lincoln Letters"
info:fedora/wayne:collectionMIM
:
"Made in Michigan Writers Series"
info:fedora/wayne:collectionMOT
:
"Michigan Opera Theatre Performance Images"
info:fedora/wayne:collectionNightingale
:
"Florence Nightingale Collection"
info:fedora/wayne:collectionRENCEN
:
"Building the Detroit Renaissance Center"
info:fedora/wayne:collectionRamsey
:
"Eloise Ramsey Collection of Literature for Young People"
info:fedora/wayne:collectionReuther
:
"Walter P. Reuther Library Collection"
info:fedora/wayne:collectionReutherSwanger
:
"Toni Swanger Papers"
info:fedora/wayne:collectionUniversityBuildings
:
"Wayne State University Buildings Collection"
info:fedora/wayne:collectionVanRiperLetters
:
"Van Riper Family Correspondence"
info:fedora/wayne:collectionWPAscores
:
"WPA Music Manuscripts"
info:fedora/wayne:collectionWSUebooks
:
"Wayne State University eBooks"
info:fedora/wayne:collectionvmc
:
"Virtual Motor City"
```

