# Crome datalog converter to Megalogviewer
This Python script converts Crome datalog files (csv) to Megalogviewer csv-friendly datalog files
It replaces double quotes, as well as the file header. It also convert imperial to metric units

![Crome datalog example using Megalogviewer](https://github.com/reynico/crome-megalogviewer-converter/example.png)

### Steps
- Open a .dlf datalog with Crome
- Save it as .csv datalog
- Run converter.py my-datalog.csv
- Open the newly created edited-my-datalog.csv with Megalogviewer
