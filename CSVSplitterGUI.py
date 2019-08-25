import PySimpleGUI as sg
import sys
import CSVSplitterFnFiles

layout = [[sg.Text('CSV Splitter')],
          [sg.Text('Choose your CSV file:')],
          [sg.Input(enable_events=True,key='_INPUT_FILEPATH_'), sg.FileBrowse()],
          [sg.Button('RowCount',key='_BTN_ROWCOUNT_'), sg.Input('',key='_INPUT_ROWCOUNT_',size=(5,5), disabled=True)],
          [sg.Check('Include Header in all Output Files',key='_CHK_INCHEADER_',default=True)],
          #[sg.Check()]
          [sg.Radio('Normal Split','SplitType',enable_events=True, key='_RB1_NS_',default=True)],
          [sg.Text('No. of Records per File: ', size=(20,1),key='_TXT_NORMALSPLIT_',visible=True),
           sg.Input('',size=(7,7),key='_INPUT_NORMALSPLIT_',visible=True,disabled=False)],
          [sg.Radio('Custom Split','SplitType',enable_events=True, key='_RB2_CS_')],
          [sg.Text('Choose output file(s) destination folder :')],
          [sg.Input(key='_INPUT_CUSTSPLIT_OUTFOLDER_',disabled=True), sg.FolderBrowse(key='_BTN_CUSTSPLIT_OUTFOLDER_',disabled=True)],
          [sg.Text('Custom Split items',key='_TXT_CUSTOMSPLIT_',visible=False)],
          [sg.Input(key='_INPUT_CUSTOMSPLIT_',visible=True,disabled=True)],
          [sg.Text('Error : ')],
          [sg.Input('',key='_INPUT_ERRORFIELD_',disabled=True)],
          [sg.Text('Status: '), sg.Input(disabled=True,key='_INPUT_PROGRESS_')],
          [sg.Button('Submit',key='_BTN_SUBMIT_',disabled=True), sg.Button('Clear',key='_BTN_CLEAR_'),
           sg.Button('Exit')]
          ]

window = sg.Window('CSV Splitter - VN',layout).Finalize()

while True:             # Event Loop
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    elif event == '_INPUT_FILEPATH_':
        print(values)
        fileName, extn = CSVSplitterFnFiles.fileCheck(values)
        window.FindElement('_INPUT_ERRORFIELD_').Update('')
        window.FindElement('_INPUT_ROWCOUNT_').Update('')
        window.FindElement('_INPUT_NORMALSPLIT_').Update(disabled=False)
        window.FindElement('_BTN_SUBMIT_').Update(disabled=False)
        window.FindElement('_BTN_ROWCOUNT_').Update(disabled=False)
        if extn not in ['CSV','csv']:
            window.FindElement('_INPUT_ERRORFIELD_').Update('Invalid File - Not a CSV')
            window.FindElement('_BTN_SUBMIT_').Update(disabled=True)
            window.FindElement('_BTN_ROWCOUNT_').Update(disabled=True)
            window.FindElement('_INPUT_NORMALSPLIT_').Update(disabled=True)
    elif event == '_BTN_ROWCOUNT_':
        rowCount = CSVSplitterFnFiles.rowCount(values)
        window.FindElement('_INPUT_ROWCOUNT_').Update(rowCount)
        
    elif event == '_RB1_NS_':
        window.FindElement('_INPUT_NORMALSPLIT_').Update(disabled=False)
        window.FindElement('_INPUT_CUSTOMSPLIT_').Update(disabled=True)
        window.FindElement('_INPUT_CUSTSPLIT_OUTFOLDER_').Update(disabled=True)
        window.FindElement('_BTN_CUSTSPLIT_OUTFOLDER_').Update(disabled=True)
        
    elif event == '_RB2_CS_':
        window.FindElement('_INPUT_NORMALSPLIT_').Update('')
        window.FindElement('_INPUT_NORMALSPLIT_').Update(disabled=True)
        window.FindElement('_INPUT_CUSTOMSPLIT_').Update(disabled=False)
        window.FindElement('_INPUT_CUSTSPLIT_OUTFOLDER_').Update(disabled=False)
        window.FindElement('_BTN_CUSTSPLIT_OUTFOLDER_').Update(disabled=False)
        
    elif event == '_BTN_SUBMIT_':
        window.FindElement('_BTN_SUBMIT_').Update(disabled=True)
        window.FindElement('_INPUT_PROGRESS_').Update('Please Wait, Splitting is In-progress....')
        status = CSVSplitterFnFiles.fileSplit(values)
        print(event,values)
        if status == 'Completed':
            window.FindElement('_INPUT_PROGRESS_').Update('Splitting Completed!!')
            sg.Popup("Done", "CSV Splitting completed successfully.")
            break
        
    elif event == '_BTN_CLEAR_':
        #window['_INPUT_ROWCOUNT_']('')
        print(event,values)
        window.FindElement('_INPUT_ROWCOUNT_').Update('')
        window.FindElement('_INPUT_FILEPATH_').Update('')
        window.FindElement('_INPUT_NORMALSPLIT_').Update('')
        window.FindElement('_INPUT_ERRORFIELD_').Update('')
        window.FindElement('_INPUT_CUSTSPLIT_OUTFOLDER_').Update('')
        window.FindElement('_INPUT_PROGRESS_').Update('')
        window.FindElement('_CHK_INCHEADER_').Update(True)
        

#print(event,values)
window.Close()




