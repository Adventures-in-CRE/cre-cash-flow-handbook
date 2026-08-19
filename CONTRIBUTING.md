# Contributing

Read [FRAMEWORK.md](FRAMEWORK.md) first. It is about 600 words and it is the
entire ruleset. Everything below is workflow.

## What you can contribute

**A stub.** A reserved ID and a name, nothing else. This is a real
contribution: it marks a line item that belongs in the handbook without
claiming to have specified it yet.

**A draft.** A stub filled in with purpose, inputs, output, method, and rules.

**A correction.** A change to an existing entry. Say what is wrong and why in
the pull request, not only what you changed.

**A retirement.** An argument that an entry should not exist, usually because
it fails the admission test or duplicates another entry.

## Before you write

Check that your line item would appear as its own row in a model someone
actually builds. If it would not, it belongs inside an existing entry as a
rule. This test rejects most proposals, and that is deliberate.

Then search [INDEX.md](INDEX.md) for the concept under any name it might carry.
A concept lives in exactly one entry, so if it is already there, your
contribution is an edit to that entry rather than a new one.

## Writing an entry

Copy [entries/TEMPLATE.md](entries/TEMPLATE.md). Fill in the frontmatter, then
the five body parts in order: Purpose, Inputs, Output, Method, Rules.

Purpose through Rules must total 250 words or fewer. CI enforces this and it is
not negotiable. The first version of this handbook failed because entries grew
without limit until nobody could read them.

Purpose through Method is written for a person. Plain sentences, no jargon you
would not say out loud, readable without the rest of the handbook in front of
you.

Rules are written for software. Numbered, unambiguous, implementable without
judgment.

A worked example, if you include one, goes below the rules and does not count
against the word ceiling.

## The dependency graph

Every entry declares what it draws from and what it feeds, and the two
directions have to agree. **Adding an entry usually means editing its
neighbors.** If your new entry feeds 1.2.9, then 1.2.9 must list yours in its
`draws_from`. CI rejects an asymmetric graph, so run the validator before you
push.

## Before you open a pull request

```bash
python tools/validate.py
```

It checks the schema, ID uniqueness, word count, allowed variant dimensions,
graph symmetry, and the evidence bar. Fix what it reports. A pull request that
fails the validator will not be reviewed.

## Sign your commits

Every commit needs a Developer Certificate of Origin sign-off, certifying that
you wrote the contribution and can license it under CC BY 4.0:

```bash
git commit -s -m "Add 1.2.9 net operating income"
```

The `-s` flag adds the `Signed-off-by` line. CI checks for it.

## Opening the pull request

One entry per pull request wherever you can manage it. Small pull requests get
reviewed. Large ones sit.

Fill in the template. State which status you are requesting, and if that status
is `ratified`, include the worked example or citation that supports it.

## What reviewers will ask

- Does it pass the admission test?
- Does the concept already live somewhere else?
- Can a practitioner read the human half without help?
- Can a developer implement the rules without asking you a question?
- Does the graph still close?
