from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Pessoas, Estados
from .forms import PessoasForm
from dal import autocomplete
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q


class PessoasCreateView(CreateView):
    model = Pessoas  # Define o modelo usado pela CreateView
    form_class = PessoasForm  # Usa o formulário personalizado
    template_name = 'pessoas_form.html'  # Nome do template a ser renderizado
    success_url = reverse_lazy('pessoas_list')  # Redireciona após o sucesso



class EstadosAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Certifique-se de que o usuário esteja autenticado (se necessário)
       
        qs = Estados.objects.all()
        print(self.term)
        if self.q:  # `self.q` contém o termo digitado pelo usuário
            qs = qs.filter(name__icontains=self.q)  # Busca pelo nome do estado

        return qs

def home(request):
    form = PessoasForm()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Verifica se é uma requisição AJAX
        term = request.GET.get('q')
        estados = Estados.objects.filter(Q(name__icontains=term)|Q(uf__icontains=term) )
        response_content = list(estados.values())
        print(response_content)
        return JsonResponse(response_content, safe=False)
    
    return render(request, 'pessoas_form.html', {'form': form})
