from sys import executable
import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name="Jogo Space",
    opitions = {'build_exe': {'packages': ['pygame'],
                                'include_files':['assets']}},
    executables = executables
)