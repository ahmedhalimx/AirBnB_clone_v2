#!/usr/bin/python3
"""
Fabric script that Generates a .tgz archive
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Create a tar archive of the web_static dir.
    """
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
