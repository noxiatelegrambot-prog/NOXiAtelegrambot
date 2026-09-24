import httpx
from urllib.parse import quote


async def web_search(query: str) -> dict:
    url = f"https://html.duckduckgo.com/html/?q={quote(query)}"

    headers = {
        "User-Agent": "Mozilla/5.0 NOXiA-Researcher/1.0"
    }

    async with httpx.AsyncClient(
        headers=headers,
        timeout=20,
        follow_redirects=True,
    ) as client:
        response = await client.get(url)
        response.raise_for_status()

    from html.parser import HTMLParser

    class Parser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.results = []
            self.current = None
            self.buffer = []

        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)

            if tag == "a" and "result__a" in attrs.get("class", ""):
                self.current = {
                    "title": "",
                    "url": attrs.get("href", ""),
                    "snippet": "",
                }
                self.buffer = []

            elif tag == "a" and self.current:
                pass

            elif tag == "a":
                self.buffer = []

        def handle_data(self, data):
            if self.current is not None:
                self.buffer.append(data)

        def handle_endtag(self, tag):
            if tag == "a" and self.current:
                title = " ".join("".join(self.buffer).split())

                if title and self.current["url"]:
                    self.current["title"] = title
                    self.results.append(self.current)

                self.current = None
                self.buffer = []

    parser = Parser()
    parser.feed(response.text)

    results = parser.results[:5]

    if not results:
        raise RuntimeError("No web search results returned.")

    output = "\n\n".join(
        f"{r['title']}\n{r['url']}"
        for r in results
    )

    return {
        "query": query,
        "results": results,
        "output": output,
    }
