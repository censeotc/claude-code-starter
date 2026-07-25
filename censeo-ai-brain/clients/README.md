# Client deployments

One directory per client, copied from [_template/](_template/), driven by [sops/client-onboarding.md](../sops/client-onboarding.md).

```
clients/
├── _template/config.yml    ← committed; the only thing in here that is
└── <client-code>/          ← GITIGNORED — real client configs contain their
    ├── config.yml             pricing, contacts, and consent basis. They live
    └── notes.md               on the VPS / in CenseoAI's private records, not
                                in this repo while it doubles as course material.
```

If/when censeo-ai-brain moves to its own private repo (decision-log #5), flip the gitignore and version real client configs there — config history per client is worth having.
