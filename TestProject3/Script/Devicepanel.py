﻿def Device():
  TestedApps.iTools.Run()
  Aliases.iTools.FrmMain.BtnNewClone.Click()
  Aliases.iTools.DlgTemplateFile.TabControl.ClickTab("EPC3000")
  Aliases.iTools.DlgTemplateFile.TabControl.LbxTemplate.ClickItem("EPC3004 V5.20 default")
  Aliases.iTools.DlgTemplateFile.OKBtn.ClickButton()
  Aliases.iTools.WaitChild('VCLObject("DlgServerCommand")',60000)
  Aliases.iTools.FrmMain.BtnPanelView.Click()
  Aliases.iTools.FrmMain.WaitChild('VCLObject("BtnTerminalWiring")', 60000)
  Aliases.iTools.FrmMain.BtnAccessLevel.Click()
  Aliases.iTools.FrmMain.BtnPanelView.Click()
  Aliases.iTools.FrmMain.MDIClient.FrmPanelView.Maximize()
  Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel.TBitBtn.Click()
  Regions.DevicePanel4.Check(Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel,False,False,3813)
  Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel.TBitBtn2.Click()
  Regions.DevicePanel5.Check(Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel,False,False,9286)
  Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel.TBitBtn3.Click()
  Regions.DevicePanel6.Check(Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel, False, False,3183)
  Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel.TBitBtn4.Click()
  Regions.DevicePanel6.Check(Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel, False, False,3886)
  Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel.TBitBtn5.Click()
  Regions.DevicePanel6.Check(Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel, False, False,4813)
  Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel.TBitBtn6.Click()
  Aliases.iTools.FrmMain.VCLObject("BtnRemoveFromNetwork").Click()
  Aliases.iTools.TMessageForm2.No.ClickButton()
  Aliases.iTools.FrmMain.Close()