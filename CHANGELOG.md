# Changelog

## 2026.06.01

### What Changed
- Added an XFCE command shortcut `super + ctrl + s` (`<Primary><Super>s`) that
  launches `kiro-keybindings`, the new searchable Qt6/PySide6 keybindings
  cheatsheet (a cross-desktop Kiro feature). `super + ctrl + s` is the universal
  cheatsheet hotkey now used across all Kiro desktops ("S" = Shortcuts;
  AZERTY-safe).

### Technical Details
- Registered as a custom command shortcut under the `<commands>/custom` node of
  the xfconf keyboard-shortcuts channel, mirroring the existing entries.
- XFCE is a full desktop, not a tiling WM, so it has no `keybindings.txt`
  reference file (that artifact is TWM-only) — only the xfconf XML changed.

### Files Modified
- `etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml`

## 2026.05.31

### What Changed
- Bound `Super+o` to the existing "Open Claude Here" Thunar custom action, so
  pressing Super+o in a focused Thunar window opens Claude Code in an Alacritty
  terminal at the folder being viewed. The custom action (`open-claude`,
  `alacritty --working-directory %f -e claude`) already shipped in `uca.xml`;
  only the keyboard shortcut was missing.

### Technical Details
- Thunar stores per-custom-action shortcuts in `accels.scm` keyed by
  `<Actions>/ThunarActions/uca-action-<unique-id>`. Added one line mirroring
  the existing `open-terminal → F4` binding.
- Chosen as a Thunar-internal shortcut (not a global sxhkd/WM bind) because the
  viewed-folder path is only available inside Thunar via `%f` — Thunar 4.20
  exposes only the folder basename in the window title, and the daemon's cwd
  doesn't track the viewed folder. Lives in edu-xfce (the sole owner of Thunar
  skel config) so it reaches every Thunar-using desktop, not just chadwm.

### Files Modified
- `etc/skel/.config/Thunar/accels.scm`

## 2026.05.25

### What Changed
- De-brand (user-visible): the xfce4-screenshooter saved config had
  `title=ArcoLinux`. Changed to `title=Kiro`. Part of the ecosystem-wide
  arcolinux de-brand sweep.

### Files Modified
- `etc/skel/.config/xfce4/xfce4-screenshooter`

## 2026.05.21

### What Changed
- Initial markdown scaffold added per the ecosystem MD-scaffold rule ([HQ/CLAUDE.md](/home/erik/Insync/Kiro/Kiro-HQ/CLAUDE.md#required-markdown-scaffold-every-repo)).
- Stubs created for `CHANGELOG.md`, `CLAUDE.md`, `IDEAS.md`, `TODO.md` (whichever were missing).
- README rewritten with real install/usage content (replaced earlier one-line stub) where applicable.

### Files Modified
- CHANGELOG.md (created)
- CLAUDE.md (created where missing)
- IDEAS.md (created where missing)
- TODO.md (created where missing)
- README.md (rewritten where it was a stub)
