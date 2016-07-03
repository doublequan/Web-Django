from django.core.urlresolvers import reverse
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils import timezone
from models import Question, Choice
from django.views import generic


# Create your views here.

class IndexView(generic.ListView):
    context_object_name = 'question_list'
    model = Question
    template_name = 'polls/question_list.html'
    paginate_by = 50

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


def calculator(request):
    return render(request, 'cal/calculator.html')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/question_detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/question_results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Increase the question's votes by 1 using F() which is a SQL operation
        selected_choice = question.choice_set.filter(pk=request.POST['choice'])
        selected_choice.update(votes=F('votes') + 1)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'polls/question_detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def admin(request):
    if request.method == 'POST':
        if 'question_text' in request.POST and 'choice1' in request.POST:
            q = Question(question_text=request.POST['question_text'], pub_date=timezone.now())
            q.save()
            c1 = Choice(question=q, choice_text=request.POST['choice1'])
            c1.save()

    return render(request, 'polls/admin.html', {})

def question_list_json(request):
    response = {}
    qs = Question.objects.all()
    for q in qs:
        response[q.id] = q.question_text
        # print q.question_text, q.pub_date

    return JsonResponse(response)