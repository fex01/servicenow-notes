"""Small fence-aware Markdown scanner, deliberately not a full CommonMark parser."""
import re
from collections import defaultdict

def visible_lines(text):
    fence_char = None
    fence_len = 0
    for n, line in enumerate(text.splitlines(), 1):
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})(.*)$', line)
        # Labs contain fences indented four spaces as list children.
        if not match:
            match = re.match(r'^ {4}(`{3,}|~{3,})(.*)$', line)
        if match:
            marker, rest = match.groups()
            if fence_char is None:
                fence_char, fence_len = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_len and not rest.strip():
                fence_char = None
            continue
        if fence_char is None:
            yield n, line

def headings(text):
    for n, line in visible_lines(text):
        m = re.match(r'^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$', line)
        if m: yield n, len(m.group(1)), m.group(2)

def anchors(text):
    seen = defaultdict(int); result = set()
    for _, _, heading in headings(text):
        heading = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', heading.lower())
        heading = re.sub(r'<[^>]+>', '', heading)
        base = re.sub(r'[^\w\- ]', '', heading).replace(' ', '-')
        count = seen[base]; seen[base] += 1
        result.add(base + (f'-{count}' if count else ''))
    return result
