import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1280, "height": 900})
        for _ in range(30):
            try:
                await pg.goto("http://localhost:4336/research/", wait_until="networkidle"); break
            except Exception:
                await asyncio.sleep(0.5)
        await pg.screenshot(path=sys.argv[1])
        await b.close()
asyncio.run(main())
