using System.Collections;
using System.Collections.Generic;
using UnityEngine;
[System.Serializable]
public class ArtSpire_API_Argument : MonoBehaviour
{
    // "[API] [JSONTEMPLATE] [INT] [OUTPUT_JSONPATH] [BATCHMODE] [highresdump]  [CHROME_DRIVER] [OUTPUT_FOLDERPATH]
    public enum BoardMode {board, pin, highresdump };
    public enum BatchMode {batch, single };
    public string APIPath;
    public string JSONTemplate;
    public int ScrollAmmount;
    public string outputJSONPath;
    public BatchMode batchMode;
    public BoardMode boardMode;
    public string ChromeDriverPath;
    public string OutputFolderPath;



}
