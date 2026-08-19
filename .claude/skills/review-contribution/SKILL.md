---
name: review-contribution
description: Review a proposed change to the CRE Cash Flow Handbook as a maintainer. Use when reviewing a pull request, evaluating a proposed entry or rule, deciding whether to merge, or judging whether an entry is ready to advance its status. Triggers on "review this PR", "should we merge this", "review the proposed entry", "is this ready to ratify", or any maintainer-side assessment of a handbook contribution.
---

# Reviewing a contribution

Merging to `main` is approval. Review accordingly.

Read [FRAMEWORK.md](../../../FRAMEWORK.md) and
[GOVERNANCE.md](../../../GOVERNANCE.md) first.

## 1. Run the validator before reading anything

```bash
python tools/validate.py
```

If it fails, stop. Report what failed and request changes. Do not review prose
in a contribution that does not pass the mechanical gate, and do not fix it
yourself: the contributor learns the schema by fixing it.

## 2. Admission test

Would this line item appear as its own row in a model someone actually builds?

If not, it is a rule inside an existing entry. Say which entry, and decline the
new file. This is the most common reason to reject, and letting one through
sets the precedent that sinks the handbook.

## 3. Canonical home

Does this concept already live somewhere, possibly under a different name?
Search for synonyms, not just the submitted title.

If it exists, the contribution is an edit to that entry. Two entries describing
one concept is the defect that governance exists to prevent.

## 4. Read the human half aloud

Purpose through Method should survive being read out loud to a practitioner who
has never opened this repository.

Reject: writing that announces its own importance, sentences padded to sound
thorough, jargon standing in for explanation, and anything a reader would have
to parse twice.

Ask directly: could someone build this line item in a spreadsheet from the
Method alone? If not, the entry has described the concept without teaching the
procedure.

## 5. Test the rules for implementability

Read the Rules as a developer with no CRE background. Every point where you
would have to ask the author a question is a defect.

Check that the rules state:

- the formula
- the sign convention and the timing
- what is excluded, and which entry holds it instead
- what changes for each dimension named in `varies_on`

A rule that says "as appropriate", "typically", or "depending on the deal" has
not been written yet.

## 6. Check the variant handling

Variants belong on the base entry as rules. If the contribution creates a
separate file per property type, per deal type, or per leverage case, request
changes. That pattern is what made the first version unmaintainable.

## 7. Check the graph

The validator confirms symmetry. You confirm correctness: are these actually
the right dependencies? An entry that declares no `draws_from` and no `feeds`
is usually wrong, because almost every line item in a model consumes something
and feeds something.

## 8. Judge the requested status

| Requested | What you are confirming |
|---|---|
| `stub` | The ID and name are right and the concept belongs |
| `draft` | It is complete and coherent, and may still be wrong |
| `reviewed` | You have checked it against practice and believe it correct |
| `ratified` | Evidence is present and sufficient, and an implementation can be built against it |

Do not advance status further than the contributor requested. Do not ratify
your own entry.

For `ratified`, verify the evidence rather than accepting it. A worked example
must actually produce the stated output under the stated rules. Recompute it. A
citation must be specific enough to look up, and must say what the entry claims
it says.

## 9. When you think practice differs

Before rejecting a rule as wrong, consider whether it is a legitimate
convention you have not used. Commercial real estate practice varies by region,
sector, and shop.

Where it is a genuine convention, the entry states the dominant one as its rule
and records the alternative as a named variant. Where it is a real
disagreement, hold the entry at `reviewed` with both positions recorded, and
escalate to the steward if it blocks.

Do not resolve a methodology dispute by preferring the version you were trained
on. Ask for a worked example.

## 10. Deliver the verdict

State one of: approve, request changes, or decline.

For request-changes, list each item as a specific, actionable edit with the
file and line. For decline, give the reason in one paragraph and name the
alternative path, which is usually a rule inside an existing entry.

Thank contributors for stubs and corrections as readily as for full drafts. A
correct stub is more useful to this project than a confident wrong draft.
