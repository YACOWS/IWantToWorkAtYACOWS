# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, HttpResponse, redirect, get_object_or_404

def salvar(request, obj=None):

    if not obj == None:

        return render_to_response('index.html', locals() )

    else:

        return redirect('/')

