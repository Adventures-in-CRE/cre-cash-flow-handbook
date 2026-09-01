# Changelog

Versioned `MAJOR.MINOR.PATCH` per [GOVERNANCE.md](GOVERNANCE.md).

- **PATCH** corrections that do not change a computed result
- **MINOR** new entries and new rules
- **MAJOR** any change that would make a conforming implementation produce a
  different number than it did before

## Unreleased

### Added

- Framework, governance, contribution workflow, and entry schema.
- Entry validator covering schema, ID uniqueness, word ceiling, variant
  dimensions, graph symmetry, and the evidence bar.
- AI contributor skills under `.claude/skills/`.
- Section scaffolding for the three regions, with line items filed as stubs.

### Changed

- Sponsor fees moved from the investment level to the partnership level.
  Investment-level returns are gross returns and carry no sponsor economics.
  Partnership-level returns are net returns, after fees and promote. Acquisition,
  asset management, development, and disposition fees are now 3.15.1 through
  3.15.4 in a new section, 3.15 Sponsor Fees.
- Portfolio Debt moved to 2.6 Aggregation as 2.6.5, beside Net Investment Cash
  Flow Levered.

### Removed

- Section 2.7 Entity-Level Adjustments, along with Entity Operating Expenses.
  The handbook models the property, investment, and partnership levels only. The
  cost of running a sponsor's business is out of scope, because carrying it into
  a forecast misstates the return the partners receive. Section number 2.7 is
  retired and will not be reused.

Nothing is ratified. No implementation should treat this release as binding.
