
def Launching():
  TestedApps.iTools.Run()
  Aliases.iTools.FrmMain.WaitChild('VCLObject("BtnNewClone")', 60000)
  Aliases.iTools.FrmMain.BtnNewClone.Click()
  Aliases.iTools.DlgTemplateFile.TabControl.ClickTab("EPC3000")
  Aliases.iTools.DlgTemplateFile.TabControl.LbxTemplate.ClickItem("EPC3004 V5.20 default")
  Aliases.iTools.DlgTemplateFile.OKBtn.ClickButton()
  Aliases.iTools.WaitChild('VCLObject("DlgServerCommand")',6000)
  Aliases.iTools.FrmMain.BtnParamExplorer.Click()
  Aliases.iTools.FrmMain.WaitChild('VCLObject("BtnAccessLevel")', 80000)
  Aliases.iTools.FrmMain.BtnAccessLevel.Click()
  aqObject.CheckProperty(Aliases.iTools.FrmMain.BtnAccessLevel, "Enabled", cmpEqual, True)
  Aliases.iTools.FrmMain.Click()
  Aliases.iTools.DlgWriteValue.PnlButtons.WaitChild('VCLObject("pnlButtond")',60000)
  
  
def Closing():
  Aliases.iTools.FrmMain.VCLObject("BtnRemoveFromNetwork").Click()
  Aliases.iTools.TMessageForm2.No.ClickButton()
  Aliases.iTools.FrmMain.Close()