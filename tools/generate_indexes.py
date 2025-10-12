import os, re
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('../tools/'))

def get_title_from_html(path):
    try:
        with open(path, encoding='utf-8') as f:
            html = f.read()
        match = re.search(r'<title>(.*?)</title>', html, re.I)
        return match.group(1).strip() if match else None
    except Exception:
        return None

def is_image(fname):
    return any(fname.lower().endswith(ext) for ext in ('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'))

template = env.get_template('index_template.html')

for root, dirs, files in os.walk('.'):
    if root.startswith('./.git') or '/.' in root:
        continue

    # Dateien im aktuellen Verzeichnis sammeln
    fileitems = []
    for fname in sorted(files):
        if fname == 'index.html' or fname.startswith('.'):
            continue
        path = os.path.join(root, fname)
        relpath = fname  # relative Pfade aus Sicht des Verzeichnisses
        info = {
            "name": fname,
            "relpath": relpath,
            "is_image": is_image(fname),
            "title": get_title_from_html(path) if fname.endswith('.html') else None,
        }
        fileitems.append(info)
    diritems = [{"name":"back","relpath":".."}]
    for dname in sorted(dirs):
        if dname.startswith('.'):
            continue
        info = {
            "name" : dname,
            "relpath" : dname
        }
        diritems.append(info)

    # Nur schreiben, wenn das Verzeichnis Dateien enthält
    if fileitems or diritems:
        output = template.render(
            directory_name=os.path.basename(root) or "Startseite",
            files=fileitems,
            dirs=diritems
        )
        outpath = os.path.join(root, 'index.html')
        if (not os.path.exists(outpath)):
            descriptor = os.open(
                path=outpath,
                flags=(
                    os.O_WRONLY  # access mode: write only
                    | os.O_CREAT  # create if not exists
                    | os.O_TRUNC  # truncate the file to zero
                ),
                mode=0o777
            )
            with open(descriptor, 'w', encoding='utf-8') as out:
                out.write(output)
            print(f"✅ {outpath} erstellt.")
        else:
            print(f"{outpath} nicht erstellt. Rechte vorhanden: {os.access(outpath, os.W_OK)}")
