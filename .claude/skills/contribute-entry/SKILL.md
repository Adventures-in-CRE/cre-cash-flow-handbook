---
name: contribute-entry
description: Author, edit, retire, or stub an entry in the CRE Cash Flow Handbook. Use whenever someone wants to add a line item, write or fix a rule, correct a method, file a stub, or change anything under entries/. Triggers on "add an entry", "contribute to the handbook", "write the entry for NOI", "the handbook is wrong about X", "propose a change", "fix this rule", or any request to create or modify handbook content.
---

# Contributing an entry

Read [FRAMEWORK.md](../../../FRAMEWORK.md) before you write anything. It is
short and it is the entire ruleset. Do not proceed from memory of it.

## 1. Classify the request

Four kinds of contribution, and picking the wrong one is the most common
mistake:

| The request | What it actually is |
|---|---|
| A row that appears in models | A new entry |
| A nuance, edge case, or exception | A rule inside an existing entry |
| A property-type or deal-type difference | A variant rule on the base entry |
| A concept already covered under another name | An edit to that entry |

Most requests that sound like new entries are rules inside existing ones. Check
before you create a file.

## 2. Apply the admission test

A line item earns its own entry only if it would appear as its own row in a
model someone actually builds.

Fails the test: "reassessment risk on sale", "how to treat a partial year",
"what if the seller pays transfer tax". These are rules inside an entry.

Passes: "Net Operating Income", "Exit Cap Rate", "GP Catch-Up". Each is a row
or a named figure someone computes.

If it fails, tell the contributor which existing entry it belongs in, and edit
that entry instead.

## 3. Check for a duplicate

Search `INDEX.md` and `entries/` for the concept under every name it might
carry. Effective Gross Income is also Effective Gross Revenue. Free and Clear
Return is also unlevered cash on cash.

A concept lives in exactly one entry. If it already exists, this is an edit.

## 4. Assign the ID

IDs are `region.section.item` and permanent. Take the next unused number in the
section. Never renumber, reuse, or reorder existing IDs.

The filename is `<id>-<slugified-name>.md` and the validator enforces the
match.

## 5. Write it

Copy `entries/TEMPLATE.md`. Five body parts in order: Purpose, Inputs, Output,
Method, Rules.

**Purpose through Rules totals 250 words or fewer.** This is a hard ceiling,
enforced by CI. When you are over, cut content. Never cut the schema, never
compress two ideas into one sentence to save words, and never bury a real
distinction in a subordinate clause to make it fit. If the material genuinely
does not fit, that is evidence you are trying to write two entries.

**Purpose through Method is for a person.** Plain sentences. Vocabulary a
practitioner would say out loud. Readable without the rest of the handbook
open. No em dashes, no "plays a key role", no three-item lists assembled for
rhythm, no sentence that exists to sound comprehensive.

**Rules are for software.** Numbered. Each states one thing: the formula, the
sign convention, the timing, what is excluded and where it lives instead, and
any variant behavior. A developer implements them without asking a question.

## 6. Close the graph

This is the step contributors forget and CI catches.

Declare `draws_from` and `feeds`. Then **open every entry you named and add the
reciprocal reference.** If your entry feeds 1.2.9, then 1.2.9 lists yours in
`draws_from`. An asymmetric graph fails validation.

## 7. Handle variants correctly

A line item can vary by property type, deal type, leverage, or period type.
Variants never get their own entry. Name the dimension in `varies_on` and carry
the difference as a rule on the base entry.

Creating `1.2.9-net-operating-income-hotel.md` is wrong. Adding a rule to
1.2.9 that says what changes for hotels is right.

## 8. Evidence, only if ratifying

Stubs and drafts need no evidence. To request `ratified`, include either a
worked example below the rules (inputs in, expected output out) or a specific
citation in the `evidence` field. Do not invent either one. If you cannot
support the rule, request `draft` and say so.

## 9. Validate

```bash
python tools/validate.py
```

Fix everything it reports. Do not open a pull request that fails it.

## 10. Commit and open the pull request

```bash
git checkout -b entry/1.2.9-net-operating-income
git commit -s -m "Add 1.2.9 net operating income"
```

The `-s` is required. It adds the Developer Certificate of Origin sign-off, and
CI rejects commits without it.

One entry per pull request. Fill in the template, state the status you are
requesting, and say what you changed and why.

## How this goes wrong

The first version of this handbook was abandoned after it grew unreadable. The
failure modes were all local decisions that looked reasonable:

- Writing 5,000 words on a topic that needed 200.
- Creating an entry for every nuance instead of a rule inside an entry.
- Forking entries per property type until the count exploded.
- Ordering material by software architecture rather than by how a model is
  built.
- Writing for an imagined standards body rather than for a practitioner.

When in doubt, write less and ask the maintainers.
