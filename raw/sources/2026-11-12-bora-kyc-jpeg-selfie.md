# Bora KYC: the NIA selfie can be a JPEG

Date: 2026-11-12
Source: direct user request in a `bora-capital-backend` session, relaying the frontend developer, plus NIA's Selfie Verification API document the user supplied on 2026-11-09 and the code changed and verified in that session (paraphrased).

Request: the frontend developer reported that the backend only allows PNG selfies; the user said NIA allows JPG too and asked to allow JPG before the next redeploy.

Evidence check: NIA's document shows only `"dataType": "PNG"` in its request samples and lists "Image format : PNG" in its image notes (size under 1 MB, at least 640 × 480). It documents no JPEG `dataType` value. The user's statement that NIA takes JPG was not verified against live NIA at recording.

Implemented: `getKycSelfieCheck` strips a `data:image/png|jpeg|jpg;base64,` prefix (any case), reads the format from how the base64 starts (`iVBORw0KGgo` PNG, `/9j/` JPEG), not from the data URL label, and returns NIA's `dataType` with the image: `PNG` or `JPG`. `verifyNiaSelfie` sends that `dataType` instead of a fixed `PNG`. Anything else is a 400 "The selfie must be a PNG or JPEG image." (the app's selfie-retake rule still matches it through "PNG"). The 1 MB limit is unchanged. BCL still receives the photo exactly as the app sent it. The gitignored `scripts/nia_staging/testNiaSelfie.ts` gained `--format jpg` and a `--data-type` override, so the user can check a JPEG against live NIA, and try another value such as `JPEG`, before redeploying.

App: `docs/frontend-handoff-2026-11-12.md` tells the frontend developer the backend now accepts JPEG and where the app still forces PNG (capture format, selfie check, PNG-header dimension check, hint). Backend first: PNG keeps working, and the current backend refuses JPEG.

Verification: `tsc` clean, `yarn build`, full Jest 193 suites and 1617 tests under Node 26.12.1; the script was dry-run against a local fake NIA with `.env` not loaded. Uncommitted at recording; no live NIA call.
