---
layout: page
title: archive
permalink: /archive/
---
{% for post in site.posts %}
* [{{ post.title }}]({{ post.url | prepend: site.baseurl }}) - {{ post.date | date: "%b %-d, %Y" }}
{% endfor %}