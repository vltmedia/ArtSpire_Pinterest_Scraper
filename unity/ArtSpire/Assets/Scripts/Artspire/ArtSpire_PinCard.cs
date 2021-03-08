using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class ArtSpire_PinCard : MonoBehaviour
{

    [Header("Set UI")]
    public RawImage PinImage;
    public TextMeshProUGUI PinTitle;
    public TextMeshProUGUI PinCaption;


    [Space(10)]
    [Header("Debug Info")]
    public ArtSpire_API_Pin Pin;

    public bool Selected = false;

    IEnumerator GetTexture()
    {
        UnityWebRequest www = UnityWebRequestTexture.GetTexture(Pin.URL);
        yield return www.SendWebRequest();

        Texture myTexture = DownloadHandlerTexture.GetContent(www);
        PinImage.texture = myTexture;
    }
    public void InitializePin()
    {

        PinTitle.text = Pin.Title;
        PinCaption.text = Pin.Caption;
        StartCoroutine(GetTexture());
    }
    public void WriteFile(bool batchmode)
    {
        if (ArtSpire_API_Manager.Instance.HighresOutputToggle.isOn)
        {
            ArtSpire_API_Manager.Instance.SingleHRDownload(this.Pin);
        }
        else
        {


            ArtSpire_API_Manager.Instance.WritePNG(this, batchmode);
        }
    }

    public void OpenPinOnline()
    {
        Application.OpenURL(Pin.PinLink);
    }
    public void OpenPin()
    {
        ArtSpire_API_Manager.Instance.OpenPin(this);

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
