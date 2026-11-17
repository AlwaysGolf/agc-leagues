# AGC League Standings

Live league standings and the in-venue TV slideshow for Always Golf Club. Served at **leagues.alwaysgolf.com** through GitHub Pages.

- **Phones:** `leagues.alwaysgolf.com`
- **TV slideshow:** `leagues.alwaysgolf.com/?tv`

## How the data flows

The data lives in Google Sheets, so nobody edits this repo week to week.

1. Ryan enters scores in each league's master sheet, the same as always.
2. Each master sheet publishes **only its LEADERBOARD tab** to the web as CSV. Never publish the entire document, because the week tabs show who has paid.
3. The **AGC League Hub** sheet (in AGC MAIN) lists those CSV links (Leagues tab) and the TV promo slides (TV Promos tab).
4. The page reads the hub and the leaderboards every 5 minutes. Rankings, ties, and the "low round of the week" are calculated in the page.

New session: publish the new master sheets' LEADERBOARD tabs and paste the links into the hub. That's it.

## Files

- `index.html`: the built, self-contained page (what's served)
- `promos/`: images for TV promo slides (referenced from the hub's Image column)
- `src/`: source (`index.src.html`), build script, logos, and a snapshot of sheet data used as an offline fallback

The hub, promos, and records CSV links are set in `CONFIG` at the top of `src/index.src.html`. Rebuild with `python3 src/build.py`.
