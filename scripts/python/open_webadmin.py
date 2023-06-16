import webbrowser

url = ""
edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

#using edge because wedadmin doesn't like firefox for me for whatever reason
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
webbrowser.get('edge').open(url)
