#!/usr/bin/env python3
"""
Generate LaTeX paper listings from papers.yml
Run this script whenever you update _data/papers.yml to regenerate the LaTeX include file.

Usage: python generate_latex_papers.py
"""

import yaml
from pathlib import Path

# Paths - relative to this script's location in assets/files/cvlatex/
SCRIPT_DIR = Path(__file__).parent
YAML_PATH = SCRIPT_DIR / ".." / ".." / ".." / "_data" / "papers.yml"
OUTPUT_PATH = SCRIPT_DIR / "papers_generated.tex"


def escape_latex(text: str) -> str:
    """Escape special LaTeX characters."""
    replacements = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "–": "--",  # en-dash
        "—": "---",  # em-dash
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def format_authors(paper: dict) -> str:
    """Format authors for LaTeX CV."""
    if paper.get("solo"):
        return "single-authored"
    
    authors = paper.get("authors", [])
    if not authors:
        return ""
    
    formatted = []
    for author in authors:
        name = escape_latex(author["name"])
        url = author.get("url", "")
        if url:
            formatted.append(f"\\href{{{url}}}{{{name}}}")
        else:
            formatted.append(name)
    
    if len(formatted) == 1:
        return f"joint w/ {formatted[0]}"
    elif len(formatted) == 2:
        return f"joint w/ {formatted[0]} and {formatted[1]}"
    else:
        return f"joint w/ {', '.join(formatted[:-1])}, and {formatted[-1]}"


def format_abstract(abstract: str) -> str:
    """Format abstract for LaTeX, wrapping text properly."""
    if not abstract:
        return ""
    # Clean up whitespace and escape
    text = " ".join(abstract.split())
    return escape_latex(text)


def generate_latex() -> str:
    """Generate LaTeX content from YAML."""
    with open(YAML_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    
    lines = [
        "% Auto-generated from _data/papers.yml",
        "% Do not edit directly - run generate_latex_papers.py instead",
        "",
    ]
    
    # Working Papers
    if data.get("working_papers"):
        lines.append(r"\section{Working Papers}")
        lines.append(r"\resumeSubHeadingListStart")
        lines.append("")
        
        for paper in data["working_papers"]:
            title = escape_latex(paper["title"])
            authors = format_authors(paper)
            status = escape_latex(paper.get("status", ""))
            
            lines.append(f"  \\resumeSubheading{{{title}}}{{}}")
            lines.append(f"    {{{authors}}}{{{status}}}")
            
            # Add abstract
            if paper.get("abstract") and paper["abstract"].strip():
                abstract = format_abstract(paper["abstract"])
                lines.append(f"  \\justify {abstract}")
            lines.append("")
        
        lines.append(r"\resumeSubHeadingListEnd")
        lines.append("")
    
    # Work in Progress
    if data.get("work_in_progress"):
        lines.append(r"\section{Work in Progress}")
        lines.append(r"\resumeSubHeadingListStart")
        lines.append("")
        
        for paper in data["work_in_progress"]:
            title = escape_latex(paper["title"])
            authors = format_authors(paper)
            status = escape_latex(paper.get("status", ""))
            
            lines.append(f"  \\resumeSubheading{{{title}}}{{}}")
            lines.append(f"    {{{authors}}}{{{status}}}")
            
            # Add abstract
            if paper.get("abstract") and paper["abstract"].strip():
                abstract = format_abstract(paper["abstract"])
                lines.append(f"  \\justify {abstract}")
            lines.append("")
        
        lines.append(r"\resumeSubHeadingListEnd")
        lines.append("")
    
    return "\n".join(lines)


def main():
    latex_content = generate_latex()
    
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(latex_content)
    
    print(f"Generated: {OUTPUT_PATH.resolve()}")
    print(f"Include in your CV with: \\input{{papers_generated.tex}}")


if __name__ == "__main__":
    main()
