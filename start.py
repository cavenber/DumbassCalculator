
###### PROGRAM START ######

title = r"""
··········································
   ___             __                     
  / _ \__ ____ _  / /  ___ ____ ___       
 / // / // /  ' \/ _ \/ _ `(_-<(_-<       
/____/\_,_/_/_/_/_.__/\_,_/___/___/       
  _____     __         __     __          
 / ___/__ _/ /_____ __/ /__ _/ /____  ____
/ /__/ _ `/ / __/ // / / _ `/ __/ _ \/ __/
\___/\_,_/_/\__/\_,_/_/\_,_/\__/\___/_/   
··········································
"""
version = "version 14.1.1"
fillin = r"""
·
:
:
:
:
:
:
:
:
·
"""
if __name__ == "__main__":
    import json
    import math
    from dependencies.main import start
    with open("dependencies/settings.json", "r") as f:
        settings = json.load(f)
    fillinAmount = (settings["line_size"] - 42) / 2
    fillinAmount1 = math.ceil(fillinAmount)
    fillinAmount2 = math.floor(fillinAmount)
    titlePrint = title.splitlines()
    fillinPrint = fillin.splitlines()
    for fillinPrint, titlePrint, fillinPrint in zip(fillinPrint, titlePrint, fillinPrint):
        print(fillinPrint * fillinAmount1 + titlePrint + fillinPrint * fillinAmount2)
    print(version)
    start()