# Quick Start

## Build
Install the RPM development tools
```sh
sudo dnf install fedpkg rpmdevtools
```
Download the tarball
```sh
spectool -g emacs-ada-mode.spec
```
Build the package (change `f39` to the target release of Fedora)
```sh
fedpkg --release f39 mockbuild
```
The RPM will be stored in a subfolder of `results_emacs-ada-mode` folder. Check it's contents using
```sh
rpm -qli ./results_emacs-ada-mode/<...>/emacs-ada-mode-<version>.<release>.noarch.rpm
```

## Install
Install the RPM using
```sh
sudo dnf install ./results_emacs-ada-mode/<...>/emacs-ada-mode-<version>.<release>.noarch.rpm
```
Uninstall using
```sh
sudo dnf remove emacs-ada-mode
```
