import urllib.request, urllib.parse, re, ssl, base64

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def bing_search(query):
    q = urllib.parse.quote(query)
    url = f'https://www.bing.com/search?q={q}&count=15'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0'})
    with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    results = []
    seen = set()
    for m in re.finditer(r'href="https://www\.bing\.com/ck/a\?[^"]*?u=a1([^&"]+)', html):
        pad = m.group(1) + '=' * (-len(m.group(1)) % 4)
        try:
            r = base64.urlsafe_b64decode(pad).decode('utf-8', errors='ignore')
            if r not in seen:
                seen.add(r)
                results.append(r)
        except Exception:
            pass
    return results

print('Buku siswa XI/XII Kemendikbudristek Kurikulum Merdeka:')
for r in bing_search('site:repositori.kemendikdasmen.go.id OR site:repositori.kemdikbud.go.id "Cerdas Cergas" "Bahasa dan Bersastra" "Kelas X" pdf'):
    print(' ', r)
