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

var uid = c()
return  uid