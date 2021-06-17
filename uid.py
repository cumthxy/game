from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

path = r'chromedriver_win32_v90\chromedriver.exe'
option = Options()
option.add_argument('--window-size=1332,700')
option.add_argument('--disable-infobars')
option.add_argument('incognito')
option.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=option, executable_path=path)
wait = WebDriverWait(driver, 10)


def get_text():
    script = ("""

        var n = "undefined" != typeof crypto && crypto.getRandomValues && crypto.getRandomValues.bind(crypto) || "undefined" != typeof msCrypto && "function" == typeof msCrypto.getRandomValues && msCrypto.getRandomValues.bind(msCrypto)
        , i = new Uint8Array(16);
    function a() {
        if (!n)
            throw new Error("crypto.getRandomValues() not supported. See https://github.com/uuidjs/uuid#getrandomvalues-not-supported");
        return n(i)
    }
    for (var o = [], s = 0; s < 256; ++s)
        o[s] = (s + 256).toString(16).substr(1);
    function l(t, e) {
        var r = e || 0
            , n = o;
        return [n[t[r++]], n[t[r++]], n[t[r++]], n[t[r++]], "-", n[t[r++]], n[t[r++]], "-", n[t[r++]], n[t[r++]], "-", n[t[r++]], n[t[r++]], "-", n[t[r++]], n[t[r++]], n[t[r++]], n[t[r++]], n[t[r++]], n[t[r++]]].join("")
    }
    var u = l;
    function c(t, e, r) {
        var n = e && r || 0;
        "string" == typeof t && (e = "binary" === t ? new Array(16) : null,
            t = null),
            t = t || {};
        var i = t.random || (t.rng || a)();
        if (i[6] = 15 & i[6] | 64,
            i[8] = 63 & i[8] | 128,
            e)
            for (var o = 0; o < 16; ++o)
                e[n + o] = i[o];
        return e || u(i)
    }
       var huang = c()
        return huang
    """)
    return script


with open('uid.js', 'r', encoding='utf-8') as f:
    jstext = f.read()

#result = driver .execute_script(jstext)  #两种方法都行
result=driver.execute_script(get_text())
print(result)
time.sleep(1)
driver .quit()