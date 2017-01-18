---
published: false
---
An interesting aside about GET parameters, particularly of the multiple variety.

Solr accepts, where appropriate _expects_, the same GET parameter multiple times.  e.g. the `fq` parameter:

`http://example.org/solr/search?q=goober&fq=foo:bar&fq=foo:baz`





