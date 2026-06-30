# CLAUDE.md — kiro-xfce

## Project overview

See [README.md](./README.md) for the user-facing description of this repo.

## Current state

Standard EDU scaffold (`setup.sh`, `up.sh`, optional `cleanup.sh`) plus the five required markdown files. Content lives where the repo actually ships files (typically `etc/skel/` or `usr/share/`).

## Patterns & decisions

- Bash scripts follow the canonical template from Kiro-HQ — see [Kiro-HQ/CLAUDE.md](/home/erik/Insync/Kiro/Kiro-HQ/CLAUDE.md) and the canonical [up.sh](/home/erik/Insync/Kiro/Kiro-HQ/up.sh) / [setup.sh](/home/erik/Insync/Kiro/Kiro-HQ/setup.sh) / [cleanup.sh](/home/erik/Insync/Kiro/Kiro-HQ/cleanup.sh).
- README + CHANGELOG + IDEAS + TODO are the four other required scaffold files per the ecosystem MD-scaffold rule.

## Keybinding overrides — DO NOT revert on a VM-sync pass

Some entries in `etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml`
are **deliberate overrides** that differ from whatever is currently live in the Kiro VM. When a
future pass fetches the live VM bindings and ports them back, it must **preserve** these — do not
let the VM value win:

- **`Print` → `xfce4-screenshooter -f`** — keep this. It was changed to a `scrot … → Pictures`
  command in the 2026-06-29 VM-sync pass and reverted on 2026-06-30. The canonical screenshot key
  is `xfce4-screenshooter -f`; do not flip it back to `scrot`.

When in doubt about a binding that a sync wants to change, check this list and the CHANGELOG
before overwriting.

## Next steps

See [TODO.md](./TODO.md) for active work.
