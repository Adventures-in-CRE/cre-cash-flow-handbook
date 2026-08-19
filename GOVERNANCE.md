# Governance

## Roles

**Contributors** propose entries, corrections, and retirements through pull
requests. Anyone can be a contributor. No permission is needed to open one.

**Maintainers** review pull requests and merge to `main`. Merging to `main` is
what approval means here. Maintainers are listed in
[.github/CODEOWNERS](.github/CODEOWNERS).

**The steward** breaks ties and admits new maintainers. Today this is the
project founder. The role exists because a methodology standard without a
tiebreaker stalls on taste.

## How a change is approved

A pull request needs one maintainer approval to merge, from a maintainer who is
not its author. Changes to `FRAMEWORK.md`, `GOVERNANCE.md`, or the license need
two approvals, one of them the steward, because those govern everything else.

## The evidence bar

A coding project settles arguments with tests. This one has no compiler, so it
has to name its own standard of proof.

To reach `ratified`, an entry carries one of the following:

**A worked example.** A small numeric case: inputs in, expected output out,
stated precisely enough that two implementations can be checked against it.
This is the stronger form, because it turns a disagreement about method into a
disagreement about a number.

**A citation.** A named model, textbook, published institutional convention, or
regulatory source that the rule follows. Name it specifically enough that a
reader can go look it up.

Below `ratified`, no evidence is required. Stubs and drafts are meant to be
cheap.

## When practice genuinely differs

Commercial real estate practice is not uniform, and pretending otherwise would
make this handbook wrong in a more confident way. Where firms legitimately
differ, an entry states the dominant convention as its rule and records the
alternative as a named variant. It does not pick a winner by argument, and it
does not quietly average the two.

Where the difference is a real disagreement rather than a regional or sector
convention, the entry stays at `reviewed` and records both positions until
evidence settles it.

## Disputes

Argue in the pull request. If two maintainers disagree and neither is
persuaded, either may escalate to the steward, who decides and records the
reasoning in the entry itself so the question does not get relitigated every
time someone new arrives.

## Becoming a maintainer

Contribute entries that get merged. The steward invites maintainers based on
demonstrated judgment about this material rather than volume. Maintainers who
go a year without reviewing move to emeritus, and can come back by asking.

## Versioning

The handbook is versioned `MAJOR.MINOR.PATCH`.

- **PATCH** for corrections that do not change a computed result.
- **MINOR** for new entries and new rules.
- **MAJOR** for any change that would make a conforming implementation produce
  a different number than it did before.

Implementations state which version they conform to. See
[CHANGELOG.md](CHANGELOG.md).
