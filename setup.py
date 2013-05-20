#!/usr/bin/env python

from distutils.core import setup

setup(
    name="aunisync",
    version="0.0.1",
    scripts=["aunisync"],
    data_files=[("share/applications", ["aunisync.desktop"])],
    author="Andrew Chadwick",
    author_email="a.t.chadwick@gmail.com",
    fullname="Automatic Unison Synchronizer",
    description="Automatically synchronizes files and folders in Unison profiles whenever they're modified",
    long_description="""

aUniSync is a low-profile interface to the Unison file synchronizer which
presents as an icon in the system tray, runs in the background, and tries to
stay out of your way.  It calls unison in batch, non-GUI mode shortly after you
make changes to files or folders within your configured Unison profiles.

For changes to files on the remote side, aUniSync uses a regular polling
strategy.  It is network aware, and restarts synchronization when the network
is available.  Synchronization can be paused for all profiles or just a subset
by running Unison's GUI from the tray icon.

""",
    keywords=["unison", "synchronizing", "sync", "replication", "dropbox-like",
              "inotify", "system tray", "status icon"],
    license="License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
)

