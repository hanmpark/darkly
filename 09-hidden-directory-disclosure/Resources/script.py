#!/usr/bin/env python3
import html.parser
import sys
import urllib.parse
import urllib.request
from collections import deque
from pathlib import Path

RESULTS_FILE = Path(__file__).with_name("results.txt")
DEFAULT_TIMEOUT = 10


class LinkParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() != "a":
            return
        for key, value in attrs:
            if key.lower() == "href" and value:
                self.links.append(value)
                break


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "curl/7.88"})
    with urllib.request.urlopen(req, timeout=DEFAULT_TIMEOUT) as response:
        return response.read().decode("utf-8", errors="replace")


def is_dir_link(href):
    return href.endswith("/") and href not in ("../", "./")


def is_readme_link(href):
    name = href.rstrip("/").split("/")[-1].lower()
    return name.startswith("readme") and not href.endswith("/")


def crawl(base_url):
    visited = set()
    queue = deque([base_url])
    lines = []

    while queue:
        current_url = queue.popleft()
        if current_url in visited:
            continue
        visited.add(current_url)

        try:
            page = fetch(current_url)
        except Exception as err:
            print(f"WARN: failed to fetch {current_url}: {err}", file=sys.stderr)
            continue

        parser = LinkParser()
        parser.feed(page)

        for href in parser.links:
            target_url = urllib.parse.urljoin(current_url, href)
            if is_dir_link(href):
                queue.append(target_url)
                continue
            if not is_readme_link(href):
                continue
            try:
                readme_content = fetch(target_url)
            except Exception as err:
                print(f"WARN: failed to fetch {target_url}: {err}", file=sys.stderr)
                continue
            one_line = " ".join(readme_content.splitlines()).strip()
            lines.append(f"{target_url} {one_line}")

    lines.sort()
    return lines


def write_results(lines):
    with RESULTS_FILE.open("w", encoding="utf-8") as output:
        for line in lines:
            output.write(f"{line}\n")


def grep_flag_lines():
    found = False
    with RESULTS_FILE.open("r", encoding="utf-8") as output:
        for line in output:
            if "flag" in line.lower():
                print(line.rstrip())
                found = True
    if not found:
        print("Aucune ligne avec le mot-cle 'flag' dans results.txt")


def main():
    if len(sys.argv) != 2:
        print("Usage: script.py <base_url>", file=sys.stderr)
        return 2

    base_url = sys.argv[1]
    if not base_url.endswith("/"):
        base_url += "/"

    lines = crawl(base_url)
    write_results(lines)
    grep_flag_lines()
    print(f"{len(lines)} lignes ecrites dans {RESULTS_FILE.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
