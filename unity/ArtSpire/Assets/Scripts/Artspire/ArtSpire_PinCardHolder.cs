using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ArtSpire_PinCardHolder : MonoBehaviour
{
    public int PageNumber = 0;
    public int MinPin = 0;
    public int MaxPin = 0;
    public ArtSpire_API_Pins PagePins;

    [Header("Set UI")]
    public List<ArtSpire_PinCard> PinObjects = new List<ArtSpire_PinCard>();

    //// Start is called before the first frame update
    //public static ArtSpire_PinCardHolder Instance;

    //private void Awake()
    //{
    //    Instance = this;
    //}

    public void SaveAllImagesOnPage()
    {
        foreach (var pincard in PinObjects)
        {
            pincard.WriteFile(true);
        }
    }
    public void InitializePins()
    {
        
        var thisc = PageNumber + 1;
         MinPin = ((thisc * 5) + 1) + ArtSpire_API_Manager.Instance.CurrentPageMinPin ;
        var rangemin = ((thisc * 5) + 1) + ArtSpire_API_Manager.Instance.CurrentPageMinPin ;
        MaxPin = (rangemin + 5) + ArtSpire_API_Manager.Instance.CurrentPageMinPin;
        var rangemax = (rangemin + 5) + ArtSpire_API_Manager.Instance.CurrentPageMinPin;
        List<ArtSpire_API_Pin> newpins = new List<ArtSpire_API_Pin>();
        for(int i = rangemin; i < rangemax; i++)
        {
            try
            {
                newpins.Add(ArtSpire_API_Manager.Instance.LoadedPins.Pins[i]);
            }
            catch
            {

                Debug.LogError("FAILED AT | newpins.Add(ArtSpire_API_Manager.Instance.LoadedPins.Pins[i]) | " + i.ToString());
            }
        }
        PagePins.Pins = newpins.ToArray();

        for (var pinn = 0; pinn < newpins.Count; pinn++)
        {
            //Debug.Log(pinn.ToString() + " | " + gameObject.name);
            //Debug.Log(pinn.ToString() + " | " + newpins[pinn].URL);
            try
            {
                //Debug.Log(pinn.ToString() + " | " + PinObjects[pinn].gameObject.name);
                PinObjects[pinn].Pin = newpins[pinn];
                PinObjects[pinn].InitializePin();
            }
            catch
            {
            }
            }
    }
    
    void Start()
    {
        ArtSpire_API_Manager.Instance.PinCardHolders.Add(this);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
