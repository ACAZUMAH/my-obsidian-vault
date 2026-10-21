# Keks Step Validation Correction

Date: 2026-09-16. Source: direct user correction in Codex.

The user rejected submit-time validateForm/setTouched logic that chose an invalid field and jumped backward to its step.

> I don't like just don't allow them to next to the next step if the form is not valid look at the other parts I use onblur and error on the inputs, don't fucking be doing different things

Durable requirement: follow the existing input onBlur and touched/error convention. Disable Next until the current step is valid. Do not introduce a separate submit-time bulk-touch-and-step-jump interaction.
