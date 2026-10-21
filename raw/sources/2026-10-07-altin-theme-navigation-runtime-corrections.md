# Altin Partner Theme, Navigation, and Runtime Corrections — 2026-10-07

Sanitized record of direct user corrections in Altin Partner Mobile Codex tasks (late September 2026, after the 2026-09-23 brand pass), read from the user-supplied shared Codex chats on 2026-10-07 and confirmed in a Claude Code session the same day. Credentials, tokens, and environment values that appeared in those chats are deliberately omitted.

## Theme

- The user rejected the brand-book theme pass in `src/theme/constants.ts` and directed the agent to use `docs/app-theme-guide.md` instead: brand palette, semantic colors, typography, spacing, and corner radii. The app's colors and look had to change, and the old look, colors, and design must not be brought back.
- The resulting pass replaced the custom Plus Jakarta Sans / IBM Plex fonts with system typography from the guide's scale. The user later tuned palette and KPI colors personally and instructed the agent not to change them.

## Icon wells

- Across the whole project, icons colored `theme.colors.primary` that sit inside an icon background must look the same in light and dark mode. The user rejected a dark-mode treatment of a `surfaceMuted` background with a white glyph, and separately rejected making the wells white in dark mode.
- The accepted fix keeps primary-red glyphs on a subtle red background in both modes, with a deep red background in dark mode.
- Notification buttons, back buttons, and other controls unrelated to the request had been changed and were ordered reverted to theme-aware neutral colors.

## Cards

- The user reduced Home card border widths to 0.3 and asked for the same on the rest of the screens. Card and skeleton surfaces adopted 0.3; input, selection, and navigation outlines kept their widths.

## Navigation

- The user intentionally changed the Notifications tab configuration to Reports. The agent first "fixed" the resulting crash by restoring Notifications, which the user rejected. Final state: Reports is a bottom tab (currently a placeholder); Notifications remains a separate screen opened from the Home header bell.

## Runtime

- OAuth works in the development build (`altinpartner://redirect`) but not Expo Go, whose `exp://` redirect is not registered in Keycloak. The agent advised against loosening Keycloak redirects.
- A stale Metro server left on port 8081 after agent verification caused `yarn ios` to reuse it, launch the app, and exit, so the user lost live reload in their terminal.

## Confirmation

- On 2026-10-07 the user approved recording these rules in the repository `AGENTS.md` (Reports tab, theme guide authority, icon wells, neutral controls, 0.3 card borders, Search rules, local runtime) and correcting `DESIGN.md`, `PRODUCT.md`, and the vault.
