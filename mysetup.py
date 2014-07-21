# mysetup.py
from distutils.core import setup
import py2exe

setup(console=["SyncFlo_Update_Drill_Info.py"],
      data_files=[("",["app.ini"])],
)
