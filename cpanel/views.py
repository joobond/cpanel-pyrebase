from django.shortcuts import render
import pyrebase

config = {
    'apiKey': "AIzaSyDg-AD8p3MTB3GhmLqupSO6TKrNqXun8TI",
    'authDomain': "to-de-dieta.firebaseapp.com",
    'databaseURL': "https://to-de-dieta.firebaseio.com",
    'projectId': "to-de-dieta",
    'storageBucket': "to-de-dieta.appspot.com",
    'messagingSenderId': "1053641145914",
    'appId': "1:1053641145914:web:dd47dc648cd5bc11"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
db = firebase.database()

def singIn(request):
    return render(request, "login.html")

def cadastrarPaciente(request):
    return render(request, "cadastrarPaciente.html")

def dadosPaciente(request):
    email = request.POST.get('email')
    idade = request.POST.get('idade')
    nivel = request.POST.get('nivel')
    nome = request.POST.get('nome')
    peso = request.POST.get('peso')
    telefone = request.POST.get('telefone')
    
    data = {"email": email, "idade":idade, "nivel":nivel, "nome":nome, "peso":peso, "telefone":telefone}
    try:
        db.child("pacientes").push(data)
    except:
        message = "Deu erro"
        return render(request,"cadastrarPaciente.html",{"msg":message})
    return render(request, "welcome.html", {"e":email})

def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request,"signIn.html",{"msg":message})
    print(user)
    return render(request, "welcome.html",{"e":email})