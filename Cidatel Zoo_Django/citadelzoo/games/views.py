from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import GameSession, Question
from .forms import StartForm
from .logic import generator_for

def home(request):
    return render(request, 'home.html')

def game_menu(request):
    return render(request, 'games/menu.html', {'form': StartForm()})

def start_game(request):
    if request.method != 'POST':
        return redirect('game_menu')
    form = StartForm(request.POST)
    if not form.is_valid():
        return render(request, 'games/menu.html', {'form': form})

    game_type = form.cleaned_data['game_type']
    level = form.cleaned_data['level']
    total = form.cleaned_data['total']

    session = GameSession.objects.create(
        user=request.user if request.user.is_authenticated else None,
        game_type=game_type,
        level=level,
        total=total
    )

    gen = generator_for(game_type)
    for prompt, answer in gen(level, n=total):
        Question.objects.create(session=session, prompt=prompt, answer=answer)

    return redirect('play', session_id=session.id, q_index=0)

def play(request, session_id, q_index):
    session = get_object_or_404(GameSession, id=session_id)
    questions = list(session.questions.all())
    if q_index >= len(questions):
        return redirect('result', session_id=session.id)
    q = questions[q_index]
    if request.method == 'POST':
        try:
            ans = int(request.POST.get('answer', ''))
        except ValueError:
            ans = None
        if ans is not None:
            q.user_answer = ans
            q.is_correct = (ans == q.answer)
            q.save()
            if q.is_correct:
                session.correct += 1
                session.save()
        return redirect('play', session_id=session.id, q_index=q_index+1)

    return render(request, 'games/play.html', {
        'session': session,
        'q': q,
        'q_index': q_index,
        'remaining': len(questions) - q_index
    })

def result(request, session_id):
    session = get_object_or_404(GameSession, id=session_id)
    from django.utils import timezone as tz
    session.finished_at = session.finished_at or tz.now()
    session.save()
    return render(request, 'games/result.html', {'session': session})

def scoreboard(request):
    top = GameSession.objects.order_by('-correct','-started_at')[:20]
    return render(request, 'games/scoreboard.html', {'top': top})
