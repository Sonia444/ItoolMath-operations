import iToolsoperations
def PerformMathoperation():
  iToolsoperations.Launching()
  Log.Message(Project.Variables.Var1)
  Driver=DDT.CSVDriver(Project.Variables.Var1)
  while not DDT.CurrentDriver.EOF():
      op=Driver.Value[0]
      in1=Driver.Value[1]
      in2=Driver.Value[2]
      out=Driver.Value[3]
      Log.Message(str(op)+" "+str(in1)+" "+str(in2)+" "+str(out))
      Mathoperations(op,in1,in2,out)
      DDT.CurrentDriver.Next()
  DDT.CloseDriver(DDT.CurrentDriver.Name)
  iToolsoperations.Closing()
    
  
def Mathoperations(op,in1,in2,out):
    
    Aliases.iTools.FrmMain.PnlDevBrowse.PnlDevBrowseMain.PgeDevBrowse.ClickTab("Browse")
    Aliases.iTools.FrmMain.PnlDevBrowse.PnlDevBrowseMain.PgeDevBrowse.TabBrowse.TvwTags.ExpandItem("|Math2")
    Aliases.iTools.FrmMain.PnlDevBrowse.PnlDevBrowseMain.PgeDevBrowse.TabBrowse.TvwTags.ClickItem("|Math2")
    Aliases.iTools.FrmMain.PnlDevBrowse.PnlDevBrowseMain.PgeDevBrowse.TabBrowse.TvwTags.ExpandItem("|Math2|1")
    Aliases.iTools.FrmMain.PnlDevBrowse.PnlDevBrowseMain.PgeDevBrowse.TabBrowse.TvwTags.DblClickItem("|Math2|1|Oper")
    Aliases.iTools.WaitChild('VCLObject("DlgWriteValue")',30000)
    Aliases.iTools.DlgWriteValue.VCLObject("LblValue").Click()
    if op==1:
        Aliases.iTools.DlgWriteValue.CmbValue.ClickItem("Add (1)")
    elif op==2:
        Aliases.iTools.DlgWriteValue.CmbValue.ClickItem("Sub (2)")
    elif op==3:
        Aliases.iTools.DlgWriteValue.CmbValue.ClickItem("Mul (3)")
    elif op==4:
          Aliases.iTools.DlgWriteValue.CmbValue.ClickItem("Div (4)")
  
    Aliases.iTools.DlgWriteValue.PnlButtons.BtnOK.ClickButton()
    Aliases.iTools.FrmMain.PnlDevBrowse.PnlDevBrowseMain.PgeDevBrowse.TabBrowse.TvwTags.DblClickItem("|Math2|1|In1")
    Aliases.iTools.WaitChild('VCLObject("DlgWriteValue")',60000)
    Aliases.iTools.DlgWriteValue.VCLObject("LblValue").Click()
    Aliases.iTools.DlgWriteValue.VCLObject("LblValue").Click()
    Aliases.iTools.DlgWriteValue.EdtValue.SetText(in1)
    Aliases.iTools.DlgWriteValue.PnlButtons.BtnOK.ClickButton()
    Aliases.iTools.FrmMain.PnlDevBrowse.PnlDevBrowseMain.PgeDevBrowse.TabBrowse.TvwTags.DblClickItem("|Math2|1|In2")
    Aliases.iTools.WaitChild('VCLObject("DlgWriteValue")',60000)
    Aliases.iTools.DlgWriteValue.VCLObject("LblValue").Click()
    Aliases.iTools.DlgWriteValue.VCLObject("LblValue").Click()
    Aliases.iTools.DlgWriteValue.EdtValue.SetText(in2)
    Aliases.iTools.DlgWriteValue.PnlButtons.BtnOK.ClickButton()
    Aliases.iTools.FrmMain.PnlDevBrowse.PnlDevBrowseMain.PgeDevBrowse.TabBrowse.TvwTags.DblClickItem("|Math2|1|Out")
    Aliases.iTools.WaitChild('VCLObject("DlgWriteValue")',60000)
    aqObject.CheckProperty(Aliases.iTools.DlgWriteValue.VCLObject("LblCurrVal"), "Caption" , cmpEqual,out)
    Aliases.iTools.WaitChild('VCLObject("BtnCancel")',6000)
    Aliases.iTools.DlgWriteValue.PnlButtons.BtnCancel.ClickButton()

    


