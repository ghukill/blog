#!/usr/bin/env -S uv run --script

from core import build_index_html, convert_all_markdown_to_html

convert_all_markdown_to_html()
build_index_html()
