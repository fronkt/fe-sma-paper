"""Build the JMRT R2 marked-up + clean DOCX pair.

Same recipe as revision/JMRT-R1/R1-manuscript/build_docx_pair.py, with one difference that
matters: the ORIGINAL for the comparison is the **Revision-1 clean file** the reviewers
read, not the July submission, so the tracked changes show only what changed in Round 2.

  1. From the repo root (pandoc concatenates; never pre-concatenate with PowerShell):
       pandoc front_JMRT.md manuscript.md --citeproc --bibliography=references.bib \
         --csl=elsevier-with-titles.csl \
         --reference-doc=revision/JMRT-R1/as-submitted/Cai_Fe-SMA_JMRT_as-submitted-2026-07-15.docx \
         -o revised_styled.docx
     (front_JMRT.md must end in ***, never ---)
  2. python revision/JMRT-R2/R2-manuscript/build_docx_pair.py revised_styled.docx
     -> Cai_Fe-SMA_JMRT_R2_marked-up.docx, Cai_Fe-SMA_JMRT_R2_clean.docx  (here)

Word must be closed: plain Dispatch attaches to a running instance, and the script refuses
to run inside one (see the R1 script for the 2026-08-18 incident).
"""
import os
import sys

import pythoncom
import win32com.client

HERE = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(HERE, '..', '..', 'JMRT-R1', 'R1-manuscript',
                    'Cai_Fe-SMA_JMRT_R1_clean.docx')
MARKED = os.path.join(HERE, 'Cai_Fe-SMA_JMRT_R2_marked-up.docx')
CLEAN = os.path.join(HERE, 'Cai_Fe-SMA_JMRT_R2_clean.docx')

WD_COMPARE_DESTINATION_NEW = 2
WD_GRANULARITY_WORD = 1
WD_REVISION_INSERT = 1
WD_REVISION_DELETE = 2


def main(revised_path):
    revised_path = os.path.abspath(revised_path)
    for p in (ORIG, revised_path):
        if not os.path.isfile(p):
            raise SystemExit('missing: %s' % p)

    word = win32com.client.dynamic.Dispatch('Word.Application')
    if word.Documents.Count:
        raise SystemExit('refusing to run: attached to a Word instance with %d '
                         'document(s) open - close Word and rerun'
                         % word.Documents.Count)
    word.Visible = False
    word.DisplayAlerts = 0
    try:
        orig = word.Documents.Open(os.path.abspath(ORIG), ReadOnly=True)
        rev = word.Documents.Open(revised_path, ReadOnly=True)
        cmp_doc = word.CompareDocuments(
            OriginalDocument=orig,
            RevisedDocument=rev,
            Destination=WD_COMPARE_DESTINATION_NEW,
            Granularity=WD_GRANULARITY_WORD,
            CompareFormatting=True,
            CompareCaseChanges=True,
            CompareWhitespace=True,
            CompareTables=True,
            CompareHeaders=True,
            CompareFootnotes=True,
            CompareTextboxes=True,
            CompareFields=True,
            CompareComments=True,
            RevisedAuthor='R2 revision',
            IgnoreAllComparisonWarnings=True,
        )
        orig.Close(False)
        rev.Close(False)

        ins = dele = other = 0
        for r in cmp_doc.Revisions:
            if r.Type == WD_REVISION_INSERT:
                ins += 1
            elif r.Type == WD_REVISION_DELETE:
                dele += 1
            else:
                other += 1
        print('tracked revisions: %d (%d insertions, %d deletions, %d other)'
              % (cmp_doc.Revisions.Count, ins, dele, other))

        if os.path.exists(MARKED):
            os.remove(MARKED)
        cmp_doc.SaveAs2(os.path.abspath(MARKED))
        print('wrote', MARKED)

        cmp_doc.Revisions.AcceptAll()
        if os.path.exists(CLEAN):
            os.remove(CLEAN)
        cmp_doc.SaveAs2(os.path.abspath(CLEAN))
        print('wrote', CLEAN)
        cmp_doc.Close(False)
    finally:
        word.Quit()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    main(sys.argv[1])
