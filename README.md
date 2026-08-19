# The CRE Cash Flow Handbook

An open technical standard for commercial real estate cash flow modeling.

A project of [Adventures in CRE](https://www.adventuresincre.com), which
publishes free financial models, training, and reference material for
commercial real estate professionals.

One entry per line item. Each entry says what the line item is for, what it
consumes, what it emits, and how to produce it, in terms a practitioner can
read. Each entry also carries numbered rules precise enough that software can
be built against them without interpretation.

**Status: v0, pre-release.** The structure is set. The content is being
written. Nothing here is ratified yet.

## Why

Every firm models cash flow a little differently, and the differences are
mostly undocumented. Two analysts underwrite the same asset, get different
answers, and cannot say exactly where they diverged. Software encodes one
shop's conventions and presents them as the method.

This handbook writes the conventions down, one line item at a time, so that
implementations can agree and disagreements can be specific.

## How it is organized

Three levels. **Regions** are the levels of the cash flow hierarchy: property,
investment, partnership. **Sections** are the blocks within a region. **Line
items** are the individual rows and metrics, and they are the unit everyone
contributes.

```
entries/1-property/1.2-operating-cash-flow/1.2.9-net-operating-income.md
        |          |                       |
        region     section                 line item
```

[1.2.9 Net Operating Income](entries/1-property/1.2-operating-cash-flow/1.2.9-net-operating-income.md)
is a worked example of the schema. [INDEX.md](INDEX.md) lists everything else.

Read [FRAMEWORK.md](FRAMEWORK.md) before contributing. It is short, and it is
the whole ruleset.

## Contributing

Anyone can propose an entry, correct a rule, or file a stub. Most of the
handbook is currently stubs, which are reserved IDs waiting for someone to
write them. Claiming one is a good first contribution.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the workflow and
[GOVERNANCE.md](GOVERNANCE.md) for how decisions get made.

If you work with an AI assistant, open this repository with it. `CLAUDE.md` and
the skills in `.claude/skills/` teach it the framework, the entry schema, and
the validation rules before it writes anything.

```bash
pip install -r tools/requirements.txt
python tools/validate.py
```

## License

[CC BY 4.0](LICENSE). Use it, implement it, build products on it. Attribution
required.
