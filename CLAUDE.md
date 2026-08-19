# Working in this repository

This is the CRE Cash Flow Handbook, an open technical standard for commercial
real estate cash flow modeling. Each entry specifies one line item: what it is
for, what it consumes, what it emits, how to produce it, and the numbered rules
software implements.

**Read [FRAMEWORK.md](FRAMEWORK.md) before you write anything.** It is about 600
words and it is the whole ruleset. Do not work from a summary of it.

## Where things are

```
FRAMEWORK.md      the ruleset: levels, schema, variants, graph, status ladder
GOVERNANCE.md     who decides, and what makes a rule correct enough to ratify
CONTRIBUTING.md   the workflow
INDEX.md          generated, do not edit by hand
entries/          one file per line item
tools/            validator and index builder
```

Two skills in `.claude/skills/` carry the detail. Use `contribute-entry` to
write or change an entry. Use `review-contribution` to review someone else's.

## Commands

```bash
pip install -r tools/requirements.txt
python tools/validate.py        # run before every commit
python tools/build_index.py     # after adding or renaming an entry
```

## The five rules people break

1. **250 words**, Purpose through Rules. CI fails the build above it. When you
   are over, cut content. Do not compress two ideas into one sentence to fit.

2. **The graph is bidirectional.** If your entry declares `feeds: ["1.2.9"]`,
   then 1.2.9 must declare your ID in `draws_from`. Adding an entry means
   editing its neighbors. This is the most common CI failure.

3. **Variants never fork an entry.** Property type, deal type, leverage, and
   period type are handled as rules on the base entry, named in `varies_on`.
   Creating a per-property-type file is wrong.

4. **IDs are permanent.** Never renumber, reuse, or reorder.

5. **A concept lives in exactly one entry.** If it already exists under another
   name, your contribution is an edit to that entry.

## The admission test

A line item earns its own entry only if it would appear as its own row in a
model someone actually builds. Nuances, exceptions, and edge cases are rules
inside an existing entry. Most proposals fail this test, and rejecting them is
what keeps the handbook readable.

## House voice

Purpose through Method is for a practitioner reading it cold. Plain sentences,
no em dashes, no filler that exists to sound thorough.

Rules are for a developer with no CRE background. A rule containing "typically"
or "as appropriate" has not been written yet.

## What not to do

Do not draft content the maintainers have not asked for. Do not invent a worked
example or a citation to clear the evidence bar. Do not advance an entry's
status past what was requested. When you are unsure whether something is an
entry or a rule, ask rather than guessing.
