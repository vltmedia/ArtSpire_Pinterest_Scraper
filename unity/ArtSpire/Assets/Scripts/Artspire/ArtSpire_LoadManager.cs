using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;

public class ArtSpire_LoadManager : MonoBehaviour
{
    public string SavedCacheLoc;
    public List<string> FoundFiles = new List<string>();
    public List<ArtSpire_LoadItem> ArtSpire_LoadItems = new List<ArtSpire_LoadItem>();
    public List<GameObject> LoadedItemsObjects = new List<GameObject>();
    public GameObject LoadHolder;
    public GameObject LoadItemPrefab;

    public static ArtSpire_LoadManager Instance;

    public void Awake()
    {
        Instance = this;
    }
    // Start is called before the first frame update
    void Start()
    {
         SavedCacheLoc = Application.dataPath + "/SavedCache/";
        RefreshLoadList();



    }
    public void RefreshLoadList()
    {
        if (LoadedItemsObjects.Count != 0)
        {

            foreach(var go in LoadedItemsObjects)
            {
                try
                {
                    Destroy(go);
                }
                catch
                {

                }
            }
            LoadedItemsObjects.Clear();
            FoundFiles.Clear();
        }
        foreach (var file in System.IO.Directory.GetFiles(SavedCacheLoc))
        {
            if (!System.IO.Path.GetExtension(file).Contains("meta"))
            {
                FoundFiles.Add(file);
                var returnedjs = LoadParsedJSON(file);
                ArtSpire_LoadItems.Add(returnedjs);

                GameObject newobj = Instantiate(LoadItemPrefab, LoadHolder.transform);
                var loadcard = newobj.GetComponent<ArtSpire_LoadCard>();
                loadcard.LoadItem = returnedjs;
                loadcard.Filepath = file;
                loadcard.InitializeItem();
                LoadedItemsObjects.Add(newobj);

            }

        }
    }
    public ArtSpire_LoadItem LoadParsedJSON(string filepath)
    {
        var jsonString = File.ReadAllText(filepath);
        ArtSpire_LoadItem loaditem = new ArtSpire_LoadItem();
        loaditem = JsonUtility.FromJson<ArtSpire_LoadItem>(jsonString);
        return loaditem;

    }
    // Update is called once per frame
    void Update()
    {
        
    }
}
