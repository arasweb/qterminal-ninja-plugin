#7F7F7F# -*- coding: utf-8 -*-
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
' Terminal for Ninja-IDE based on xterm '
__version__ = ' 0.1 '
__license__ = ' GPL '
__author__ = ' arasweb '
__email__ = ' arasweb@users.noreply.github.com '
__url__ = ''
__date__ = ' 04/11/2016 '
__prj__ = ' qterminal '
__docformat__ = 'html'
__source__ = ''
__full_licence__ = ''


# imports
from sip import setapi

from PyQt4.QtCore import *
from PyQt4.QtGui import *


from ninja_ide.core import plugin

import sys
# API 2
(setapi(a, 2) for a in ("QDate", "QDateTime", "QString", "QTime", "QUrl",
                        "QTextStream", "QVariant"))


###############################################################################


class QTerminal(plugin.Plugin):
    " QTerminal Class "
    def initialize(self):
        " Init Class QTerminal "
        QDockWidget.__init__(self)
        self.terminal = QDockWidget()
        #self.terminal.setFeatures(QDockWidget.DockWidgetFloatable |
         #                         QDockWidget.DockWidgetMovable)
        self.terminal.setWindowTitle(__doc__)
        self.terminal.setStyleSheet('QDockWidget::title{text-align: center;}')
        layout = QVBoxLayout()
        layout.addWidget(self.terminal)
        try:
            self.process = QProcess()
            self.terminal.setWidget(self.process.start(
                'xterm', ['-into', str(self.terminal.winId())]))
        except:
            self.terminal.setWidget(QLabel(""" <center> <h3>ಠ_ಠ<br>
            ERROR: Please, install xterm and PyQt4 ! </h3><br>
            <br><i> (Sorry, cant embed non-Qt Terminal Apps). </i><center>"""))
        self.misc = self.locator.get_service('misc')
        self.misc.add_widget(self.terminal,
                               QIcon.fromTheme("utilities-terminal"), __doc__)


###############################################################################


if __name__ == "__main__":
    print(__doc__)
