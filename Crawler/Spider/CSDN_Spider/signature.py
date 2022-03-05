import execjs

"bK9jk5dBEtjauy6gXL7vZCPJ1fOy076H"
203899271
nonce_func = execjs.compile("""
p = function(e) {
        var t = e || null;
        return null == t && (t = "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (function(e) {
            var t = 16 * Math.random() | 0;
            return ("x" === e ? t : 3 & t | 8).toString(16)
        }
        ))),
        t
    }
""")

print(nonce_func.call("p",))