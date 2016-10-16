#-----------------------------------------------------------------------
#	bihin アプリケーションのviews
#
#	2016.09.xx	V0.01	Yoshimitsu.Nakazawa
#				Djangoの勉強のために作成。
#	YYYY.MM.DD	Vx.xx	XXXX
#				XXXXXXXXXXXXXXXXXXXXXXX
#
#-----------------------------------------------------------------------
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from bihin.models import Bihin
from bihin.forms import BihinForm

# Create your views here.

#-----------------------------------------------------------------------
#	index：
#   urls.py の index からここが起動される.
#   ここでは備品DBを取得し、bihin.htmlを動かす.
#-----------------------------------------------------------------------
@login_required
def index(request):
    #return HttpResponse("Bihin Top.")
    #return render(request, 'bihin/bihin.html')
    bihins = Bihin.objects.all().order_by('id')
    #return render(request, 'bihin/bihin.html', {'bihins':bihins})
    return render(request, 'bihin/bihin.html', {'bihins':bihins, 'user':request.user})

#-----------------------------------------------------------------------
#	bihin_edit：
#   urls.py の bihin_edit からここが起動される.
#   ここでは備品DBを取得し、bihin.htmlを動かす.
#-----------------------------------------------------------------------
@login_required
def bihin_edit(request, bihin_id=None):
    #return HttpResponse("Bihin Top.")
    print ( u"Debug:bihin_edit(bihin_id)", bihin_id )

    """備品の登録・編集"""
    if bihin_id:
        bihin = get_object_or_404(Bihin, pk=bihin_id)
    else:
        bihin = Bihin()

    print ( u"Debug:bihin_edit(001)" )

    if request.method == 'POST':
        form = BihinForm(request.POST, instance=bihin)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            bihin = form.save(commit=False)
            bihin.save()
            return redirect('bihin:index')
    else:    # GET の時
        form = BihinForm(instance=bihin)   # bihin インスタンスからフォームを作成
	    #return HttpResponse("Bihin Top.")

    print ( u"Debug:bihin_edit(002)" )

    d = {
        'form':form,
        'bihin_id':bihin_id,
        #'bihin_no':bihin.bihin_no,
        #'bihin_type':bihin.bihin_type,
        #'bihin_manufct':bihin.bihin_manufct,
        #'bihin_name':bihin.bihin_name,
        #'bihin_shisan':bihin.bihin_shisan,
        #'bihin_date':bihin.bihin_date,
        #'bihin_sts':bihin.bihin_sts,
        'bihin':bihin,
    }

    #return render(request, 'bihin/bihin_edit.html', dict(form=form, bihin_id=bihin_id))
    return render(request, 'bihin/bihin_edit.html', d)

