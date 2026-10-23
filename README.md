# Supporting materials: LLM and Agent Security in Energy Systems

Supporting materials prepared for this repository. Updated 23 October 2026.

Repository: https://github.com/habibullahmanzoor/LLM-and-Agent-Security-in-Energy-Systems
The manuscript PDF and editable LaTeX source are intentionally excluded.

## Contents

- `data/`: comparison records for 23 studies, eight related-review comparisons, 17 numerical
  claim checks, the 143-record exploratory census, search details and coding definitions.
- `data/classification_disagreements.csv`: 13 unresolved differences between historical codes
  and the later AI source pass.
- `data/index.html`: searchable study index; download and open it locally.
- `data/metric_dictionary.csv` and `data/evaluation_worksheet.md`: proposed evaluation aids.
- `figures/`: the five figures in vector PDF and PNG formats.
- `scripts/`: Python code to regenerate the figures, including shared colors and typography.
- `CITATION.cff`: citation information for these supporting materials.
- `manifest.json`: file checksums.

## Interpretation

The 23-study comparison and the exploratory census are separate collections. Census counts
are not estimates of field prevalence. Source checks and synthesis are AI-assisted and have
not been independently confirmed by human reviewers or experimentally replicated. Coding
disagreements and source-access limits are retained. The worked evaluation example uses
invented arithmetic, not observations. Cite original studies for their findings.

## Regenerate figures

Use Python 3.10 or later. From the repository root:

```text
python -m pip install -r requirements.txt
python scripts/build_publication_figures.py
```

The script regenerates the five paper figures and optional visual assets from the recorded
counts. It does not require the manuscript or downloaded research PDFs. Segoe UI is used when available, with Arial, Liberation Sans and DejaVu Sans as fallbacks. Supplied figure PDFs have embedded
fonts. Historical search collectors are not included; search-return order cannot be reconstructed.

## Release and reuse

The repository retains the owner-selected [MIT license](LICENSE). Original cited publications
retain their respective rights. No DOI has been assigned. After publication, add the article DOI or journal
link here and in the citation metadata. The manuscript remains separate from this repository.
Third-party research PDFs, credentials, local paths, temporary files and internal drafts are excluded.
