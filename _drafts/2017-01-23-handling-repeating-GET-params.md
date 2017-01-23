---
published: false
---
Re: the last couple of posts about repeating GET parameters, and how PHP is slightly unconventional in how it parses.  Came up with a solution: a `QueryBuilder` class.

![IMG_20170123_140040.jpg]({{site.baseurl}}/assets/images/IMG_20170123_140040.jpg)

It was a particularly pernicious problem, and time will tell how well our solution scales and evolves.  The problem came down to how the [Slim PHP framework](https://www.slimframework.com/) parsed GET parameters, and the [Guzzle PHP client](http://docs.guzzlephp.org/en/latest/) encoded `GET` requests.  

Slim used the built-in PHP function, [`parse_str`](http://php.net/manual/en/function.parse-str.php) that followed the PHP convention to _only_ capture repeating `GET` parameters when the `GET` parameter string contained square brackets `[]` around those repeating fields.  For example: 

`?fq=foo&fq=bar` would get truncated to `'fq'=>'bar'`

However, the repeating values would get picked up from `?fq[]=foo&fq[]=bar`, and become `'fq'=['foo','bar']`.