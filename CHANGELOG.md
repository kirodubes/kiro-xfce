# Changelog

## 2026.06.14

### What Changed
- Removed the three conky keybindings from XFCE (`Super + c` conky-toggle, `Ctrl + Alt + Page_Up` / `Ctrl + Alt + Page_Down` conky theme rotation). Edited at the real source (`xfce4-keyboard-shortcuts.xml`) and regenerated the cheatsheet.

### Technical Details
- Deleted the `<Super>c` (conky-toggle), `<Primary><Alt>Page_Up` (conky-rotate -n) and `<Primary><Alt>Page_Down` (conky-rotate -p) custom-command nodes from the xfconf shortcuts channel. Re-rendered `keybindings.txt` (now 104 bindings) and `keybindings.html` + `keybindings.pdf` via `kiro-keybindings-html.py` (pure transform of the `.txt`); header bumped to today.

### Files Modified
- `etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml`
- `etc/skel/.config/xfce4/keybindings.txt`
- `etc/skel/.config/xfce4/keybindings.html`
- `etc/skel/.config/xfce4/keybindings.pdf`

## 2026.06.08

### What Changed
- Rebound `Super + F9` from `lollypop` to `virt-manager` in `xfce4-keyboard-shortcuts.xml`, matching the distro-wide change applied across all Kiro environments.
- Regenerated the XFCE keybindings cheatsheet to catch up with source changes made to `xfce4-keyboard-shortcuts.xml`: `Ctrl + Alt + d` is now `obs` (was the show/hide-desktop WM action), and `Super + Ctrl + s` → `kiro-keybindings` (the universal cheatsheet hotkey) is now reflected in the cheatsheet.

### Technical Details
- `Super + F9`: changed the `<Super>F9` custom-command value from `lollypop` to `virt-manager`.
- `Ctrl + Alt + d` moved from the Window Management section to Applications & Launchers (it launches an app now, not a WM action), matching how every other Kiro cheatsheet sorts `obs`. Added the `Super + Ctrl + s` launcher line. Header bumped to today + unified generator name; the `Source:` line made repo-relative. Re-rendered `keybindings.html` + `keybindings.pdf` via `kiro-keybindings-html.py` (pure transform of the `.txt`).

### Files Modified
- `etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml`
- `etc/skel/.config/xfce4/keybindings.txt`
- `etc/skel/.config/xfce4/keybindings.html`
- `etc/skel/.config/xfce4/keybindings.pdf`

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
