## ငါရေးချင်တာရေးတယ် 
## Evasion ကိုယ်ဖျောက်ချင်း ဟန်ဆောင်ချင်း
* ပုံမှန် အားဖြင့် ကိုယ် ဖျေက်မယ့် နည်းတေ များကြီးရှိ တယ် ပထမ တစ်ခုအနေနဲ့ base64
၁.payload ကို base64 encode လုပ်ပီးကိုယ် ဖျေက်မယ်ဆိုရင် backend မှာ decode ပြန် လုပ်တဲ့ function သုံးထား ရင် အဆင် ပြေတယ်.တကယ်လို့သုံးမထားဘူးဆို ရင် payload inject လုပ် တဲ့အခါ frontend မှာ ကိုယ်တိုင် ထည့်ပေးဖို့လိုလာတယ် . encode လုပ်  function တေ ကတော့ 
	* [].constructor.constructor("code")()
	* atob()
	* setTimeout("code") #all browsers
	* setInterval("code") #all browsers
	* setImmediate("code") #IE 10+
	* Function("code")() #all browsers
၂.URI အရှည် ကောက် သိလား မသိ ရင် ဖတ် Uniform (local and remote), Resource Identifier အောက်ကပုံကိုြကည့်ရင် ပိုသိသာမယ် 
![alt text](https://github.com/PiCarODD/oswe-prepare/blob/master/images/uri-vs-url-vs-urn.jpg). facebook ပေါ်မှာ pornhub link တေ တချို့ website တွေ ပို့မရတာ ကြုံဖူးတယ် မလား အဲ့ အခါ ချိဖ တို့ URL Shortening ကိုသုံးပီး ကျော် တယ် မလား အရင် က အဲ့ attack ကခေတ်စားခဲ့တယ် ခု တချို့နေရာတွေမာပဲသုံးလို့ရတော့ တယ်. နောက် တစ် နည်းက URL authority Obfuscation အဲ့ကောင် ကို နားလည် ဖိုက အောက် က ကောင် ကို ကြည့် 
```         
foo://example.com:8042/over/there?name=ferret#nose
\_/   \______________/\_________/ \_________/ \__/
|           |            |            |        |
scheme     authority       path        query   fragment
 |   _____________________|__
/ \ /                        \
urn:example:animal:ferret:nose
```
authority ကဘယ် လိုအလုပ် လုပ် လဲဆိုရင် userinfo @ host : port အဲ့လို သွားတယ် အဲ့ တာဆို ရင် https://www.google.com@EVIL.COM အဲ့မှာ ဆိုရင် evil.com ကကျနော် တို့ WEBSITE လို့ထားလိုက်။အဲ့မှာ www.google.com က userinfo အြဖစ် အလုပ် လုပ် သွားတယ် host ကတော့ evil.com.ရုပ်တရက် ကြည့်လိုက် ရင် google link လို့ထင် ရတယ် တကယ်တန်းတော့ maliciouse link ဖြစ်နေတယ်ဆိုတာ သိရ မယ်။
နောက်တစ်ခု က url ကို ip သုံးပီး ကိုယ်‌ေဖျာက် တာ website တိုင်းမှာ ip ရှိတယ် မလား.  216.58.215.78 ဒါက google ရဲ့ ip https://www.silisoftware.com/tools/ipconverter.php (DWORD) နဲ့‌ ပြောင်းပီးစမ်းြကည့်ကွာ လိ ပဲ‌ေရးရတာ လက်ညောင်းတယ်။
၃. 
