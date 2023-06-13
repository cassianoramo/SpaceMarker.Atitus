import cx_Freeze
executables =[
    cx_Freeze.Executable(script = "main.py", icon="nave.ico")
]
cx_Freeze.setup(
    name = "Space Marker",
    options={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["BG.bmp",
                            "icon.bmp",
                            "RegistroDeEstrelas.txt",
                            "Interstellar.mp3"]
        }
    }, executables = executables
)
