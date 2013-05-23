# aUniSync

aUniSync keeps your files in sync using the [Unison file synchronizer](http://www.cis.upenn.edu/~bcpierce/unison/status.html). It runs Unison automatically whenever you make changes to the files you want to keep synchronized. Using aUniSync means that the files you care about are always the same everywhere.

File synchronization should just be pervasive, automatic and not keep annoying you. aUniSync presents as an icon in the notification area, and generally tries to stay out of your way.

For some setups, files can change on the remote side while you're working. To catch these cases reliably, aUniSync polls the remote side every so often. It is network aware, and restarts synchronization as soon as the network is available. Synchronization can be paused for all profiles or just a subset by running Unison's GUI from the status icon.

If you use Unison for synchonizing files already, you may find it's a pretty good partial replacement for Dropbox or Ubuntu One.

## Using aUniSync

After installation (see below), aUniSync can be run from your desktop's main menu or launcher.

When running aUniSync for the first time, nothing will happen until you set up some Unison profles to synchronize. aUniSync allows you to launch the main Unison GUI from its status icon's "Preferences" menu item. From there you can create and test new profiles and synchronize them for the first time before turning things over to aUniSync's control. While the Unison GUI is visible, aUniSync pauses its profiles

<center>![Status icon menu](https://raw.github.com/achadwick/aUniSync/master/images/statusiconmenu.png)</center>

The status icon's menu also lists out the profiles being managed, and allows them to be synchronized manually. Select a profile from the menu to launch Unison with the profile name as an argument. Note that this pauses automatic synchronization while the Unison window is open.

### Profile state icons

When aUniSync is running normally and synchronizing profiles, you'll see one of the following icons:

> **Idle: ![the Unison logo on its own, in a subdued colour](https://rawgithub.com/achadwick/aUniSync/master/icons/status/aunisync-idle-symbolic.svg)**

> > No files or folders have changed recently, and no synchronization is being done.

> **Changed: ![the Unison logo on its own, in bold](https://rawgithub.com/achadwick/aUniSync/master/icons/status/aunisync-changed-symbolic.svg)**

> > Files or folders have been changed recently, and they will be synchronized shortly. There's a short lead time of about 5 seconds to handle bursts of updates.

> **Syncing: ![the same logo with a pair of "synchronizing" arrows](https://rawgithub.com/achadwick/aUniSync/master/icons/status/aunisync-active-symbolic.svg)**

> > Currently synchronizing. This will be seen every so often even when the profile is otherwise idle because aUniSync occasionally polls for changes just in case the other end has changed.

If normal synchronization is interrupted for some reason, the icon shows why:

> **Manual Intervention: ![a gearwheel on the logo](https://rawgithub.com/achadwick/aUniSync/master/icons/status/aunisync-properties-symbolic.svg)**

> > aUniSync is running the regular Unison GUI for *this profile only*. Automatic synchronization is paused, and will resume when Unison exits.

> **Paused: ![the "paused" symbol on to the logo](https://rawgithub.com/achadwick/aUniSync/master/icons/status/aunisync-paused-symbolic.svg)**

> > The Unison GUI is running for *all profiles*, and synchronization is paused. In other words, Unison is running in "Preferences" mode. This mode allows new profiles to be added. When the Unison window is closed, aUniSync will reload its configuration and start synchronizing profiles again, inclusing any new ones.

> **Offline: ![an "X" mark next to the logo](https://rawgithub.com/achadwick/aUniSync/master/icons/status/aunisync-offline-symbolic.svg)**

> > The network is offline, and automatic synchronization is paused. When connectivity resumes, this flag will be cleared and automatic synchronizing will resume.

> **Error: ![an exclamation mark next to the logo](https://rawgithub.com/achadwick/aUniSync/master/icons/status/aunisync-error-symbolic.svg)**

> > Unison encountered a problem during batch-mode synchronization. The two ends of the profile are probably not fully synchronized. When network connectivity resumes, aUniSync makes an attempt to sync it anyway so don't worry too much about this if you see it briefly after un-suspending your laptop. If it persists, the problem might be solvable by launching the Unison GUI for the profile that's showing the error flag.

When you have more than one profile, the main status icon shows the most serious of these statuses.

## Installing aUniSync

Make sure you gave the Unison GUI, `unison-gtk` installed.

To install aUniSync and its icons, run the standard `setup.py` script in the usual way. Don't forget to specify your preferred prefix:

        $ python setup.py --help-commands
        $ python setup.py install --help
        $ python setup.py install --prefix=/usr/local

If you want to just install it for personal use, you can use the [user scheme](http://docs.python.org/2/install/#alternate-installation) for `setup.py`:

        $ python setup.py install --user

but you should make sure that the `~/.local/bin` folder is in your `$PATH`.

To make aUniSync run every time your desktop environment starts, copy `aunisync.desktop` into your `~/.config/autostart` folder.

## Known issues and omissions

* Active profiles and configuration are accessed via an icon in your desktop's notification area. This works well with Xfce4 on Debian, and it should work with Linux Mint, and with Cinnamon or GNOME3 desktops too. Ubuntu is more problematic. Patches are welcome for configuring via Ubuntu-style appindicators if supported on the system. Alternatively, Ubuntu users can reenable this standard feature by doing:

> > `$ gsettings set com.canonical.Unity.Panel systray-whitelist "['all']"`

* Handling of paths on removable media needs to be improved. aUniSync parses a profile's `mountpoint` options already, but doesn't interpret them specially yet. Looks like this would be the natural way of distinguishing profiles which correspond to removable media, but how to monitor the locations for insertions/removals?

* Running Unison from outside aUniSync doesn't pause the GUI in any way ☺

* Menu items should probably have larger state marks and not repeat the Unison logo each time.

* There's no configuration option for making aUniSync run when the desktop session starts.

* aUniSync should employ lockfiles or some other system (`GApplication`?) to prevent more than one instance from being launched simultaneously.

## License

The aUniSync program itself is licensed under the terms of the GNU General Public License, version 3 (or any later version). See the file COPYING contained with this program distribution for full details. If not, a copy can be downloaded from [the Free Software Foundation's licenses web page](http://www.gnu.org/licenses/).

> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

The symbolic icons contain elements taken from the gnome-icon-theme-symbolic distribution, which are licenced under the Creative Commons Attribution-Share Alike 3.0 United States License. To view a copy of this licence, visit http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to Creative Commons, 171 Second Street, Suite 300, San Francisco, California 94105, USA.

> When attributing this artwork, using "GNOME Project" is enough. Please link
to http://www.gnome.org where available.

These icons are themeable, although they should already adapt to your desktop's graphical style to some extent.
