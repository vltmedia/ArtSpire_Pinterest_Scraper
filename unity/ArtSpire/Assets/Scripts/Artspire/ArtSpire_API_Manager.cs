using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Text;
using TMPro;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class RandomGenerator
{
    // Instantiate random number generator.  
    // It is better to keep a single Random instance 
    // and keep using Next on the same instance.  
    private readonly System.Random _random = new System.Random();

    // Generates a random number within a range.      
    public int RandomNumber(int min, int max)
    {
        return _random.Next(min, max);
    }

    // Generates a random string with a given size.    
    public string RandomString(int size, bool lowerCase = false)
    {
        var builder = new StringBuilder(size);

        // Unicode/ASCII Letters are divided into two blocks
        // (Letters 65–90 / 97–122):   
        // The first group containing the uppercase letters and
        // the second group containing the lowercase.  

        // char is a single Unicode character  
        char offset = lowerCase ? 'a' : 'A';
        const int lettersOffset = 26; // A...Z or a..z: length = 26  

        for (var i = 0; i < size; i++)
        {
            var @char = (char)_random.Next(offset, offset + lettersOffset);
            builder.Append(@char);
        }

        return lowerCase ? builder.ToString().ToLower() : builder.ToString();
    }

    // Generates a random password.  
    // 4-LowerCase + 4-Digits + 2-UpperCase  
    public string RandomPassword()
    {
        var passwordBuilder = new StringBuilder();

        // 4-Letters lower case   
        passwordBuilder.Append(RandomString(4, true));

        // 4-Digits between 1000 and 9999  
        passwordBuilder.Append(RandomNumber(1000, 9999));

        // 2-Letters upper case  
        passwordBuilder.Append(RandomString(2));
        return passwordBuilder.ToString();
    }
}
public class ArtSpire_API_Manager : MonoBehaviour
{
    [Header("Set if needed")]
    public string APIExeFile = "ScrapePinterestSelenium.exe";
    public string ChromeDriverFilePattern = "chromedriver*.exe";
    public string OutputParseFile = "parsedfile.json";
    public int PinsPerPage = 20;

    [Space(10)]
    [Header("Set UI")]
    public ArtSpire_PinCard MainPinCard;
    public TextMeshProUGUI PinsCount;
    public TextMeshProUGUI PageCounter;
    public TextMeshProUGUI LoadingText;
    public TMP_InputField URLField;
    public TMP_InputField ScrollCountField;
    public GameObject LoadingPanel;
    public TextMeshProUGUI StatusText;

    public Image SeleniumLocated;
    public Image ChromeDriverLocated;


    [Space(10)]
    [Header("Debug Info")]

    public string ChromeDriverFilePath = "";
    public string APIExeFilePath = "";
    public string OutputParseFilePath = "";
    public int CurrentPage = 0;
    public int CurrentPageMinPin = 0;
    public int CurrentPageMaxPin = 0;
    public int CurrentPageMax = 0;
    public ArtSpire_API_Pins LoadedPins;
    public List<ArtSpire_PinCardHolder> PinCardHolders = new List<ArtSpire_PinCardHolder>();


    // Start is called before the first frame update
    public static ArtSpire_API_Manager Instance;

    private void Awake()
    {
        Instance = this;
    }

