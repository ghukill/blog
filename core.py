import glob
import json
from pathlib import Path

import frontmatter
import markdown

def markdown_to_html(filepath:str):
    i = Path(filepath)
    with open(i) as fi:
        post = frontmatter.loads(fi.read())
        html = markdown.markdown(post.content)

        html = html.replace("{{site.baseurl}}/assets/images", "images")

        title = i.stem
        html = f"<h1>{title}</h1>\n<pre><code>{json.dumps(post.metadata, indent=2)}</code></pre>\n{html}"

        o = i.stem + ".html"
        with open(Path("posts/html") / o, 'w') as fo:
            fo.write(html)

def convert_all_markdown_to_html(directory:str = "posts/markdown"):
    for i in Path(directory).glob("*.md"):
        markdown_to_html(str(i))
    print("conversion complete")

def build_index_html():
    # TODO: let's use jinja!
    print("index building not yet implemented")
