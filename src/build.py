"""Build a single self-contained index.html (preview snapshot + assets inlined)."""
import base64, json, pathlib

ROOT = pathlib.Path(__file__).parent
d = lambda p: (ROOT / "data" / p).read_text()
b64 = lambda p, mime: f"data:{mime};base64," + base64.b64encode((ROOT / "assets" / p).read_bytes()).decode()

snapshot = {
    "asOf": "2026-11-17T17:00:00-05:00",
    "leagues": [
        {"id": "4-person-scramble", "name": "4-Person Scramble", "csv": d("4man-scramble.csv")},
        {"id": "2v2-scramble", "name": "2v2 Scramble", "csv": d("2v2-scramble.csv")},
        {"id": "ladies-2v2", "name": "Ladies 2v2 Scramble", "csv": d("ladies-2v2.csv")},
        {"id": "best-ball", "name": "2v2 Best Ball", "csv": d("2v2-bestball.csv")},
        {"id": "individual", "name": "Individual Play Anytime", "csv": d("individual.csv")},
    ],
    "records": d("records.csv"),
    "promos": [
        {"headline": "Christmas Classic", "when": "Saturday, December 19 · 10am–2pm or 8pm–close",
         "details": "27-hole 4-person scramble. $50/golfer or $200/team, with a tee gift, pizza, and over $1,000 in prizes. Limited team spots!",
         "link": "https://www.alwaysgolf.com/christmas-classic", "image": b64("promo-christmas-classic.jpg", "image/jpeg")},
        {"headline": "Throw Your Holiday Party Here", "when": "Company parties, team nights & full-venue buyouts",
         "details": "Sims, a full bar, and food for the whole crew. Golfers and non-golfers alike have a blast. We'll handle the details.",
         "link": "https://www.alwaysgolf.com/events", "image": ""},
        {"headline": "Grab Your Crew & Book a Sim", "when": "Open 7 days a week",
         "details": "2,600+ courses, full bar, and a spot for every kind of golfer. First-timers welcome.",
         "link": "https://www.alwaysgolf.com", "image": ""},
    ],
}

html = (ROOT / "index.src.html").read_text()
qrlib = (ROOT / "vendor" / "qrcode.js").read_text()
html = html.replace("/*QRLIB*/", qrlib.replace("</script", "<\\/script"))
html = html.replace("/*SNAPSHOT*/", json.dumps(snapshot).replace("</", "<\\/"))
html = html.replace("__LOGOINV__", b64("logo-inverse.png", "image/png"))
html = html.replace("__LOGO__", b64("logo.png", "image/png"))
html = html.replace("__COIN__", b64("coin.png", "image/png"))
OUT = ROOT.parent
(OUT / "index.html").write_text(html)
(OUT / "CNAME").write_text("leagues.alwaysgolf.com\n")
print("built", len(html) // 1024, "KB")
