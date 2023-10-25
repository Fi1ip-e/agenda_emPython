from django.shortcuts import render
from .models import TbAgenda
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import AddContato

# Create your views here.
def HomePage(request):
    Agenda = TbAgenda.objects.all()

    valor = {
        'registros': Agenda
    }
    return render(request, 'myhome.html', valor)

def CadastroAgenda(request):
    
    if str(request.method) == 'POST':
        form = AddContato(request.POST or None)

        if form.is_valid():
            contato = form.save(commit=True)
        
        else:
            print('Erro a salvar')
    else:
        form = AddContato()
    valor = {
        'form': form
    }
    return render(request, 'addContato.html', valor)


def DeleteContato(request, contato_id):
    contatoDelete = get_object_or_404(TbAgenda, id=contato_id)
    contatoDelete.delete()
    

    return redirect('HomePage')