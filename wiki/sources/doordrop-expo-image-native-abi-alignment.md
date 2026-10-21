---
type: source
status: active
created: 2026-09-14
updated: 2026-09-14
tags: [livelycura, doordrop, expo, ios, expo-image, native-abi]
sources:
  - ../../raw/sources/2026-09-14-doordrop-expo-image-native-abi-crash.md
confidence: high
---

# doorDrop Expo Image Native ABI Alignment

## Source

- Raw file: [2026-09-14-doordrop-expo-image-native-abi-crash.md](../../raw/sources/2026-09-14-doordrop-expo-image-native-abi-crash.md)
- Date: 2026-09-14
- Author: user crash report and live Codex verification
- Ingested: 2026-09-14

## Core Claims

- The doorDrop iOS startup failure was a native Expo ABI mismatch: `ExpoImage.framework` referenced `BaseModule.willDestroy`, while the embedded older `ExpoModulesCore.framework` did not provide it.
- Native Expo packages must be aligned across the installed SDK patch line; matching only the SDK major version is insufficient for precompiled Expo frameworks.
- After aligning the SDK 57 native packages, regenerating iOS, reinstalling Pods, and rebuilding, doorDrop launched without the original `dyld` failure.

## Useful Details

- The failure was independent of JavaScript execution and the doorDrop rename.
- A clean prebuild matters because a successful package update alone does not remove stale embedded frameworks from an existing native project or Derived Data product.
- A local backend connection refusal after launch is a runtime environment issue, not evidence that the native ABI fix failed.

## Connections

- [[../projects/livelycura-choproute-app|LivelyCura doorDrop App]]

## Contradictions Or Tensions

- Expo's dependency check initially reported the older graph as current while operating from its local/offline compatibility map. The crash report and installed Swift API surface were stronger evidence; after updating Expo, the refreshed compatibility map identified and aligned the remaining outdated native packages.

## Open Questions

- None for this incident. Repeat native launch verification whenever Expo packages containing precompiled frameworks move between patch versions.
