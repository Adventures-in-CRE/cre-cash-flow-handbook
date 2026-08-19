# Handbook Framework

This document governs how the handbook is built. It contains no cash flow
content of its own. Line items are contributed over time; this fixes the shape
every contribution takes so the whole stays coherent as it grows.

## Three levels

**Region.** A level of the cash flow hierarchy. Closed set of three: property,
investment, partnership. Adding a region means amending this document.

**Section.** A block within a region that produces a named subtotal, or a group
of related metrics. Added rarely, by agreement.

**Line item.** One row in a model, or one metric. This is the unit of
contribution and the only level that grows freely.

**Admission test.** A line item earns its own entry if it would appear as its
own row in a model someone actually builds. If it would not, it belongs inside
another entry as a rule, not as an entry of its own. This test is what keeps
the handbook from swallowing every nuance anyone raises.

## Entry schema

One line item, one file, one frontmatter block, five body parts.

```yaml
---
id: "1.2.9"
name: Net Operating Income
section: "1.2"
status: stub
varies_on: [property-type]
draws_from: ["1.2.7", "1.2.8"]
feeds: ["1.2.12", "1.3.1"]
evidence: ""
---
```

Body, in this order, 250 words total:

- **Purpose** - what the line item is for
- **Inputs** - what it consumes
- **Output** - what it emits, and in what shape
- **Method** - how to produce it
- **Rules** - numbered, binding, implementable without judgment

A worked example may follow the rules. It does not count against the ceiling.

## The variant rule

A line item can vary along four dimensions:

| Dimension | Values |
|---|---|
| `property-type` | the twelve supported types |
| `deal-type` | acquisition, development, value-add |
| `leverage` | unlevered, levered |
| `period-type` | day, week, month, quarter, year |

Variants never fork an entry. The base entry is canonical. Where a dimension
changes its behavior, the entry names that dimension in `varies_on` and carries
the difference as a rule. An entry silent on a dimension behaves identically
across every value of it.

This rule is what keeps the handbook finite. Without it, a hundred line items
become thousands, which is how the first attempt failed.

## The dependency graph

`draws_from` and `feeds` must agree in both directions. If A declares it feeds
B, B declares it draws from A. The resulting graph is the model's calculation
order, and it is also the handbook's own consistency check: a contribution that
breaks the graph is rejected before anyone reads its prose.

## Identity

IDs are `region.section.item` and are permanent. An ID is never reused,
renumbered, or reordered. A deprecated entry keeps its ID and points at its
replacement.

Names are the terms of art practitioners already use. Where the industry uses
two names for one thing, the entry picks one and records the other.

## Status ladder

```
stub -> draft -> reviewed -> ratified
```

Only `ratified` entries bind a conforming implementation. Everything below is
visible and citable but not authoritative. A stub is a reserved ID and a name
and nothing else, and filing one is a legitimate contribution: it marks
territory without claiming to have mapped it.

Reaching `ratified` requires evidence, either a worked example or a citation.
[GOVERNANCE.md](GOVERNANCE.md) defines that bar.

## One canonical home

A concept lives in exactly one entry. Where the same concept appears at several
points in a model, every other point cross-references it by ID rather than
restating it.

## Two audiences

Purpose through Method is written for a person. Brief, plain, readable on its
own without the rest of the document in front of you.

Rules are written for software. Numbered, unambiguous, and implementable
without interpretation. An implementation of this handbook is built against
them.
