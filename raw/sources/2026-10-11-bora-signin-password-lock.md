# Bora sign-in password lock

Date: 2026-10-11
Source: direct user request in the rate-limiting review, with repository inspection.

After the client-IP fix, the user asked why limits should also key on the customer. Repository inspection showed OTP sends already have a per-user escalating cooldown (`reserveAuthRequest`) and each OTP allows 5 attempts (`MAX_CODE_ATTEMPTS`). Wrong passwords at `signin` were rejected before any per-user counter, so only the per-IP shield limit (3 per minute) applied, and an attacker rotating IPs could guess passwords for one phone number without limit. Three gaps were presented in priority order: refreshToken keyed per IP, the sign-in password gap, and the escalating per-IP signup cooldown. An earlier suggestion to key signup on email was withdrawn, because attackers use new emails.

The user chose to start with the sign-in password gap. LivelyCura has no password lockout (its login is passwordless), so there was no reference to mirror.

Implemented policy: 5 password attempts per phone number per 15-minute window, then 429 until the window ends. Each attempt is spent before the password check, so concurrent guesses cannot exceed the limit. Unknown numbers are counted the same way so a lock does not reveal registration. Counters are stored by phone-number hash in `signinAttempts`. A correct password, a code-based password reset, or an authenticated password change clears the counter, so the owner can escape a lock someone else caused. Biometric login is unaffected.
