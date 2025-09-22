import clr
from pathlib import Path

# Load DLLs
scriptDir = Path(__file__).parent.parent.as_posix() + r'/DLLs'
#scriptDir = os.getcwd() + r'\src\silentpartner\DLLs'
# This dll contains the classes in which the data is stored
clr.AddReference(scriptDir + r'/PalmSens.Core.dll')
# This dll is used to load your session file
clr.AddReference(scriptDir + r'/PalmSens.Core.Windows.dll')