#!/usr/bin/env python3
import json
import glob

def fix_notebook_languages(nb_path):
    """Fix VSCode languageId for cells with correct Python detection"""
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
        
        changed = False
        
        # Check each code cell
        for cell in nb.get('cells', []):
            if cell['cell_type'] != 'code':
                continue
            
            # Get cell source content
            source = ''.join(cell.get('source', []))
            stripped = source.strip()
            
            # Skip cells with Jupyter magic commands - they define their own language
            if stripped.startswith('%%'):
                continue
            
            # Determine if this is Python code
            is_python_code = (
                # Python-specific patterns
                'print(' in source or
                'import ' in source or
                'from ' in source or
                'def ' in source or
                'class ' in source or
                ('for ' in source and ' in ' in source) or
                'while ' in source or
                (source.lstrip().startswith('#') and '#' in source) or
                'self.' in source or
                'if ' in source and ' == ' in source and ': ' in source or
                'return ' in source or
                'len(' in source or
                'range(' in source or
                'sum(' in source or
                'max(' in source or
                'min(' in source or
                'if ' in source and 'for' in source  # comprehension
            )
            
            # Don't trust source detection alone for small code
            if len(source) < 20:
                continue
            
            # Check VSCode metadata
            if 'metadata' not in cell:
                cell['metadata'] = {}
            
            if 'vscode' not in cell['metadata']:
                cell['metadata']['vscode'] = {}
                
            vscode_meta = cell['metadata']['vscode']
            current_lang = vscode_meta.get('languageId', '')
            
            # Only fix if it's marked as JavaScript and we're confident it's Python
            if is_python_code and current_lang == 'javascript':
                vscode_meta['languageId'] = 'python'
                changed = True
                preview = source.split('\n')[0][:50]
                print(f"  Fixed: {preview}...")
        
        if changed:
            with open(nb_path, 'w', encoding='utf-8') as f:
                json.dump(nb, f, indent=1)
            return True
        
        return False
        
    except Exception as e:
        print(f"  Error: {e}")
        return False

# Process all notebooks
notebooks = glob.glob("_notebooks/**/*.ipynb", recursive=True)
fixed_count = 0

print("Fixing notebook cell languages...")
for nb_path in sorted(notebooks):
    if fix_notebook_languages(nb_path):
        print(f"✓ {nb_path}")
        fixed_count += 1

print(f"\n✓ Fixed {fixed_count} notebooks ({len(notebooks)} total processed)")
