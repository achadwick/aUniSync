aUniSync
========

aUniSync is a low-profile interface to the Unison file synchronizer which presents as an icon in the notification area, runs in the background, and generally tries to stay out of your way.  It calls `unison` in batch, non-GUI mode shortly after you make changes to the files or folders within your configured Unison profiles.

If you use Unison for synchonizing files already, you may find it's an accepatble replacement for Dropbox or Ubuntu One.

For changes to files on the remote side, aUniSync uses a regular polling strategy.  It is network aware, and restarts synchronization when the network is available.  Synchronization can be paused for all profiles or just a subset by running Unison's GUI from the tray icon.

Installation
------------

Run the standard `setup.py` script in the usual way to install the script and its data files to your preferred prefix:

    $ python setup.py --help-commands
    $ python setup.py install --help
    $ python setup.py install --prefix=/usr/local

Folks running Debian-derived distros can do

    $ python setup.py install --user

but should make sure that the `~/.local/bin` folder is in their `$PATH`.

To make aUniSync run every time your desktop environment starts, copy `aunisync.desktop` into your `~/.config/autostart` folder.

Configuration
-------------

Active profiles and configuration are accessed via an icon in your desktop's notification area. This works well with Xfce4 on Debian, and it should be tolerable with Linux Mint, and Cinnamon or GNOME3 desktops too.

Ubuntu is more problematic. Patches are welcome for configuring via Ubuntu-style appindicators if supported on the system. Alternatively, Ubuntu users can reenable this standard feature by doing:

    $ gsettings set com.canonical.Unity.Panel systray-whitelist "['all']"

