def Panel():
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
  Regions.DevicePanel.Check(Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel, False, False, 0, 0, "DevicePanel_Mask")
  Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel.TBitBtn2.Click()
  Regions.DevicePanel32.Check(Regions.CreateRegionInfo(Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel, 393, 44, 340, 201, False), False, False, 0, 0, "DevicePanel32_Mask")
  Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel.TBitBtn3.Click()
  Regions.DevicePanel30.Check(Regions.CreateRegionInfo(Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel, 393, 39, 341, 207, False), False, False, 0, 0, "DevicePanel30_Mask")
  Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel.TBitBtn4.Click()
  Regions.DevicePanel33.Check(Regions.CreateRegionInfo(Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel, 393, 44, 341, 199, False), False, False, 0, 0, "DevicePanel33_Mask")
  Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel.TBitBtn5.Click()
  Regions.DevicePanel29.Check(Regions.CreateRegionInfo(Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel, 396, 43, 337, 201, False), False, False, 0, 0, "DevicePanel29_Mask")
  Aliases.iTools.FrmMain.MDIClient.FrmPanelView.DevicePanel.TBitBtn6.Click()
  Aliases.iTools.FrmMain.VCLObject("BtnRemoveFromNetwork").Click()
  Aliases.iTools.TMessageForm2.No.ClickButton()
  Aliases.iTools.FrmMain.Close()