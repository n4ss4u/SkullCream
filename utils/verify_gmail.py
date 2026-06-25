import mechanize

def verify_gmail(email):

    navegador = mechanize.Browser()
    navegador.open("https://accounts.google.com/signin/v2/identifier")
    navegador.select_form(nr=0)
    navegador["identifier"] = email
    respuesta = navegador.submit()

    if "rejected" in respuesta.geturl():
        return True
    else:
        return False