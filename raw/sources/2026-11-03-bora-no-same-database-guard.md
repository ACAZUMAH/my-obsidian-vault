# Bora production scripts carry no same-database guard

Date: 2026-11-03
Source: Direct user correction on `bora-capital-backend` (paraphrased; the user was angry).

## User correction

- The user removed the check in `scripts/paystack_production/helpers` that refused a `PROD_MONGODB_URI` equal to `MONGODB_URI`, along with what its test asserted. This happened before 2026-11-03.
- The user's reason: they set the environment values themselves, so the two can never be the same.
- The agent flagged the removal and asked whether to restore the check. The user had already given the same correction on 2026-10-31 in another session.

## Rule

- Production scripts do not add a same-database guard, do not test for one, and do not raise its absence.
- This corrects `2026-11-03-bora-cdh-balanced-paystack.md`, which says no reason was given for the removal.
