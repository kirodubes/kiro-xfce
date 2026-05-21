# edu-xfce

Educational / tutorial repository for [Xfce 4](https://www.xfce.org/), the lightweight classic desktop environment. Part of the `~/EDU/` learning series — Erik's Xfce defaults dropped on top of a fresh Arch / Kiro install.

## What's in this repo

- `etc/skel/` — Xfce user config (xfconf settings, panel layout, autostart entries) that lands in `/etc/skel/`.
- `setup.sh`, `up.sh`, `cleanup.sh` — standard EDU bash scaffold.

## Installation

### From `nemesis_repo` (recommended)

```ini
[nemesis_repo]
SigLevel = Never
Server = https://erikdubois.github.io/$repo/$arch
```

```bash
sudo pacman -Syu
sudo pacman -S edu-xfce
```

You'll also need Xfce itself:

```bash
sudo pacman -S xfce4 xfce4-goodies
```

### Manual

```bash
git clone https://github.com/erikdubois/edu-xfce.git
cd edu-xfce
sudo cp -r etc/skel/. /etc/skel/
```

Existing users can pull the config into their own home:

```bash
cp -rT /etc/skel ~/
```

## Websites

Information : https://erikdubois.be

## Social Media

Youtube : https://www.youtube.com/erikdubois

## License

See [LICENSE](./LICENSE).
