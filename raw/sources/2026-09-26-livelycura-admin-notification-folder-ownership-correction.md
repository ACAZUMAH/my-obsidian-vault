# LivelyCura Admin Notification Folder Ownership Correction

Date: 2026-09-26
Source: Direct user correction during LivelyCura Admin Portal implementation

## Correction

Admin notification files belong directly under `src/notifications`. Do not introduce an additional `inbox` folder between the notification domain and its components, hooks, helpers, or interfaces.

The intended structure keeps the drawer and content at the notification feature root and places supporting files in `src/notifications/components`, `src/notifications/hooks`, `src/notifications/helpers`, and `src/notifications/interfaces`.

When rearranging the feature, move every operation hook and update every import together. A partial move that deletes hooks or leaves imports pointing to `src/notifications/inbox` breaks Vite module loading.
