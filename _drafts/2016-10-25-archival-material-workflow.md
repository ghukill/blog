---
published: false
---
## Archival Material Ingest Workflow

It has taken quite some time, but we've honed in on a workflow for ingesting archival materials from the Reuther library -- aka, University Archives here on campus -- into our Fedora Commons based repository.  Turns out, the following is all there is to it!

![archival_ingest_workflow.jpg]({{site.baseurl}}/assets/images/archival_ingest_workflow.jpg)

Rest assured, there are more to those arrows than immediately meets the eye.  Let's dive in.

Our goal was to take digitized archival materials from the Reuther Library and provide preservation and access via our [Digital Collections](http://digitalcollections.nypl.org/about) infrastructure.  At a very high level, we were imagining **one digital object in Fedora for each digital file coming from the archives**.

But we were realistic from the get-go, it was going to be a much larger enterprise than file-by-file.  How would we manage ingest and description at scale?  To answer that, we need to look at the systems in play: [Archivematica](https://www.archivematica.org/en/) and [ArchivesSpace](http://archivesspace.org/).

**Archivematica** is a series of tubes.  To be more precise, micro-services.  Archivematica takes groups of files, runs them through a host of preservation micro-services -- virus scanning, file format normalization, checksumming, etc. -- and ties them up together in a tidy bow with an over-arching [METS](http://www.loc.gov/standards/mets/) file.  Archivematica is inspired by the venerable [OAIS model (Open Archival Information System)]()https://en.wikipedia.org/wiki/Open_Archival_Information_System), and as such, speaks in terms of [AIPs, SIPs, and DIPs](https://en.wikipedia.org/wiki/Open_Archival_Information_System#The_functional_model).  

We are using Archivematica as means to get actual, discrete digital files from the Reuther into a format that we can batch process them for ingest.  Additionally, we get all the preservation friendly treatment from the micro-services, and begin a paper trail of metadata about the files journey.  It's quite possible we'll dig deeper into affordances and functionality of AM (it's time to shorten), but for now, it's primarily a virus checking, checksumming, METS writing, server/building spanning networked pipeline for us.  And it's going to be great!

The next dish in the cupboard is **ArchivesSpace**.  ArchivesSpace, save a lengthy and highly passionate and opinionated rant here, is the next generation of archival software to handle description, management of information around materials, discovery, and much more.  Our partner in crime, the Reuther Library, is slowly switching to ASpace to handle their description and information management.  It is a database driven application, that still also exports finding aids for archival collections in EAD.  We'll be using those, with plans to leverage the API once deploymente has settled down a bit.


