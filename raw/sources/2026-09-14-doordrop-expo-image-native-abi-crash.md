# doorDrop Expo Image Native ABI Crash

Date: 2026-09-14
Source: user-provided iOS Simulator crash report plus live repository diagnosis and rebuild verification

## User Report

Opening a newly built doorDrop app in the iOS Simulator terminated immediately.

The crash report identified a dynamic-loader failure:

- termination namespace: `DYLD`
- reason: missing symbol
- missing API: `ExpoModulesCore.BaseModule.willDestroy`
- requesting framework: `ExpoImage.framework`
- expected provider: the embedded `ExpoModulesCore.framework`

## Live Diagnosis

The installed native packages were on incompatible Expo SDK 57 patch levels:

- `expo-image` was `57.0.4`.
- `expo-modules-core` was `57.0.8`.
- The installed `BaseModule` source in `expo-modules-core 57.0.8` did not define `willDestroy`.
- A working SDK 57 comparison used a newer `expo-modules-core` whose `BaseModule` did define the symbol.

This established a native ABI mismatch rather than a JavaScript, bundle-identifier, or doorDrop rename failure.

## Remediation And Verification

- Updated Expo to the current compatible SDK 57 patch line and ran Expo's compatibility fix for the complete native dependency set.
- Regenerated the ignored iOS project from a clean prebuild and reinstalled CocoaPods.
- Rebuilt and installed doorDrop on the iPhone Simulator.
- The native build completed with zero errors.
- The app relaunched successfully under `com.livelycura.doordrop`.
- Recent simulator logs contained no `dyld`, missing-symbol, or termination event.
- TypeScript, Expo dependency validation, all-platform Expo export, and `git diff --check` passed.

The simulator separately logged a refused request to the local GraphQL server because the backend was not running; that network condition was unrelated to the native startup crash.
