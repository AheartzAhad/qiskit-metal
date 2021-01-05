# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_ui.ui',
# licensing of 'main_window_ui.ui' applies.
#
# Created: Tue Jan  5 12:28:39 2021
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/metal_logo"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowNestedDocks |
                                  QtWidgets.QMainWindow.AllowTabbedDocks |
                                  QtWidgets.QMainWindow.AnimatedDocks |
                                  QtWidgets.QMainWindow.GroupedDragging)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.mainViewTab = QtWidgets.QWidget()
        self.mainViewTab.setObjectName("mainViewTab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.mainViewTab)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/main_view"), QtGui.QIcon.Normal,
                        QtGui.QIcon.On)
        self.tabWidget.addTab(self.mainViewTab, icon1, "")
        self.tabElements = QtWidgets.QWidget()
        self.tabElements.setObjectName("tabElements")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tabElements)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/elements"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabElements, icon2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 22))
        self.menubar.setBaseSize(QtCore.QSize(0, 0))
        self.menubar.setObjectName("menubar")
        self.menuDesign = QtWidgets.QMenu(self.menubar)
        self.menuDesign.setTearOffEnabled(False)
        self.menuDesign.setSeparatorsCollapsible(True)
        self.menuDesign.setToolTipsVisible(True)
        self.menuDesign.setObjectName("menuDesign")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuStylesheet = QtWidgets.QMenu(self.menuView)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/metal_logo"), QtGui.QIcon.Normal,
                        QtGui.QIcon.On)
        self.menuStylesheet.setIcon(icon3)
        self.menuStylesheet.setObjectName("menuStylesheet")
        self.menuAnalysis = QtWidgets.QMenu(self.menubar)
        self.menuAnalysis.setObjectName("menuAnalysis")
        self.menuRender = QtWidgets.QMenu(self.menubar)
        self.menuRender.setObjectName("menuRender")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setMinimumSize(QtCore.QSize(0, 0))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/help"), QtGui.QIcon.Normal,
                        QtGui.QIcon.On)
        self.menuHelp.setIcon(icon4)
        self.menuHelp.setToolTipsVisible(True)
        self.menuHelp.setObjectName("menuHelp")
        self.menuPlot = QtWidgets.QMenu(self.menubar)
        self.menuPlot.setObjectName("menuPlot")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBarDesign = QtWidgets.QToolBar(MainWindow)
        self.toolBarDesign.setOrientation(QtCore.Qt.Horizontal)
        self.toolBarDesign.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBarDesign.setObjectName("toolBarDesign")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarDesign)
        self.toolBarView = QToolBarExpanding(MainWindow)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.toolBarView.setFont(font)
        self.toolBarView.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBarView.setObjectName("toolBarView")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBarView)
        self.dockDesign = QtWidgets.QDockWidget(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/design"), QtGui.QIcon.Normal,
                        QtGui.QIcon.On)
        self.dockDesign.setWindowIcon(icon5)
        self.dockDesign.setFloating(False)
        self.dockDesign.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockDesign.setObjectName("dockDesign")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(-1, 2, -1, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_comp_zoom = QtWidgets.QToolButton(self.dockWidgetContents)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/fullscreen"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btn_comp_zoom.setIcon(icon6)
        self.btn_comp_zoom.setObjectName("btn_comp_zoom")
        self.gridLayout.addWidget(self.btn_comp_zoom, 0, 3, 1, 1)
        self.btn_comp_actions = QtWidgets.QToolButton(self.dockWidgetContents)
        self.btn_comp_actions.setPopupMode(
            QtWidgets.QToolButton.MenuButtonPopup)
        self.btn_comp_actions.setObjectName("btn_comp_actions")
        self.gridLayout.addWidget(self.btn_comp_actions, 0, 1, 1, 1)
        self.btn_comp_del = QtWidgets.QToolButton(self.dockWidgetContents)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/delete"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.btn_comp_del.setIcon(icon7)
        self.btn_comp_del.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btn_comp_del.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.btn_comp_del.setObjectName("btn_comp_del")
        self.gridLayout.addWidget(self.btn_comp_del, 0, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filter_text_design = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.filter_text_design.setText("")
        self.filter_text_design.setClearButtonEnabled(True)
        self.filter_text_design.setObjectName("filter_text_design")
        self.horizontalLayout.addWidget(self.filter_text_design)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tableComponents = QTableView_AllComponents(self.dockWidgetContents)
        self.tableComponents.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableComponents.setAutoScroll(False)
        self.tableComponents.setAlternatingRowColors(True)
        self.tableComponents.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.tableComponents.setSortingEnabled(True)
        self.tableComponents.setObjectName("tableComponents")
        self.tableComponents.horizontalHeader().setVisible(True)
        self.tableComponents.horizontalHeader().setSortIndicatorShown(False)
        self.tableComponents.horizontalHeader().setStretchLastSection(True)
        self.tableComponents.verticalHeader().setVisible(False)
        self.verticalLayout_3.addWidget(self.tableComponents)
        self.dockDesign.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockDesign)
        self.dockNewComponent = QtWidgets.QDockWidget(MainWindow)
        self.dockNewComponent.setMinimumSize(QtCore.QSize(78, 123))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/component"), QtGui.QIcon.Normal,
                        QtGui.QIcon.On)
        self.dockNewComponent.setWindowIcon(icon8)
        self.dockNewComponent.setFeatures(
            QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockNewComponent.setObjectName("dockNewComponent")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.filter_text_component = QtWidgets.QLineEdit(
            self.dockWidgetContents_2)
        self.filter_text_component.setClearButtonEnabled(True)
        self.filter_text_component.setObjectName("filter_text_component")
        self.horizontalLayout_2.addWidget(self.filter_text_component)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.treeWidget = QtWidgets.QTreeWidget(self.dockWidgetContents_2)
        self.treeWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.treeWidget.setAutoScroll(False)
        self.treeWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.DoubleClicked)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setAnimated(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout_5.addWidget(self.treeWidget)
        self.dockNewComponent.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),
                                 self.dockNewComponent)
        self.dockComponent = QtWidgets.QDockWidget(MainWindow)
        self.dockComponent.setMinimumSize(QtCore.QSize(62, 38))
        self.dockComponent.setFeatures(
            QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockComponent.setObjectName("dockComponent")
        self.dockComponentCental = QtWidgets.QWidget()
        self.dockComponentCental.setObjectName("dockComponentCental")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.dockComponentCental)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.dockComponent.setWidget(self.dockComponentCental)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),
                                 self.dockComponent)
        self.dockLog = QtWidgets.QDockWidget(MainWindow)
        self.dockLog.setMinimumSize(QtCore.QSize(78, 100))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/log"), QtGui.QIcon.Normal,
                        QtGui.QIcon.On)
        self.dockLog.setWindowIcon(icon9)
        self.dockLog.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.dockLog.setObjectName("dockLog")
        self.dockWidgetContents_4 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dockWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_4.setSizePolicy(sizePolicy)
        self.dockWidgetContents_4.setObjectName("dockWidgetContents_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setSizeConstraint(
            QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.log_text = QTextEditLogger(self.dockWidgetContents_4)
        self.log_text.setTextInteractionFlags(
            QtCore.Qt.LinksAccessibleByKeyboard |
            QtCore.Qt.LinksAccessibleByMouse |
            QtCore.Qt.TextBrowserInteraction |
            QtCore.Qt.TextSelectableByKeyboard |
            QtCore.Qt.TextSelectableByMouse)
        self.log_text.setObjectName("log_text")
        self.verticalLayout_4.addWidget(self.log_text)
        self.dockLog.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.dockLog)
        self.dockConnectors = QtWidgets.QDockWidget(MainWindow)
        self.dockConnectors.setMinimumSize(QtCore.QSize(78, 123))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/connectors"), QtGui.QIcon.Normal,
                         QtGui.QIcon.On)
        self.dockConnectors.setWindowIcon(icon10)
        self.dockConnectors.setObjectName("dockConnectors")
        self.dockWidgetContents_5 = QtWidgets.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.text_filter_connectors = QtWidgets.QLineEdit(
            self.dockWidgetContents_5)
        self.text_filter_connectors.setClearButtonEnabled(True)
        self.text_filter_connectors.setObjectName("text_filter_connectors")
        self.horizontalLayout_3.addWidget(self.text_filter_connectors)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.tableConnectors = QtWidgets.QTableView(self.dockWidgetContents_5)
        self.tableConnectors.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableConnectors.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableConnectors.setAutoScroll(False)
        self.tableConnectors.setAlternatingRowColors(False)
        self.tableConnectors.setObjectName("tableConnectors")
        self.tableConnectors.horizontalHeader().setVisible(False)
        self.verticalLayout_6.addWidget(self.tableConnectors)
        self.dockConnectors.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),
                                 self.dockConnectors)
        self.dockVariables = QtWidgets.QDockWidget(MainWindow)
        self.dockVariables.setObjectName("dockVariables")
        self.dockVariablesContents = QtWidgets.QWidget()
        self.dockVariablesContents.setObjectName("dockVariablesContents")
        self.vlayoutVariables = QtWidgets.QVBoxLayout(
            self.dockVariablesContents)
        self.vlayoutVariables.setSpacing(0)
        self.vlayoutVariables.setContentsMargins(0, 0, 0, 0)
        self.vlayoutVariables.setObjectName("vlayoutVariables")
        self.dockVariables.setWidget(self.dockVariablesContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1),
                                 self.dockVariables)
        self.toolbar_renderers = QtWidgets.QToolBar(MainWindow)
        self.toolbar_renderers.setIconSize(QtCore.QSize(32, 32))
        self.toolbar_renderers.setObjectName("toolbar_renderers")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolbar_renderers)
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/save"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.actionSave.setIcon(icon11)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/load"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.actionLoad.setIcon(icon12)
        self.actionLoad.setAutoRepeat(False)
        self.actionLoad.setObjectName("actionLoad")
        self.actionDesign = QtWidgets.QAction(MainWindow)
        self.actionDesign.setCheckable(True)
        self.actionDesign.setChecked(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/design"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.actionDesign.setIcon(icon13)
        self.actionDesign.setObjectName("actionDesign")
        self.actionComponent = QtWidgets.QAction(MainWindow)
        self.actionComponent.setCheckable(True)
        self.actionComponent.setChecked(True)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/component"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.actionComponent.setIcon(icon14)
        self.actionComponent.setObjectName("actionComponent")
        self.actionElements = QtWidgets.QAction(MainWindow)
        self.actionElements.setCheckable(True)
        self.actionElements.setChecked(False)
        self.actionElements.setIcon(icon2)
        self.actionElements.setObjectName("actionElements")
        self.actionLog = QtWidgets.QAction(MainWindow)
        self.actionLog.setCheckable(True)
        self.actionLog.setChecked(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/log"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.actionLog.setIcon(icon15)
        self.actionLog.setObjectName("actionLog")
        self.actionNewComponent = QtWidgets.QAction(MainWindow)
        self.actionNewComponent.setCheckable(True)
        self.actionNewComponent.setChecked(False)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/component-library"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewComponent.setIcon(icon16)
        self.actionNewComponent.setObjectName("actionNewComponent")
        self.actionDelete_All = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/delete_all"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.actionDelete_All.setIcon(icon17)
        self.actionDelete_All.setPriority(QtWidgets.QAction.LowPriority)
        self.actionDelete_All.setObjectName("actionDelete_All")
        self.actionZoom = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/plot/zoom"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.actionZoom.setIcon(icon18)
        self.actionZoom.setObjectName("actionZoom")
        self.actionPan = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/plot/pan"), QtGui.QIcon.Normal,
                         QtGui.QIcon.On)
        self.actionPan.setIcon(icon19)
        self.actionPan.setObjectName("actionPan")
        self.actionConnectors = QtWidgets.QAction(MainWindow)
        self.actionConnectors.setCheckable(True)
        self.actionConnectors.setChecked(False)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(":/connectors"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.actionConnectors.setIcon(icon20)
        self.actionConnectors.setObjectName("actionConnectors")
        self.actionStyleOpen = QtWidgets.QAction(MainWindow)
        self.actionStyleOpen.setObjectName("actionStyleOpen")
        self.actionStyleDefault = QtWidgets.QAction(MainWindow)
        self.actionStyleDefault.setObjectName("actionStyleDefault")
        self.actionStyleDark = QtWidgets.QAction(MainWindow)
        self.actionStyleDark.setObjectName("actionStyleDark")
        self.actionScreenshot = QtWidgets.QAction(MainWindow)
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/screenshot"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.actionScreenshot.setIcon(icon21)
        self.actionScreenshot.setObjectName("actionScreenshot")
        self.action_full_refresh = QtWidgets.QAction(MainWindow)
        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap(":/force_refresh"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.action_full_refresh.setIcon(icon22)
        self.action_full_refresh.setShortcutContext(
            QtCore.Qt.WidgetWithChildrenShortcut)
        self.action_full_refresh.setAutoRepeat(False)
        self.action_full_refresh.setPriority(QtWidgets.QAction.HighPriority)
        self.action_full_refresh.setObjectName("action_full_refresh")
        self.actionRebuild = QtWidgets.QAction(MainWindow)
        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap(":/rebuild"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.actionRebuild.setIcon(icon23)
        self.actionRebuild.setPriority(QtWidgets.QAction.HighPriority)
        self.actionRebuild.setObjectName("actionRebuild")
        self.actionFull_Screen = QtWidgets.QAction(MainWindow)
        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap(":/plot/----autozoom"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFull_Screen.setIcon(icon24)
        self.actionFull_Screen.setObjectName("actionFull_Screen")
        self.actionMetal_Dark = QtWidgets.QAction(MainWindow)
        self.actionMetal_Dark.setObjectName("actionMetal_Dark")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setIcon(icon11)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionSave_window_state = QtWidgets.QAction(MainWindow)
        self.actionSave_window_state.setIcon(icon11)
        self.actionSave_window_state.setObjectName("actionSave_window_state")
        self.actionLabelDesign = QtWidgets.QAction(MainWindow)
        self.actionLabelDesign.setEnabled(False)
        self.actionLabelDesign.setObjectName("actionLabelDesign")
        self.actionClose_window = QtWidgets.QAction(MainWindow)
        self.actionClose_window.setObjectName("actionClose_window")
        self.actionMetal_Window = QtWidgets.QAction(MainWindow)
        self.actionMetal_Window.setEnabled(False)
        self.actionMetal_Window.setObjectName("actionMetal_Window")
        self.actionViewDummyLabel = QtWidgets.QAction(MainWindow)
        self.actionViewDummyLabel.setObjectName("actionViewDummyLabel")
        self.actionVariables = QtWidgets.QAction(MainWindow)
        self.actionVariables.setCheckable(True)
        self.actionVariables.setChecked(False)
        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap(":/variables"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.actionVariables.setIcon(icon25)
        self.actionVariables.setObjectName("actionVariables")
        self.actionToggleDocks = QtWidgets.QAction(MainWindow)
        self.actionToggleDocks.setIcon(icon6)
        self.actionToggleDocks.setObjectName("actionToggleDocks")
        self.actionNew_QComponent = QtWidgets.QAction(MainWindow)
        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap(":/add"), QtGui.QIcon.Normal,
                         QtGui.QIcon.Off)
        self.actionNew_QComponent.setIcon(icon26)
        self.actionNew_QComponent.setObjectName("actionNew_QComponent")
        self.actionGDS = QtWidgets.QAction(MainWindow)
        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap(":/renderer/_imgs/renderers/GDS.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGDS.setIcon(icon27)
        self.actionGDS.setObjectName("actionGDS")
        self.actionHFSS = QtWidgets.QAction(MainWindow)
        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap(":/renderer/_imgs/renderers/HFSS.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHFSS.setIcon(icon28)
        self.actionHFSS.setObjectName("actionHFSS")
        self.actionQ3D = QtWidgets.QAction(MainWindow)
        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap(":/renderer/_imgs/renderers/Q3D.png"),
                         QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQ3D.setIcon(icon29)
        self.actionQ3D.setObjectName("actionQ3D")
        self.menuDesign.addSeparator()
        self.menuDesign.addAction(self.actionLabelDesign)
        self.menuDesign.addAction(self.actionLoad)
        self.menuDesign.addAction(self.actionSave)
        self.menuDesign.addAction(self.actionSaveAs)
        self.menuDesign.addSeparator()
        self.menuDesign.addAction(self.actionDelete_All)
        self.menuDesign.addSeparator()
        self.menuDesign.addAction(self.actionClose_window)
        self.menuStylesheet.addAction(self.actionMetal_Dark)
        self.menuStylesheet.addAction(self.actionStyleDark)
        self.menuStylesheet.addSeparator()
        self.menuStylesheet.addAction(self.actionStyleDefault)
        self.menuStylesheet.addAction(self.actionStyleOpen)
        self.menuView.addAction(self.actionDesign)
        self.menuView.addAction(self.actionComponent)
        self.menuView.addAction(self.actionElements)
        self.menuView.addAction(self.actionConnectors)
        self.menuView.addAction(self.actionLog)
        self.menuView.addAction(self.actionNewComponent)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionToggleDocks)
        self.menuView.addAction(self.actionFull_Screen)
        self.menuView.addAction(self.actionScreenshot)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionMetal_Window)
        self.menuView.addAction(self.actionSave_window_state)
        self.menuView.addAction(self.menuStylesheet.menuAction())
        self.menuAnalysis.addSeparator()
        self.menuRender.addSeparator()
        self.menuPlot.addAction(self.actionPan)
        self.menuPlot.addAction(self.actionZoom)
        self.menubar.addAction(self.menuDesign.menuAction())
        self.menubar.addAction(self.menuPlot.menuAction())
        self.menubar.addAction(self.menuRender.menuAction())
        self.menubar.addAction(self.menuAnalysis.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBarDesign.addAction(self.actionLoad)
        self.toolBarDesign.addAction(self.actionSave)
        self.toolBarDesign.addAction(self.actionDelete_All)
        self.toolBarDesign.addSeparator()
        self.toolBarDesign.addAction(self.action_full_refresh)
        self.toolBarDesign.addAction(self.actionRebuild)
        self.toolBarDesign.addSeparator()
        self.toolBarDesign.addAction(self.actionNew_QComponent)
        self.toolBarView.addAction(self.actionViewDummyLabel)
        self.toolBarView.addAction(self.actionDesign)
        self.toolBarView.addAction(self.actionComponent)
        self.toolBarView.addAction(self.actionNewComponent)
        self.toolBarView.addAction(self.actionVariables)
        self.toolBarView.addSeparator()
        self.toolBarView.addAction(self.actionConnectors)
        self.toolBarView.addAction(self.actionLog)
        self.toolBarView.addSeparator()
        self.toolBarView.addAction(self.actionToggleDocks)
        self.toolBarView.addAction(self.actionScreenshot)
        self.toolbar_renderers.addAction(self.actionGDS)
        self.toolbar_renderers.addAction(self.actionHFSS)
        self.toolbar_renderers.addAction(self.actionQ3D)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.actionElements,
                               QtCore.SIGNAL("toggled(bool)"),
                               MainWindow._set_element_tab)
        QtCore.QObject.connect(self.actionDelete_All,
                               QtCore.SIGNAL("triggered()"),
                               MainWindow.delete_all_components)
        QtCore.QObject.connect(self.actionLoad, QtCore.SIGNAL("triggered()"),
                               MainWindow.load_design)
        QtCore.QObject.connect(self.actionSave, QtCore.SIGNAL("triggered()"),
                               MainWindow.save_design)
        QtCore.QObject.connect(self.actionStyleDark,
                               QtCore.SIGNAL("triggered()"),
                               MainWindow.load_stylesheet_dark)
        QtCore.QObject.connect(self.actionStyleDefault,
                               QtCore.SIGNAL("triggered()"),
                               MainWindow.load_stylesheet_default)
        QtCore.QObject.connect(self.actionScreenshot,
                               QtCore.SIGNAL("triggered()"),
                               MainWindow._screenshot)
        QtCore.QObject.connect(self.actionStyleOpen,
                               QtCore.SIGNAL("triggered()"),
                               MainWindow.load_stylesheet_open)
        QtCore.QObject.connect(self.action_full_refresh,
                               QtCore.SIGNAL("triggered()"),
                               MainWindow.full_refresh)
        QtCore.QObject.connect(self.actionRebuild, QtCore.SIGNAL("triggered()"),
                               MainWindow.rebuild)
        QtCore.QObject.connect(self.actionFull_Screen,
                               QtCore.SIGNAL("triggered()"),
                               MainWindow.showFullScreen)
        QtCore.QObject.connect(self.actionMetal_Dark,
                               QtCore.SIGNAL("triggered()"),
                               MainWindow.load_stylesheet_metal_dark)
        QtCore.QObject.connect(self.dockDesign,
                               QtCore.SIGNAL("visibilityChanged(bool)"),
                               self.actionDesign.setChecked)
        QtCore.QObject.connect(self.actionDesign,
                               QtCore.SIGNAL("triggered(bool)"),
                               self.dockDesign.show)
        QtCore.QObject.connect(self.actionComponent,
                               QtCore.SIGNAL("triggered()"),
                               self.dockComponent.show)
        QtCore.QObject.connect(self.dockConnectors,
                               QtCore.SIGNAL("visibilityChanged(bool)"),
                               self.actionConnectors.setChecked)
        QtCore.QObject.connect(self.dockLog,
                               QtCore.SIGNAL("visibilityChanged(bool)"),
                               self.actionLog.setChecked)
        QtCore.QObject.connect(self.dockComponent,
                               QtCore.SIGNAL("visibilityChanged(bool)"),
                               self.actionComponent.setChecked)
        QtCore.QObject.connect(self.dockNewComponent,
                               QtCore.SIGNAL("visibilityChanged(bool)"),
                               self.actionNewComponent.setChecked)
        QtCore.QObject.connect(self.actionNewComponent,
                               QtCore.SIGNAL("triggered(bool)"),
                               self.dockNewComponent.show)
        QtCore.QObject.connect(self.actionLog, QtCore.SIGNAL("triggered(bool)"),
                               self.dockLog.show)
        QtCore.QObject.connect(self.actionConnectors,
                               QtCore.SIGNAL("triggered(bool)"),
                               self.dockConnectors.show)
        QtCore.QObject.connect(self.actionDesign, QtCore.SIGNAL("triggered()"),
                               self.dockDesign.raise_)
        QtCore.QObject.connect(self.actionConnectors,
                               QtCore.SIGNAL("triggered()"),
                               self.dockConnectors.raise_)
        QtCore.QObject.connect(self.actionNewComponent,
                               QtCore.SIGNAL("triggered()"),
                               self.dockNewComponent.raise_)
        QtCore.QObject.connect(self.actionComponent,
                               QtCore.SIGNAL("triggered()"),
                               self.dockComponent.raise_)
        QtCore.QObject.connect(self.actionElements,
                               QtCore.SIGNAL("triggered()"),
                               self.tabWidget.setFocus)
        QtCore.QObject.connect(self.actionLog, QtCore.SIGNAL("triggered()"),
                               self.dockLog.raise_)
        QtCore.QObject.connect(self.actionSaveAs,
                               QtCore.SIGNAL("toggled(bool)"),
                               MainWindow.save_design_as)
        QtCore.QObject.connect(self.actionClose_window,
                               QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QObject.connect(self.actionSave_window_state,
                               QtCore.SIGNAL("triggered()"),
                               MainWindow.save_window_settings)
        QtCore.QObject.connect(self.actionVariables,
                               QtCore.SIGNAL("triggered(bool)"),
                               self.dockVariables.show)
        QtCore.QObject.connect(self.actionVariables,
                               QtCore.SIGNAL("triggered()"),
                               self.dockVariables.raise_)
        QtCore.QObject.connect(self.actionToggleDocks,
                               QtCore.SIGNAL("triggered()"),
                               MainWindow.toggle_all_docks)
        QtCore.QObject.connect(self.actionNew_QComponent,
                               QtCore.SIGNAL("triggered()"),
                               MainWindow.new_qcomponent)
        QtCore.QObject.connect(self.actionGDS, QtCore.SIGNAL("triggered()"),
                               MainWindow.show_renderer_gds)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Qiskit Metal: Quantum Creator",
                                             None, -1))
        MainWindow.setToolTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Qiskit Metal: Quantum Creator",
                                             None, -1))
        MainWindow.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Qiskit Metal: Quantum Creator",
                                             None, -1))
        MainWindow.setWhatsThis(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Qiskit Metal: Quantum Creator",
                                             None, -1))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.mainViewTab),
            QtWidgets.QApplication.translate("MainWindow", "Main View", None,
                                             -1))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabElements),
            QtWidgets.QApplication.translate("MainWindow", "Elements", None,
                                             -1))
        self.tabWidget.setTabToolTip(
            self.tabWidget.indexOf(self.tabElements),
            QtWidgets.QApplication.translate(
                "MainWindow", "Shoe the tables of elements of the the design",
                None, -1))
        self.menuDesign.setToolTip(
            QtWidgets.QApplication.translate("MainWindow", "Design Menu", None,
                                             -1))
        self.menuDesign.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow", "Design Menu", None,
                                             -1))
        self.menuDesign.setWhatsThis(
            QtWidgets.QApplication.translate("MainWindow", "Design Menu", None,
                                             -1))
        self.menuDesign.setTitle(
            QtWidgets.QApplication.translate("MainWindow", "Metal Design", None,
                                             -1))
        self.menuView.setTitle(
            QtWidgets.QApplication.translate("MainWindow", "Window View", None,
                                             -1))
        self.menuStylesheet.setTitle(
            QtWidgets.QApplication.translate("MainWindow", "Color theme", None,
                                             -1))
        self.menuAnalysis.setTitle(
            QtWidgets.QApplication.translate("MainWindow", "Analysis", None,
                                             -1))
        self.menuRender.setTitle(
            QtWidgets.QApplication.translate("MainWindow", "Render", None, -1))
        self.menuHelp.setToolTip(
            QtWidgets.QApplication.translate("MainWindow", "Open Metal Help",
                                             None, -1))
        self.menuHelp.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow", "Open Metal Help",
                                             None, -1))
        self.menuHelp.setWhatsThis(
            QtWidgets.QApplication.translate("MainWindow", "Open Metal Help",
                                             None, -1))
        self.menuHelp.setTitle(
            QtWidgets.QApplication.translate("MainWindow", "Help", None, -1))
        self.menuPlot.setTitle(
            QtWidgets.QApplication.translate("MainWindow", "Plot", None, -1))
        self.toolBarDesign.setWindowTitle(
            QtWidgets.QApplication.translate("MainWindow", "Design toolbar",
                                             None, -1))
        self.toolBarDesign.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow", "Design toolbar",
                                             None, -1))
        self.toolBarDesign.setWhatsThis(
            QtWidgets.QApplication.translate("MainWindow", "Design toolbar",
                                             None, -1))
        self.toolBarView.setWindowTitle(
            QtWidgets.QApplication.translate("MainWindow", "View Toolbar", None,
                                             -1))
        self.toolBarView.setToolTip(
            QtWidgets.QApplication.translate("MainWindow", "View Toolbar", None,
                                             -1))
        self.toolBarView.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow", "View Toolbar", None,
                                             -1))
        self.toolBarView.setWhatsThis(
            QtWidgets.QApplication.translate("MainWindow", "View Toolbar", None,
                                             -1))
        self.dockDesign.setToolTip(
            QtWidgets.QApplication.translate("MainWindow", "Design Dock", None,
                                             -1))
        self.dockDesign.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow", "Design Dock", None,
                                             -1))
        self.dockDesign.setWhatsThis(
            QtWidgets.QApplication.translate("MainWindow", "Design Dock", None,
                                             -1))
        self.dockDesign.setAccessibleName(
            QtWidgets.QApplication.translate("MainWindow", "Design Dock", None,
                                             -1))
        self.dockDesign.setAccessibleDescription(
            QtWidgets.QApplication.translate("MainWindow", "Design Dock", None,
                                             -1))
        self.dockDesign.setWindowTitle(
            QtWidgets.QApplication.translate("MainWindow", "QComponents", None,
                                             -1))
        self.btn_comp_zoom.setToolTip(
            QtWidgets.QApplication.translate(
                "MainWindow", "Focus on component in drawing window", None, -1))
        self.btn_comp_zoom.setStatusTip(
            QtWidgets.QApplication.translate(
                "MainWindow", "Focus on component in drawing window", None, -1))
        self.btn_comp_zoom.setText(
            QtWidgets.QApplication.translate(
                "MainWindow", "Focus on component in drawing window", None, -1))
        self.btn_comp_actions.setText(
            QtWidgets.QApplication.translate("MainWindow", "Do", None, -1))
        self.btn_comp_del.setToolTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Delete a selected component",
                                             None, -1))
        self.btn_comp_del.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Delete a selected component",
                                             None, -1))
        self.btn_comp_del.setWhatsThis(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Delete a selected component",
                                             None, -1))
        self.btn_comp_del.setText(
            QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.filter_text_design.setPlaceholderText(
            QtWidgets.QApplication.translate("MainWindow", "Filter", None, -1))
        self.dockNewComponent.setToolTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Library of components", None, -1))
        self.dockNewComponent.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Library design components", None,
                                             -1))
        self.dockNewComponent.setWhatsThis(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Library design components", None,
                                             -1))
        self.dockNewComponent.setWindowTitle(
            QtWidgets.QApplication.translate("MainWindow", "Library", None, -1))
        self.filter_text_component.setPlaceholderText(
            QtWidgets.QApplication.translate("MainWindow", "Filter", None, -1))
        self.treeWidget.setSortingEnabled(True)
        self.dockComponent.setWindowTitle(
            QtWidgets.QApplication.translate("MainWindow", "Edit component",
                                             None, -1))
        self.dockLog.setToolTip(
            QtWidgets.QApplication.translate("MainWindow", "Log window", None,
                                             -1))
        self.dockLog.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow", "Log window", None,
                                             -1))
        self.dockLog.setWhatsThis(
            QtWidgets.QApplication.translate("MainWindow", "Log window", None,
                                             -1))
        self.dockLog.setWindowTitle(
            QtWidgets.QApplication.translate("MainWindow", "Log", None, -1))
        self.log_text.setDocumentTitle(
            QtWidgets.QApplication.translate("MainWindow", "Log", None, -1))
        self.dockConnectors.setWindowTitle(
            QtWidgets.QApplication.translate("MainWindow", "Pins", None, -1))
        self.text_filter_connectors.setPlaceholderText(
            QtWidgets.QApplication.translate("MainWindow", "Filter", None, -1))
        self.dockVariables.setWindowTitle(
            QtWidgets.QApplication.translate("MainWindow", "Variables", None,
                                             -1))
        self.toolbar_renderers.setWindowTitle(
            QtWidgets.QApplication.translate("MainWindow", "toolBar", None, -1))
        self.actionSave.setText(
            QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))
        self.actionSave.setToolTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Save design to file", None, -1))
        self.actionSave.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Save design to file", None, -1))
        self.actionSave.setWhatsThis(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Save design to file", None, -1))
        self.actionSave.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "Ctrl+S", None, -1))
        self.actionLoad.setText(
            QtWidgets.QApplication.translate("MainWindow", "Load", None, -1))
        self.actionLoad.setToolTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Load design from file", None, -1))
        self.actionLoad.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Load design from file", None, -1))
        self.actionLoad.setWhatsThis(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Load design from file", None, -1))
        self.actionLoad.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "Ctrl+O", None, -1))
        self.actionDesign.setText(
            QtWidgets.QApplication.translate("MainWindow", "Select component",
                                             None, -1))
        self.actionDesign.setToolTip(
            QtWidgets.QApplication.translate(
                "MainWindow",
                "Show design window -- select components (show/hide)", None,
                -1))
        self.actionDesign.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "Ctrl+D", None, -1))
        self.actionComponent.setText(
            QtWidgets.QApplication.translate("MainWindow", "Edit component",
                                             None, -1))
        self.actionComponent.setToolTip(
            QtWidgets.QApplication.translate(
                "MainWindow", "Edit a component of the design (show/hide)",
                None, -1))
        self.actionComponent.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Edit a design component", None,
                                             -1))
        self.actionComponent.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "Ctrl+E", None, -1))
        self.actionElements.setText(
            QtWidgets.QApplication.translate("MainWindow", "Elements", None,
                                             -1))
        self.actionElements.setToolTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Show/hide elements table", None,
                                             -1))
        self.actionLog.setText(
            QtWidgets.QApplication.translate("MainWindow", "Log", None, -1))
        self.actionLog.setToolTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Show/hide log window", None, -1))
        self.actionLog.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "Ctrl+L", None, -1))
        self.actionNewComponent.setText(
            QtWidgets.QApplication.translate("MainWindow", "Create", None, -1))
        self.actionNewComponent.setToolTip(
            QtWidgets.QApplication.translate(
                "MainWindow",
                "Create new component: Library of new design components you can create",
                None, -1))
        self.actionNewComponent.setStatusTip(
            QtWidgets.QApplication.translate(
                "MainWindow",
                "Create new component: Library of new design components you can create",
                None, -1))
        self.actionNewComponent.setWhatsThis(
            QtWidgets.QApplication.translate(
                "MainWindow",
                "Create new component: Library of new design components you can create",
                None, -1))
        self.actionNewComponent.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "Ctrl+N", None, -1))
        self.actionDelete_All.setText(
            QtWidgets.QApplication.translate("MainWindow", "Delete all", None,
                                             -1))
        self.actionDelete_All.setToolTip(
            QtWidgets.QApplication.translate(
                "MainWindow", "Delete All Component Objects and Elements", None,
                -1))
        self.actionDelete_All.setStatusTip(
            QtWidgets.QApplication.translate(
                "MainWindow", "Delete All Component Objects and Elements", None,
                -1))
        self.actionDelete_All.setWhatsThis(
            QtWidgets.QApplication.translate(
                "MainWindow", "Delete All Component Objects and Elements", None,
                -1))
        self.actionZoom.setText(
            QtWidgets.QApplication.translate("MainWindow", "Zoom", None, -1))
        self.actionZoom.setToolTip(
            QtWidgets.QApplication.translate("MainWindow", "Zoom control", None,
                                             -1))
        self.actionZoom.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "Z", None, -1))
        self.actionPan.setText(
            QtWidgets.QApplication.translate("MainWindow", "Pan", None, -1))
        self.actionPan.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "P", None, -1))
        self.actionConnectors.setText(
            QtWidgets.QApplication.translate("MainWindow", "Pins", None, -1))
        self.actionConnectors.setToolTip(
            QtWidgets.QApplication.translate(
                "MainWindow", "Show connector pins of qcomponents", None, -1))
        self.actionConnectors.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "C", None, -1))
        self.actionStyleOpen.setText(
            QtWidgets.QApplication.translate("MainWindow", "Open File", None,
                                             -1))
        self.actionStyleDefault.setText(
            QtWidgets.QApplication.translate("MainWindow", "System default",
                                             None, -1))
        self.actionStyleDark.setText(
            QtWidgets.QApplication.translate("MainWindow", "Q Dark", None, -1))
        self.actionScreenshot.setText(
            QtWidgets.QApplication.translate("MainWindow", "Screenshot", None,
                                             -1))
        self.actionScreenshot.setToolTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Take a screenshot of the window",
                                             None, -1))
        self.action_full_refresh.setText(
            QtWidgets.QApplication.translate("MainWindow", "Replot", None, -1))
        self.action_full_refresh.setToolTip(
            QtWidgets.QApplication.translate(
                "MainWindow",
                "Replot all components (and refresh all gui widgets). Does NOT REBUILD",
                None, -1))
        self.action_full_refresh.setStatusTip(
            QtWidgets.QApplication.translate(
                "MainWindow", "Force a full refresh of all plots and widgets",
                None, -1))
        self.action_full_refresh.setWhatsThis(
            QtWidgets.QApplication.translate(
                "MainWindow", "Force a full refresh of all plots and widgets",
                None, -1))
        self.action_full_refresh.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "Ctrl+R", None, -1))
        self.actionRebuild.setText(
            QtWidgets.QApplication.translate("MainWindow", "Rebuild", None, -1))
        self.actionRebuild.setToolTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Force rebuild all components",
                                             None, -1))
        self.actionRebuild.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Force rebuild all components",
                                             None, -1))
        self.actionRebuild.setWhatsThis(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Force rebuild all components",
                                             None, -1))
        self.actionRebuild.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "Ctrl+D", None, -1))
        self.actionFull_Screen.setText(
            QtWidgets.QApplication.translate("MainWindow", "Full Screen", None,
                                             -1))
        self.actionFull_Screen.setToolTip(
            QtWidgets.QApplication.translate("MainWindow", "Go to full screen",
                                             None, -1))
        self.actionMetal_Dark.setText(
            QtWidgets.QApplication.translate("MainWindow", "Metal Dark", None,
                                             -1))
        self.actionSaveAs.setText(
            QtWidgets.QApplication.translate("MainWindow", "Save as", None, -1))
        self.actionSaveAs.setToolTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Save design to new file", None,
                                             -1))
        self.actionSaveAs.setStatusTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Save design to file", None, -1))
        self.actionSaveAs.setWhatsThis(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Save design to file", None, -1))
        self.actionSaveAs.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "Ctrl+Shift+S", None,
                                             -1))
        self.actionSave_window_state.setText(
            QtWidgets.QApplication.translate("MainWindow", "Save window state",
                                             None, -1))
        self.actionLabelDesign.setText(
            QtWidgets.QApplication.translate("MainWindow", "Design", None, -1))
        self.actionClose_window.setText(
            QtWidgets.QApplication.translate("MainWindow", "Close window", None,
                                             -1))
        self.actionMetal_Window.setText(
            QtWidgets.QApplication.translate("MainWindow", "Metal Window ",
                                             None, -1))
        self.actionViewDummyLabel.setText(
            QtWidgets.QApplication.translate("MainWindow", "View", None, -1))
        self.actionVariables.setText(
            QtWidgets.QApplication.translate("MainWindow", "Design variables",
                                             None, -1))
        self.actionVariables.setToolTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Edit variables of the QDesign",
                                             None, -1))
        self.actionVariables.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "Meta+V", None, -1))
        self.actionToggleDocks.setText(
            QtWidgets.QApplication.translate("MainWindow", "Toggle view", None,
                                             -1))
        self.actionToggleDocks.setToolTip(
            QtWidgets.QApplication.translate("MainWindow", "ToggleDocks", None,
                                             -1))
        self.actionToggleDocks.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "Meta+F, Ctrl+F",
                                             None, -1))
        self.actionNew_QComponent.setText(
            QtWidgets.QApplication.translate("MainWindow", "New QComponent",
                                             None, -1))
        self.actionNew_QComponent.setToolTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Create a new QComponent file",
                                             None, -1))
        self.actionNew_QComponent.setShortcut(
            QtWidgets.QApplication.translate("MainWindow", "Ctrl+N, Meta+N",
                                             None, -1))
        self.actionGDS.setText(
            QtWidgets.QApplication.translate("MainWindow", "GDS", None, -1))
        self.actionGDS.setToolTip(
            QtWidgets.QApplication.translate("MainWindow",
                                             "Open the GDS renderer.", None,
                                             -1))
        self.actionHFSS.setText(
            QtWidgets.QApplication.translate("MainWindow", "HFSS", None, -1))
        self.actionQ3D.setText(
            QtWidgets.QApplication.translate("MainWindow", "Q3D", None, -1))


from .widgets.bases.expanding_toolbar import QToolBarExpanding
from .widgets.log_widget.log_metal import QTextEditLogger
from .widgets.all_components.table_view_all_components import QTableView_AllComponents
from . import main_window_rc_rc
