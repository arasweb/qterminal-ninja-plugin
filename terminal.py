# -*- coding: utf-8 -*-
# PEP8:OK, LINT:OK, PY3:OK


#############################################################################
## This file may be used under the terms of the GNU General Public
## License version 2.0 or 3.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http:#www.fsf.org/licensing/licenses/info/GPLv2.html and
## http:#www.gnu.org/copyleft/gpl.html.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
#############################################################################


# metadata
' Terminal for Ninja-IDE '
__version__ = ' 0.1 '
__license__ = ' GPL '
__author__ = ' juancarlospaco '
__email__ = ' juancarlospaco@ubuntu.com '
__url__ = ''
__date__ = ' 15/02/2013 '
__prj__ = ' terminal '
__docformat__ = 'html'
__source__ = ''
__full_licence__ = ''


# imports
from sip import setapi

from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QDockWidget

try:
    from PyKDE4.kdecore import *
    from PyKDE4.kparts import *
except ImportError:
    pass

from ninja_ide.core import plugin


# API 2
(setapi(a, 2) for a in ("QDate", "QDateTime", "QString", "QTime", "QUrl",
                        "QTextStream", "QVariant"))


###############################################################################


class Terminal(plugin.Plugin):
    " Terminal Class "
    def initialize(self):
        " Init Class Terminal "
        self.terminal = QDockWidget()
        self.terminal.setFeatures(QDockWidget.DockWidgetFloatable |
                                           QDockWidget.DockWidgetMovable)
        self.terminal.setWindowTitle(__doc__)
        self.terminal.setStyleSheet('QDockWidget::title{text-align: center;}')
        try:
            self.factory = KPluginLoader("libkonsolepart").factory()
            self.terminal.setWidget(self.factory.create(self).widget())
        except:
            self.terminal.setWidget(QLabel(""" <center>
            <h3>ಠ_ಠ<br> ERROR: Please, install Konsole Terminal App ! </h3><br>
            <br><i> (Sorry, cant embed non-Qt Terminal Apps). </i><center>"""))
        self.misc = self.locator.get_service('misc')
        self.misc.add_widget(self.terminal,
                               QIcon.fromTheme("utilities-terminal"), __doc__)


###############################################################################


if __name__ == "__main__":
    print(__doc__)
