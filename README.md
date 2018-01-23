# Crome datalog converter to Megalogviewer
This Python script converts Crome datalog files (csv) to Megalogviewer csv-friendly datalog files
It replaces double quotes, as well as the file header. It also convert imperial to metric units

![Crome datalog example using Megalogviewer](https://github.com/reynico/crome-megalogviewer-converter/raw/master/example.png)

### Steps
- Open a `.dlf` datalog with Crome
- Save it as `.csv` datalog
- Run `converter.py my-datalog.csv`
- Open the newly created `edited-my-datalog.csv` with Megalogviewer

### Make a Windows executable package
- Install Python for Windows [Python for Windows](https://www.python.org/download/releases/2.7/)
- Install pyinstaller `pip install pyinstaller`
- Run `pyinstaller gui.py`
- Set the PATH for the gui executable [Example at Stackoverflow](https://stackoverflow.com/a/9546345)
- Use [Context menu editor](http://www.thewindowsclub.com/context-menu-editor-for-windows-7-vista-released) to add an entry to the context menu 

![Windows context menu example](https://github.com/reynico/crome-megalogviewer-converter/raw/master/windows-context-menu.png)