    public void NextPage()
    {
        var nextpage = CurrentPage + 1;

        //if (CurrentPageMaxPin > LoadedPins.Pins.Length)
        if (nextpage > CurrentPageMax)
        {
             nextpage = 0;

        }

        CurrentPageMinPin = nextpage * PinsPerPage;
        CurrentPageMaxPin = CurrentPageMinPin + 20;
        CurrentPage = nextpage;
        UpdatePageInfo();
        InitializeHolders();
    }
    public void UpdatePageInfo()
    {
        PageCounter.text = (CurrentPage + 1) + " / " + (CurrentPageMax + 1);
        PinsCount.text = CurrentPageMinPin.ToString() + " : " + LoadedPins.Pins.Length;

    }
    public void PrevPage()
    {
        var nextpage = CurrentPage - 1;

        if (nextpage < 0)
        {
             nextpage = CurrentPageMax;

        }

        CurrentPageMinPin = nextpage * PinsPerPage;
        CurrentPageMaxPin = CurrentPageMinPin + 20;
        CurrentPage = nextpage;
        UpdatePageInfo();
        InitializeHolders();
    }
    public void WritePNG(ArtSpire_PinCard Pin, bool batchmode)
    {
        
        //first Make sure you're using RGB24 as your texture format
        Texture2D texture = (Texture2D)Pin.PinImage.texture;

        //then Save To Disk as PNG
        byte[] bytes = texture.EncodeToPNG();
   
        RandomGenerator randomGenerator = new RandomGenerator();
        var dirPath = Application.dataPath + "/SaveImages/";

        var datepath = dirPath + System.DateTime.Now.ToString("yyyyMMdd") + "/";
        if (!Directory.Exists(dirPath))
        {
            Directory.CreateDirectory(dirPath);
        }
        if (!Directory.Exists(datepath))
        {
            Directory.CreateDirectory(datepath);
        }
        var filepath = datepath + randomGenerator.RandomPassword()+ System.DateTime.Now.ToString("yyyyMMddhhmmss") + ".png";
        File.WriteAllBytes(filepath, bytes);

        if(batchmode == false)
        {
            StartCoroutine(ShowMenuTime("SAVED PNG TO : " + filepath, 2));
        }
    }

    IEnumerator WriteAllPinsToPNG()
    {
        var currentcountt = 0;
        LoadingPanel.SetActive(true);
        LoadingText.text = "SAVING " + LoadedPins.Pins.Length.ToString() + " Pins... At | 0%";

        yield return new WaitForSeconds(0.8f);
        foreach (var pinn in LoadedPins.Pins)
        {
            var newcount = currentcountt + 1;
            currentcountt = newcount;
            var percentage = Mathf.RoundToInt((currentcountt / LoadedPins.Pins.Length) * 100).ToString() + "%";
        UnityWebRequest www = UnityWebRequestTexture.GetTexture(pinn.URL);
        yield return www.SendWebRequest();

        Texture myTexture = DownloadHandlerTexture.GetContent(www);
 
        //first Make sure you're using RGB24 as your texture format
        Texture2D texture = (Texture2D)myTexture;

        //then Save To Disk as PNG
        byte[] bytes = texture.EncodeToPNG();
            var dirPath = Application.dataPath + "/SaveImages/";

            var datepath = dirPath + System.DateTime.Now.ToString("yyyyMMdd") + "/";
        if (!Directory.Exists(dirPath))
        {
            Directory.CreateDirectory(dirPath);
        }
        if (!Directory.Exists(datepath))
        {
            Directory.CreateDirectory(datepath);
        }
        RandomGenerator randomGenerator = new RandomGenerator();
        var filepath = datepath + randomGenerator.RandomPassword() + System.DateTime.Now.ToString("yyyyMMddhhmmss") + ".png";
        File.WriteAllBytes(filepath, bytes);
            LoadingText.text = "SAVING " + LoadedPins.Pins.Length.ToString() + " Pins... At | " + percentage;

        }
        StartCoroutine(ShowMenuTime("Saved all the " + LoadedPins.Pins.Length.ToString() + " Images." , 3));



    }

