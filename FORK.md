# Infinity Online Solutions maintained fork

This fork powers Infinity Astro's self-hosted engine.

- Origin: https://github.com/infinityonlinesolutions/PyJHora
- Upstream: https://github.com/naturalstupid/PyJHora
- Upstream baseline for the first fork fix: `67b4c861a88ce5d112b2d182b7708f3781cc3c4a`
- Preserve upstream attribution and the AGPL-3.0-or-later license.

## Maintenance policy

1. Keep fixes small, on topic branches, with regression tests.
2. Open pull requests against this fork's `main`; merge only after tests pass.
3. Fetch upstream periodically and review changes on an integration branch.
   Never force-reset the maintained branch to upstream or auto-sync over fixes.
4. Run fork regression tests and the Infinity Astro API endpoint suite before
   accepting upgrades. These focused tests are not the full upstream suite.
5. Pin the consuming engine Docker build and CI to the same full commit SHA
   published in this fork. Rebuild and smoke-test before deployment; do not
   consume a floating `main` for production.
6. Offer generally applicable fixes upstream, without depending on acceptance.
7. Make the corresponding source of deployed modifications available to users
   under the applicable AGPL obligations; retain LICENSE and notices.

## Local checkout

```bash
git clone https://github.com/infinityonlinesolutions/PyJHora.git
cd PyJHora
git remote add upstream https://github.com/naturalstupid/PyJHora.git
git fetch upstream
```

Create a topic branch before changes. To review a future upstream update:

```bash
git fetch upstream
git switch -c integrate/upstream-update origin/main
git merge upstream/main
```

Resolve conflicts explicitly, run tests, then submit an integration PR.
A shallow checkout may need `git fetch --unshallow origin` before merging history.

## Focused regression tests

With the engine's Python dependencies installed and Python 3.11:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Fork changes

### 2026-11-12: yoga 155 score contract

`vaiseshikamsa_dhasavarga_of_planets` returns each planet's entry as
`[count, chart_names, weighted_score]`. Yoga 155 now compares the first element
(the count) to its thresholds, rather than comparing the whole list to an int.
Threshold and prerequisite regressions are in `tests/test_yoga_155.py`.
