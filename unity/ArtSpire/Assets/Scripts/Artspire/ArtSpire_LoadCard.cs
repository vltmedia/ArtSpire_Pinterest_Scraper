using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using TMPro;
[System.Serializable]
public class ArtSpire_LoadItem
{
    public ArtSpire_API_Pin[] Pins;
    public string URL;
    public int ScrollCount;
    public string BatchMode;


}
public class ArtSpire_LoadCard : MonoBehaviour
{
    public TextMeshProUGUI NameText;
    public TextMeshProUGUI PinsText;
    public TextMeshProUGUI TermText;
    public ArtSpire_LoadItem LoadItem;
    public string Filepath;

    public void InitializeItem()
    {
        PinsText.text = LoadItem.Pins.Length.ToString();
        TermText.text = LoadItem.URL;
        NameText.text = System.IO.Path.GetFileNameWithoutExtension(Filepath);
    }
    public void LoadLoadItem()
    {
        ArtSpire_API_Manager.Instance.LoadParsedJSON(Filepath);


    }
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