    public void SaveAllImagesOnPage()
    {
        foreach(var pincard in PinCardHolders)
        {
            pincard.SaveAllImagesOnPage();
        }
        StartCoroutine(ShowMenuTime("Saved all the Images for Page " + CurrentPage.ToString(), 3));
    }
    void Start()
    {
        try
        {
            ChromeDriverFilePath = Directory.GetFiles(Application.dataPath, ChromeDriverFilePattern, SearchOption.TopDirectoryOnly)[0];
            APIExeFilePath = Application.dataPath + "/" + APIExeFile;
            OutputParseFilePath = Application.dataPath + "/" + OutputParseFile;

        }
        catch
        {

        }

            StatusText.text = "API : " + APIExeFilePath + " | ChromeDriver : " + ChromeDriverFilePath + " | AppPath : " + Application.dataPath;

        //Debug.Log(File.Exists(path)); 
        ////Debug.Log(File.Exists(filess[0]));

    }
    public IEnumerator ShowLoadingMenuRunProcess(string Arguments,string message)
    {
        LoadingText.text = message;
        LoadingPanel.SetActive(true);

        yield return new WaitForSeconds(0.4f);
        RunProcess(Arguments);

    }
    public IEnumerator ShowMenuTime(string message, float upTime)
    {
        LoadingText.text = message;
        LoadingPanel.SetActive(true);

        yield return new WaitForSeconds(upTime);
        LoadingPanel.SetActive(false);

    }
    public void RunProcess(string arg)
    {
        var argg = "\"" + APIExeFilePath + "\" "+ arg;
        //var arg = "\"" + APIExeFilePath + "\" https://www.pinterest.com/justin_jaro/character-design/ 3 \"" + OutputParseFilePath + "\" batch board \"" + ChromeDriverFilePath + "\"";
        UnityEngine.Debug.Log("Starting!");
        Process p = new Process
        {

            StartInfo = new ProcessStartInfo
            {
                FileName = APIExeFilePath,
                Arguments = arg,
                //Arguments = "https://www.pinterest.com/justin_jaro/character-design/ 3 \"" + OutputParseFilePath + "\" batch board \"" + ChromeDriverFilePath+ "\"",
                WindowStyle = ProcessWindowStyle.Normal
                //startInfo.Arguments = "MyArgument";
                //UseShellExecute = true
                //RedirectStandardOutput = true
            }
        };
        p.Start();

        //UnityEngine.Debug.Log(p.StandardOutput.ReadToEnd());
        p.WaitForExit();
        UnityEngine.Debug.Log("Finished!");
        UnityEngine.Debug.Log(argg);
        LoadParsedJSON();
        LoadingPanel.SetActive(false);
        
    }

    public void LoadParsedJSON()
    {
        var jsonString = File.ReadAllText(OutputParseFilePath);
        LoadedPins = JsonUtility.FromJson<ArtSpire_API_Pins>(jsonString);
        CurrentPageMax = Mathf.RoundToInt(LoadedPins.Pins.Length / 20) - 1;
        UpdatePageInfo();
        InitializeHolders();

    }

    public void InitializeHolders()
    {
        foreach (var holder in PinCardHolders)
        {
            holder.InitializePins();
        }
    }
    public void RunRefresh()
    {
        var boardmode = "board";
        var urll = URLField.text;
        if (!URLField.text.Contains(".com"))
        {
            urll = "https://www.pinterest.com/search/pins/?q=" + URLField.text.Replace(" ", "%20") + "&rs=typed&term_meta[]=" + URLField.text.Replace(" ", "%20") + "%7Ctyped";
            boardmode = "search";
        }
        var Arguments = urll + " "+ ScrollCountField.text+ " \"" + OutputParseFilePath + "\" batch "+ boardmode + " \"" + ChromeDriverFilePath + "\"";
        StartCoroutine(ShowLoadingMenuRunProcess(Arguments, "LOADING PLEASE WAIT..."));


    }
    public void SaveAllImages()
    {
        StartCoroutine(WriteAllPinsToPNG());
    }
    public void OpenPin(ArtSpire_PinCard currentcard)
    {
        MainPinCard.Pin = currentcard.Pin;
        MainPinCard.InitializePin();
    }
    public void LoadBoard(string url)
    {



    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.PageUp))
        {
            RunRefresh();
        }
        if (Input.GetKeyDown(KeyCode.End))
        {
            LoadParsedJSON();

        }
    }
}
