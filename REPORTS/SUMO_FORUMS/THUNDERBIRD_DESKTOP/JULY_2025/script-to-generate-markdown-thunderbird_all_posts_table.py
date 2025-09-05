import json, re, pandas as pd

PATH = '2025-07-sumo-questions-desktop.json'
with open(PATH, 'r', encoding='utf-8') as f:
    posts = json.load(f)

CATS = [
    'Authentication Issues','Calendar Issues','Contacts Issues',
    'Sending Email Problems','Receiving Email Problems',
    'IMAP Issues','POP3 Issues','Other / Miscellaneous'
]

KEYS = {
    'Authentication Issues': [r'pass(word|code)?', r'log ?in|sign ?in', r'auth(enticat(e|ion)|\b)', 
                              r'credential', r'app(lication)? password', r'2fa|two[- ]factor', r'xoauth2|oauth'],
    'Calendar Issues': [r'calendar|caldav|lightning|\bics\b'],
    'Contacts Issues': [r'contacts?|address book|carddav|\bvcf\b'],
    'Sending Email Problems': [r'send(ing)?|smtp|outgoing'],
    'Receiving Email Problems': [r'receiv(e|ing)|incoming|download|sync|fetch|Get Messages|new mail'],
    'IMAP Issues': [r'\bimap\b|imaps|port 993'],
    'POP3 Issues': [r'\bpop3?\b|port 110|port 995'],
}

def id_from_url(u): return re.search(r"(\d+)$", u).group(1) if re.search(r"(\d+)$", u) else ""
def short(text, n=20):
    if not text: return ""
    words = re.sub(r"\s+", ' ', re.sub(r"https?://\S+", '', text)).strip().split()
    return ' '.join(words[:n]) + ('…' if len(words) > n else '')

rows = []
for p in posts:
    title, link, content = p.get('title','').strip(), p.get('question_link','').strip(), p.get('question_content','') or ''
    blob = f"{title}\n{content}".lower()
    assigned = 'Other / Miscellaneous'
    for cat in CATS:
        if cat in KEYS and any(re.search(rx, blob) for rx in KEYS[cat]):
            assigned = cat
            break
    rows.append({"Category": assigned, "Post Link": f"[{id_from_url(link)}: {title}]({link})", "Brief Description": short(content, 20)})

df = pd.DataFrame(rows)
df.to_markdown("thunderbird_all_posts_table.md", index=False)

