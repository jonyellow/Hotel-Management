import datetime

from django.shortcuts import render
from .models import *


#主页
def index(request):
    # hotel = Hotel.objects.filter(name='Hotel')[0]
    # description = hotel.description
    return render(request, 'index.html', locals())

def about(request):
    title = 'Hotel'
    hotel = Hotel.objects.get(name='Hotel')
    name = hotel.name
    description = hotel.description
    address = hotel.address
    return render(request, 'about.html', {'title':title, 'name':name, 'description':description, 'address':address})

#预定
def order(request):
    return render(request, 'order.html')

#预定结果
def orderResult(request):
    tempCustomer=Customer()
    tempCustomer.tel= request.GET['tel']
    tempCustomer.name= request.GET['name']
    tempCustomer.cardid= request.GET['cardid']
    tempCustomer.save()
    tempOrder=Order()
    tempOrder.name = request.GET['name']
    tempOrder.tel = request.GET['tel']
    tempOrder.cardid = request.GET['cardid']
    tempOrder.roomtype = request.GET['roomtype']
    begin = request.GET['begin']
    end = request.GET['end']
    tempOrder.begin = (datetime.datetime.strptime(begin , '%Y-%m-%d')).date()
    tempOrder.end = (datetime.datetime.strptime(end , '%Y-%m-%d')).date()
    period = (tempOrder.end - tempOrder.begin).days
    price = 0
    if tempOrder.roomtype == 'standard':
        price = (RoomInfo.objects.get(name='标准间')).price

    elif tempOrder.roomtype =='better':
        price = (RoomInfo.objects.get(name='豪华间')).price

    elif tempOrder.roomtype =='president':
        price = (RoomInfo.objects.get(name='总统间')).price
    tempOrder.totalprice = period * price
    tempOrder.save()
    tel = request.GET['tel']
    begin = request.GET['begin']
    return render(request, 'orderresult.html', {'orderid':tempOrder.id})

def roomInfo(request):
    roomInfoList = RoomInfo.objects.all()
    return render(request, 'roominfo.html', {'roomInfoList':roomInfoList})
