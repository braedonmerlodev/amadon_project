# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, "amadon/index.html")
def buy(request):
    if "spent" not in request.session:
        request.session["spent"]=0
    if "count" not in request.session:
        request.session["count"]=0
    products = {
        "1":19.99,
        "2":29.99,
        "3":4.99,
        "4":49.99
    }
    request.session["price"] = products[request.POST["product_id"]]*int(request.POST["quantity"])
    request.session["spent"] += request.session["price"]
    request.session["count"] += int(request.POST["quantity"])
    return redirect("/amadon/checkout")
def checkout(request):
    return render(request, "amadon/checkout.html")