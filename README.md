# GrimDawn_DB_to_CSV_Extractor
Just a tool to convert Grim Dawn items in a database to a csv for further editing.


To use this tool, you need to first extract the packed Grim Dawn database into its individual records.
The tool for doing this, "AssetManager.exe" come installed with Grim Dawn and is located in the same folder as the game itself.
ex. X:\Steam\SteamApps\common\Grim Dawn

# AssetManager.exe Super Quick Tutorial

## Open AssetManager.exe, on the first prompt choose "Work Offline"
![image](https://user-images.githubusercontent.com/10130237/163330748-6371a246-f81f-4b3a-a558-3833d4bc08f1.png)
(Unless you work for Crate Entertainment, then you should login to your source/asset control system)


## Go to the menu, Tools -> Options
 - Working Directory: Where you want the Grim Dawn database extracted to
 - Build Directory: Not used for this, pick another folder but we wont use it.
 - Tools Directory: The game folder where all the exe including the AssetManager.exe is located.

![image](https://user-images.githubusercontent.com/10130237/163331934-00a4b4d4-a22c-4aa1-b1e0-d36a5dadcc6a.png)

## Go to the menu, Tools -> Extract Game Files
  - Browse for the folder containing the game files, this is usually the same folder as the "Tools Directory"
  - Click ok, and then wait about 10-20 minutes for the files to extract.

This will create a folder structure containing many folders and ".dbr" (Database Record Files) in your working directory.
These .dbr files are what this project works on, and that concludes the "AssetManager.exe Tutorial"

---

# How To Use GrimDawn_DB_to_CSV_Extractor






