"""Build the JMRT R1 marked-up + clean DOCX pair from the pandoc-styled revision.

Replaces the compare.py that lived (and died) in a session scratchpad. Recipe and the
two build traps are documented in submissions/JMRT-R1-resubmission/README.md; in short:

  1. cat front_JMRT.md manuscript.md | pandoc --citeproc --reference-doc=<as-submitted>
     -> revised_styled.docx  (front_JMRT.md must end in ***, never ---)
  2. this script: Word CompareDocuments(as-submitted, revised_styled) -> marked-up,
     then AcceptAll on the same document -> clean.

CompareDocuments is called with NAMED arguments through pywin32's dynamic dispatch,
which sidesteps the positional-signature trap noted in the README (this Word build has
no CompareMoves parameter, so a positional call miscounts).

    python build_docx_pair.py <revised_styled.docx>
"""
import os
import sys

import win32com.client

HERE = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(HERE, '..', 'as-submitted',
                    'Cai_Fe-SMA_JMRT_as-submitted-2026-07-15.docx')
MARKED = os.path.join(HERE, 'Cai_Fe-SMA_JMRT_R1_marked-up.docx')
CLEAN = os.path.join(HERE, 'Cai_Fe-SMA_JMRT_R1_clean.docx')

WD_COMPARE_DESTINATION_NEW = 2
WD_GRANULARITY_WORD = 1
WD_REVISION_INSERT = 1
WD_REVISION_DELETE = 2
WD_NO_PROTECTION = -1


def main(revised_path):
    revised_path = os.path.abspath(revised_path)
    for p in (ORIG, revised_path):
        if not os.path.isfile(p):
            raise SystemExit('missing: %s' % p)

    # dynamic dispatch: skips the gen_py typelib cache, which is corrupt on this
    # machine (CLSIDToClassMap AttributeError) and is not needed for named args
    word = win32com.client.dynamic.Dispatch('Word.Application')
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
            RevisedAuthor='R1 revision',
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
        total = cmp_doc.Revisions.Count
        print('tracked revisions: %d (%d insertions, %d deletions, %d other)'
              % (total, ins, dele, other))

        for target in (MARKED,):
            if os.path.exists(target):
                os.remove(target)
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
