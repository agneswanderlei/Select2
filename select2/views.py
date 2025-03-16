from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Pessoas, Estados
from .forms import PessoasForm
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q


class PessoasCreateView(CreateView):
    model = Pessoas  # Define o modelo usado pela CreateView
    form_class = PessoasForm  # Usa o formulário personalizado
    template_name = 'pessoas_form.html'  # Nome do template a ser renderizado
    success_url = reverse_lazy('pessoas_create')  # Redireciona após o sucesso
    def dispatch(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Verifica se é uma requisição AJAX
            term = request.GET.get('q')
            estados = Estados.objects.filter(Q(name__icontains=term) | Q(uf__icontains=term))
            response_content = list(estados.values())
            return JsonResponse(response_content, safe=False)
        return super().dispatch(request, *args, **kwargs)


def home(request):
    form = PessoasForm()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # Verifica se é uma requisição AJAX
        term = request.GET.get('q')
        estados = Estados.objects.filter(Q(name__icontains=term)|Q(uf__icontains=term) )
        response_content = list(estados.values())
        print(response_content)
        return JsonResponse(response_content, safe=False)
    
    return render(request, 'pessoas_form.html', {'form': form})
