#!/usr/bin/env python3
"""Fast notebook conversion for Homework1 files only"""
import os
import json
import nbformat
from pathlib import Path
from datetime import datetime

def convert_single_file(notebook_path):
    """Convert a single notebook to markdown"""
    try:
        with open(notebook_path, 'r') as f:
            nb = nbformat.read(f, as_version=4)
        
        # Extract front matter
        front_matter = {}
        if nb.cells and nb.cells[0].cell_type == 'raw':
            try:
                raw_text = nb.cells[0].source
                if raw_text.startswith('---'):
                    fm_text = raw_text.split('---')[1]
                    for line in fm_text.strip().split('\n'):
                        if ':' in line:
                            key, val = line.split(':', 1)
                            front_matter[key.strip()] = val.strip()
            except:
                pass
        
        # Build markdown
        md_content = "---\n"
        md_content += f"layout: post\n"
        for key, val in front_matter.items():
            md_content += f"{key}: {val}\n"
        md_content += "---\n\n"
        
        # Convert cells
        for cell in nb.cells[1:]:
            if cell.cell_type == 'markdown':
                md_content += cell.source + "\n\n"
            elif cell.cell_type in ['code', 'html']:
                if cell.source.strip():
                    md_content += f"```\n{cell.source}\n```\n\n"
        
        return md_content
    except Exception as e:
        print(f"Error converting {notebook_path}: {e}")
        return None

# Create Homework1 posts directory
homework_dir = Path("_posts/Homework1")
homework_dir.mkdir(parents=True, exist_ok=True)

# Convert all Homework1 notebooks
notebook_files = sorted(Path("_notebooks/Homework1").glob("*.ipynb"))
print(f"Converting {len(notebook_files)} Homework1 notebooks...")

for i, nb_path in enumerate(notebook_files, 1):
    output_name = nb_path.stem + "_IPYNB_2_.md"
    output_path = homework_dir / output_name
    
    content = convert_single_file(nb_path)
    if content:
        with open(output_path, 'w') as f:
            f.write(content)
        print(f"  [{i}/{len(notebook_files)}] ✓ {nb_path.name}")
    else:
        print(f"  [{i}/{len(notebook_files)}] ✗ {nb_path.name}")

print(f"\n✓ Conversion complete: {len(list(homework_dir.glob('*.md')))} markdown files created")
