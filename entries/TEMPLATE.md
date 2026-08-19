---
id: "0.0.0"
name: Line Item Name
section: "0.0"
status: stub
varies_on: []
draws_from: []
feeds: []
evidence: ""
---

## Purpose

What this line item is for, in two or three sentences. Written for a
practitioner who has not read the rest of the handbook.

## Inputs

What it consumes. Name the other entries by ID where it draws from them.

## Output

What it emits, and in what shape: a single figure, a periodic stream, a rate.

## Method

How to produce it. Plain sentences. The steps someone would follow at a
spreadsheet.

## Rules

1. State the formula.
2. State the sign convention and the timing.
3. State what is excluded, and where those things live instead.
4. State any variant behavior for a dimension named in `varies_on`.

## Worked example

Optional below `ratified`, required at `ratified` unless a citation is given
instead. Inputs in, expected output out, precise enough that two
implementations can be checked against it. Does not count toward the 250-word
ceiling.
