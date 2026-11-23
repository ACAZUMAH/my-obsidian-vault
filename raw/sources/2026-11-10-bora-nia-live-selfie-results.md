# Bora KYC: live NIA selfie results for a match and a non-match

Date: 2026-11-10
Source: terminal output the user pasted from two runs of the gitignored `scripts/nia_staging/testNiaSelfie.ts` in `bora-capital-backend`, against the NIA environment in the user's local `.env`, with the user's own Ghana Card (PIN not recorded here), plus the user's reaction (paraphrased).

Run 1, a photo of someone else: NIA answered HTTP 200 in about 1.6 s. Top-level fields `data`, `success`, `code`, `msg`; `data` fields `transactionGuid`, `shortGuid`, `requestTimestamp`, `responseTimestamp`, `verified`, `center`, `merchantName`, `merchantCode`, `source`, `person`. Code `01`, msg "Not Matched Found", `success` true, `verified` "FALSE". The backend's answer: 400 "Your selfie did not match your Ghana Card. Retake it facing the camera in good light, then try again."

Run 2, the user's own selfie: HTTP 200 in about 1.4 s, same fields. Code `00`, msg "Verified Successfully", `success` true, `verified` "TRUE". The backend's answer: a match, so the KYC goes on to BCL.

Both PNGs were about 0.9 MB after conversion. Neither reply carried `onWatchList`, `nationalId` or `userID`, which the 2026-11-09 staging code-11 reply (HTTP 400) did. `success` is true for a non-match, so it reports that NIA processed the request, not that the face matched; only `code` and `verified` decide.

User's reaction: this is the outcome wanted, verified or not verified.

Follow-up the agent made the same day: a unit test pinning the live not-matched reply (HTTP 200, `success` true, code `01`, `verified` "FALSE") as not verified with nothing logged. NIA's code `11` was not reproduced by either run, so its meaning is still unknown.
