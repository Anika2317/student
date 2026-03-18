#!/usr/bin/env python3
"""Full notebook conversion with correct metadata"""
import os
import json
import yaml
from pathlib import Path
from nbformat import read

def extract_frontmatter(nb):
    """Extract YAML front matter from notebook"""
    if nb.cells and nb.cells[0].cell_type == 'raw':
        raw = nb.cells[0].source
        if raw.startswith('---'):
            try:
                fm_str = raw.split('---')[1]
                return yaml.safe_load(fm_str)
            except:
                return {}
    return {}

def convert_notebooks_full():
    """Convert all notebooks with proper categories"""
    from nbconvert import MarkdownExporter
    
    notebook_dir = Path("_notebooks")
    posts_dir = Path("_posts")
    
    total_converted = 0
    
    # Convert all notebooks
    for nb_path in sorted(notebook_dir.rglob("*.ipynb")):
        if '.ipynb_checkpoints' in str(nb_path):
            continue
        
        try:
            with open(nb_path) as f:
                nb = read(f, as_version=4)
            
            # Extract front matter
            fm = extract_frontmatter(nb)
            
            # Determine output path maintaining directory structure
            rel_path = nb_path.relative_to(notebook_dir)
            output_filename = rel_path.stem + '_IPYNB_2_.md'
            output_path = posts_dir / rel_path.parent / output_filename
            output_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Convert notebook
            exporter = MarkdownExporter()
            md_content, _ = exporter.from_filename(str(nb_path))
            
            # Update front matter with correct categories
            lines = md_content.split('\n')
            
            # Find and preserve existing front matter
            if lines[0] == '---':
                end_fm = 0
                for i in range(1, len(lines)):
                    if lines[i] == '---':
                        end_fm = i
                        break
                fm_text = '\n'.join(lines[1:end_fm])
                body = '\n'.join(lines[end_fm+1:])
            else:
                fm_text = ''
                body = md_content
            
            # Rebuild front matter with proper categories
            fm_dict = {}
            if fm_text:
                for line in fm_text.split('\n'):
                    if ':' in line:
                        k, v = line.split(':', 1)
                        fm_dict[k.strip()] = v.strip()
            
            # Preserve or set categories based on directory
            if 'Homework' in str(rel_path) or 'homework' in str(rel_path):
                fm_dict['categories'] = "['Javascript', 'Homework']"
            
            # Rebuild markdown with clean front matter
            new_md = "---\n"
            for key in ['layout', 'title', 'description', 'categories', 'permalink', 'author', 'type']:
                if key in fm_dict:
                    val = fm_dict[key]
                    new_md += f"{key}: {val}\n"
            new_md += "---\n\n" + body
            
            with open(output_path, 'w') as f:
                f.write(new_md)
            
            total_converted += 1
            print(f"✓ {rel_path}")
            
        except Exception as e:
            print(f"✗ {nb_path}: {e}")
    
    print(f"\n✓ Converted {total_converted} notebooks")

if __name__ == "__main__":
    convert_notebooks_full()
