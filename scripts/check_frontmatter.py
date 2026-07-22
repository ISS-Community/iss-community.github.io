import os, json
root = r"c:\Users\bugra\bugthe"
problems = []
md_files = []
for dirpath, dirnames, filenames in os.walk(root):
    for fn in filenames:
        if fn.endswith('.md'):
            md_files.append(os.path.join(dirpath, fn))

for f in sorted(md_files):
    with open(f, 'r', encoding='utf-8-sig') as fh:  # utf-8-sig handles BOM
        txt = fh.read()
    fm_ok = False
    if txt.lstrip().startswith('---'):
        parts = txt.split('\n')
        found = False
        for i,line in enumerate(parts[1:], start=1):
            if line.strip() == '---':
                found = True
                break
        fm_ok = found
    tab_lines = []
    for i,line in enumerate(txt.splitlines(), start=1):
        if '\t' in line:
            tab_lines.append(i)
    if not fm_ok:
        problems.append({'file': os.path.relpath(f, root), 'issue': 'missing_or_unclosed_frontmatter'})
    if tab_lines:
        problems.append({'file': os.path.relpath(f, root), 'issue': 'tab_characters_in_file', 'lines': tab_lines[:10]})

out = {'checked': len(md_files), 'problems': problems}
print(json.dumps(out, ensure_ascii=False, indent=2))
