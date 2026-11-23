# Bora KYC: live NIA matches a JPEG selfie sent as dataType JPG

Date: 2026-11-12
Source: terminal output the user pasted from one run of the gitignored `scripts/nia_staging/testNiaSelfie.ts --format jpg` in `bora-capital-backend`, against the NIA environment in the user's local `.env`, with the user's own Ghana Card and selfie (PIN not recorded here), plus the exchange before it (paraphrased).

Run: the user's own selfie, converted by `sips` to a JPEG and sent with `dataType` `JPG`. NIA answered HTTP 200 in about 1.6 s with the same fields as the 2026-11-10 PNG runs (`data`, `success`, `code`, `msg`; `data` with `transactionGuid`, `shortGuid`, timestamps, `verified`, `center`, `merchantName`, `merchantCode`, `source`, `person`). Code `00`, msg "Verified Successfully", `success` true, `verified` "TRUE". The backend's answer: a match, so the KYC goes on to BCL.

The JPEG was 129,425 bytes; the same selfie as a PNG on 2026-11-10 was 915,322 bytes, close to NIA's 1 MB limit.

Earlier misreading: the user first took the 2026-11-10 run with `--image some.jpg` as proof that NIA accepts JPEG. That version of the script always converted the photo to PNG with `sips` and sent `dataType` `PNG`, so it was not; the `.jpg` filename made it look otherwise. The agent acknowledged the script's silent conversion caused the confusion. This run with `--format jpg` is the first JPEG NIA received.
