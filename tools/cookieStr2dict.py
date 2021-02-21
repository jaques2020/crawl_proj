
def Str2dict(cookies_String):
    cookies_String = cookies_String.split(';')
    dict_content = {}
    for i in cookies_String:
        i = i.split('=')
        dict_content[i[0]] = i[1]
    return dict_content
