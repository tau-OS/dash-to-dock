# Dash to Dock
![screenshot](https://github.com/micheleg/dash-to-dock/raw/master/media/screenshot.jpg)

## A dock for the GNOME Shell
This extension enhances the dash moving it out of the overview and transforming it in a dock for an easier launching of applications and a faster switching between windows and desktops without having to leave the desktop view.

[<img src="https://micheleg.github.io/dash-to-dock/media/get-it-on-ego.png" height="100">](https://extensions.gnome.org/extension/307/dash-to-dock)

For additional installation instructions and more information visit [https://micheleg.github.io/dash-to-dock/](https://micheleg.github.io/dash-to-dock/).

> This repository is based off of https://github.com/micheleg/dash-to-dock, to see the upstream source, visit that repository

## Installation from source

The extension can be installed directly from source, either for the convenience of using git or to test the latest development version. Clone the desired branch with git

### Build Dependencies

To compile the stylesheet you'll need `sassc`.

### Building

Clone the repository or download the branch from github.

To enable the extension, a shell reload is required `Alt+F2 r Enter` under Xorg or under Wayland you may have to logout and login. The extension has to be enabled  with *gnome-extensions-app* (GNOME Extensions) or with *dconf*.

```sh
git clone https://github.com/tau-OS/dash-to-dock.git
cd dash-to-dock
# To install the extension locally, use ~/.local
meson build --prefix=/usr
cd build
ninja && ninja install
```

## Bug Reporting

Bugs should be reported to the Github bug tracker [https://github.com/tau-OS/dash-to-dock/issues](https://github.com/tau-OS/dash-to-dock/issues).

## License
Dash to Dock Gnome Shell extension is distributed under the terms of the GNU General Public License,
version 2 or later. See the COPYING file for details.
