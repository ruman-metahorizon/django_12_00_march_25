from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post

from .forms import NewTopicForm, PostForm

from django.contrib.auth.decorators import login_required

def home(request):
    boards = Board.objects.all()
    # boards_names = []

    # for board in boards:
    #     boards_names.append(board.name)

    # response_html = '<br>'.join(boards_names)

    # return HttpResponse(response_html)
    return render(request, 'home.html', {'boards': boards})

def about(request):
    # do something...
    return render(request, 'about.html')

def board_topics(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})


def question(request, pk):
    return HttpResponse(f"Question : {pk}")

def post(request, slug):
    return HttpResponse(f"Slug : {slug}")

def blog_post(request, slug, pk):
    return HttpResponse(f"Blog_post : {slug} and PK : {pk}")

def user_profile(request, username):
    return HttpResponse(f"User Name : {username}")

def year_archive(request, year):
    return HttpResponse(f"Year: {year}")

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)  
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})



def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    return render(request, 'topic_posts.html', {'topic': topic})


@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})