#!/usr/bin/env python3
"""Static pre-build validation for the Clienvora technical SEO checklist site.

Runs the checks that would otherwise require a Jekyll build:
  * HTML tag balance on every page (and the homepage)
  * Valid JSON-LD on every page
  * Every internal /categories/<slug>/ link resolves to an existing page
  * Jekyll template braces are well-formed (no stray single-brace site.baseurl)
  * Every page links to the homepage and carries the standard CTA + PDF link
  * Meta descriptions within 120-160 characters on the 12 new cluster pages
  * Every page has a Tools section with at least one paid and one free badge

Usage:
  python3 scripts/prebuild-check.py
Exit code 0 when all checks pass, 1 otherwise.
"""
import glob
import json
import re
import sys

ROOT = '/home/amir/Desktop/technical-seo-checklist'
PAGES = sorted(glob.glob(f'{ROOT}/categories/*/index.html'))
NEW_PAGES = [
    'javascript-rendering', 'indexing-canonicalization', 'international-seo',
    'redirects-status-codes', 'crawl-budget-log-analysis', 'image-seo',
    'on-page-technical', 'cdn-caching-hosting', 'ecommerce-faceted-nav',
    'accessibility-a11y', 'eeat-entities', 'site-migrations',
]
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
        'link', 'meta', 'param', 'source', 'track', 'wbr'}


def tag_balance(txt):
    stack = []
    for m in re.finditer(
            r'<(/?)([a-zA-Z][a-zA-Z0-9]*)((?:"[^"]*"|\'[^\']*\'|[^>"\'])*)>',
            txt):
        closing, tag, attrs = m.group(1), m.group(2).lower(), m.group(3)
        if tag in VOID or attrs.strip().endswith('/'):
            continue
        if closing:
            if not stack or stack[-1] != tag:
                return False, f'unexpected </{tag}> (top of stack: {stack[-1] if stack else "empty"})'
            stack.pop()
        else:
            stack.append(tag)
    return (True, 'ok') if not stack else (False, f'unclosed: {stack[:5]}')


def main():
    problems = []
    all_slugs = set(p.split('/')[-2] for p in PAGES)

    for f in PAGES:
        slug = f.split('/')[-2]
        txt = open(f).read()

        ok, err = tag_balance(txt)
        if not ok:
            problems.append(f'{slug}: TAG {err}')

        for jm in re.finditer(
                r'<script type="application/ld\+json">(.*?)</script>',
                txt, re.S):
            try:
                json.loads(jm.group(1))
            except Exception as exc:
                problems.append(f'{slug}: JSONLD {str(exc)[:60]}')

        if 'site.baseurl }}/"' not in txt:
            problems.append(f'{slug}: missing homepage link')

        if txt.count('https://www.clienvora.com') < 1:
            problems.append(f'{slug}: missing clienvora CTA')
        if txt.count('https://wa.link/m9rotk') < 1:
            problems.append(f'{slug}: missing whatsapp CTA')
        if txt.count('technical-seo-checklist-2026.pdf') < 1:
            problems.append(f'{slug}: missing PDF link')

        if 'Related <span>Checklists</span>' not in txt:
            problems.append(f'{slug}: missing Related Checklists section')

        if re.search(r'(?<!\{)\{ site\.baseurl \}(?!\})', txt):
            problems.append(f'{slug}: single-brace site.baseurl bug')

        for lm in re.finditer(r'{{ site.baseurl }}/categories/([a-z0-9-]+)/', txt):
            if lm.group(1) not in all_slugs:
                problems.append(f'{slug}: broken link to {lm.group(1)}')

        free = len(re.findall(r'<span class="badge badge-free">', txt))
        paid = len(re.findall(r'<span class="badge badge-paid">', txt))
        if free < 1 or paid < 1:
            problems.append(f'{slug}: Tools section lacks free+paid badges (free={free}, paid={paid})')

    ok, err = tag_balance(open(f'{ROOT}/index.html').read())
    if not ok:
        problems.append(f'index.html: TAG {err}')

    for slug in NEW_PAGES:
        f = f'{ROOT}/categories/{slug}/index.html'
        m = re.search(r'^description:\s*(.*)$', open(f).read(), re.M)
        if m:
            length = len(m.group(1).strip())
            if not 120 <= length <= 160:
                problems.append(f'{slug}: description length {length} (want 120-160)')

    if problems:
        print(f'{len(problems)} problem(s) found:')
        for p in problems:
            print(f'  {p}')
        return 1
    print(f'OK: {len(PAGES)} category pages + index.html passed all checks.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
