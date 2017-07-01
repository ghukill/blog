---
published: false
---
## Infradata

Stumbled on an interesting concept this morning while sipping coffee in a windowed seat.  But before the topic at hand, "stumbled"?  Good grief.  Perhaps I should say, "while paddling through the dewey, glass-like passages of morning's inlets, I came across a beach..."  Beach, stumbled, semantics.

I stumbled on the concept of *infradata*, while [reading a blog post from Ed Summers on, you guessed it, *infradata*](https://inkdroid.org/2017/05/18/infradata/).  That was 79% of the way into the weaving a few ideas.  This blog post cites [an article by Fidler and Acker](http://onlinelibrary.wiley.com/doi/10.1002/asi.23660/abstract) that more formally introduces and defines the idea of *infradata*.  Ed's blog post was outlining a neat project about creating a Twitter bot that monitors the structure of the Twitter API response, tweeting changes to the underlying "blueprint" as they occur.  I thought this was interesting at first, but it wasn't until reading more of the Fidler and Acker's article did it click.

So what is *infradata*?  Only one cup of coffee deep into the topic, weaering sunglasses indoors to block the beautiful July 1st sun, I'm about as equipped to summarize as a colander is for pouring water.  But here goes.  In these early glimpses, I get the idea that *infradata* is metadata required by a particular scoped infrastructure to operate.  Said another way, how it strikes me now, it's metadata that serves to represent the current state of objects *in situ* in a given infrastructure.

### Coat check analogy

I love analogies.

My quick and dirty working analogy is a coat check.  When I drop off my coat at a coat check, I'm given a small arrow-shaped piece of paper that says "13" on it.  Then, they hang my coat on rack 3, in room B.  they jot down "rack 3 / room B" on their similar looking ticket that says "13", and file it behind 12, but before 14.  

Okay, I realize this isn't how coat checks work, but a little bit of dramatization and unnecessary complexity makes for a nice, tangible "network" of coats.

My coat is no longer my coat, it is now coat "13".  And it floats listlessly in the sea of coats they have squirreled away.  The only lifeline that the coat has with me, with identity outside of its vapid existence as "coat in coat closet", is the number "13" and the *infradata* that accompanies it.  "13" is the identifier of my *infradata* record, a record which details the precise, and current, location and state of my coat.  Without this bit of information, it's as good as lost.  Without this bit of information, the infrastructure has met its entropic end.  

**To follow up on:** *infradata* or *metadata* as cooling agent in information system imagined as thermodynamic system, staving entropy and the homogenization of uniqueness in records.

### Back to reality

The original blog post was 79% of idea coagulation, the Fidley and Acker article pushing to 100%, but what laid the groundwork for 0% - 78%?  Months, years now, of thinking about the invisible forces of complex systems (infrastructures).

Without perfect surrogates, I humbly submit the concept of *opinionation* as a related term to *infradata*.  Or, *infradata* as the instantiation of *opinionation*.

And, [an article from Microsoft Research asking, "What is a File?"](https://www.microsoft.com/en-us/research/wp-content/uploads/2011/10/MSR-TR-2011-109.pdf).  I must admit I haven't finished the article, but what I have read, it begins to prod the idea of a "file".  When I upload the file `cactus.jpg` to Google Drive, I am rewarded with a link to `cactus.jpg` in my Drive folder.  But where is that file?  There is not a single harddrive in California, with the directory structure `/Google/Drive/ghukill/images/` with my file there.  Oh no, cloud storage is distrubuted.  The file is moving.  The file is duplicated.  The file is versioned.  The only way that Google can return the bytes from `cactus.jpg` when I request it, is by using some kind of *infradata* internal to their Drive infrastructure, but hovering above my `cactus.jpg` metadata that may contain descriptive information, exif data, etc.  

And this is key: my *very* early understanding of the idea of *infradata* is that it is metadata that describes the **state** of an object *in situ*, but is not metadata that will accompany the object through various states and infrastructures.

So what is this *opinionation* connection?  Going back to my coat check example, where is it codified that they will:

  * create two tickets with the same identifier ("13"), keep one, and give me one?
  * record the room and rack information on their ticket?
  
Perhaps it is not, but it's just *the way that things are done*.  That's a very dangerous phrase, and unforutnately, one that I think accompanies *opinionation* often.  These are loose connections I realize, but they feel related.  *Infradata* is unique in that follows the *opinionation* of an infrastructure, valuable in that it and the infrastructure are expecting the same values, ephmeral because it is lost when the state of the object changes.  

Do we need to save *infradata*?  Is it enough just to understand that it temporarily exists to shephard an object through time and space? 
  
  
