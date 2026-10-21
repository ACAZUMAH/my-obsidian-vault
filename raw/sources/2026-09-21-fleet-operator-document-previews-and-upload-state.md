# Fleet Operator Document Previews And Upload State

- Date: 2026-09-21
- Author: User
- Context: LivelyCura Pharmacy Portal Fleet operator forms

## Direct Correction

- Identity-document front/back files, license attachments, and other operator documents must show previews after upload.
- Uploading one file must not put every other upload button into a loading state.

## Durable Interpretation

Every Fleet operator upload control owns its own request state and preview. Images and PDFs render inline after selection; update forms resolve saved private documents through the existing temporary document-URL query.
