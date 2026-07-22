import os, yaml, json

root = r"c:\Users\bugra\bugthe"
problems = []

# Check all YAML files
for dirpath, dirnames, filenames in os.walk(root):
    # Skip .git and node_modules
    dirnames[:] = [d for d in dirnames if d not in ['.git', 'node_modules', '.jekyll-cache']]
    
    for fn in filenames:
        if fn.endswith(('.yml', '.yaml')):
            fpath = os.path.join(dirpath, fn)
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    yaml.safe_load(f)
            except yaml.YAMLError as e:
                problems.append({
                    'file': os.path.relpath(fpath, root),
                    'error': str(e)
                })
            except Exception as e:
                problems.append({
                    'file': os.path.relpath(fpath, root),
                    'error': f"{type(e).__name__}: {str(e)}"
                })

# Check markdown frontmatter
md_count = 0
for dirpath, dirnames, filenames in os.walk(os.path.join(root, 'content')):
    for fn in filenames:
        if fn.endswith('.md'):
            md_count += 1
            fpath = os.path.join(dirpath, fn)
            with open(fpath, 'r', encoding='utf-8') as f:
                txt = f.read()
            if not txt.startswith('---'):
                problems.append({
                    'file': os.path.relpath(fpath, root),
                    'error': 'Missing opening frontmatter delimiter'
                })

out = {'yaml_files_checked': len([f for d, _, fs in os.walk(root) for f in fs if f.endswith(('.yml', '.yaml'))]),
       'markdown_files_checked': md_count,
       'problems': problems}
print(json.dumps(out, ensure_ascii=False, indent=2))
