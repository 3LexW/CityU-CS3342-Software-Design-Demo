from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import shoppingCart, Product, shoppingCartHistory
from django.contrib import messages
from .forms import BirthdayForm
from dateutil.relativedelta import relativedelta
from datetime import date

# Create your views here.
def dashboard(request):
    cartID = request.session.get('cartID')
    if cartID is None:
        cart = shoppingCart()
        cart.save()
        request.session['cartID'] = cart.id
    itemlist, total = readCart(request)
    try:
        del (request.session['itemPending'])
    except:
        pass
    return render(request, 'terminal/dashboard.html', {
        "itemlist": itemlist,
        "total": round(total, 2),
    })

def addItemText(request):
    try:
        item_lookup = request.POST.get("itemtext").strip()
        try: 
            item = Product.objects.get(name__icontains = item_lookup)
            if item.age_resticted == False:
                addLog(request, item)
                messages.info(request, '%s is added to your cart.' % item_lookup)
                return redirect('../')
            elif item.age_resticted == True :
                request.session['itemPending'] = item.name
                if request.session.get('birthday_year') is None:
                    messages.info(request, 'Item %s requires age check.' % item.name)
                return redirect('../ageCheck')
        except:
            messages.info(request, 'Item %s not found.' % item_lookup)
            return redirect('../')
    except:
        item_lookup = request.session.get('itemPending').strip()
        item = Product.objects.get(name__icontains = item_lookup)
        addLog(request, item)
        messages.info(request, '%s is added to your cart' % item_lookup)
        return redirect('../')

def addLog(request, item):
    log = shoppingCartHistory()
    cartID = request.session.get('cartID')
    log.shoppingCart = shoppingCart.objects.get(id = cartID)
    log.item = item
    log.action = "Add"
    log.activate = True
    log.save()

def cancelCart(request):
    cartID = request.session.get('cartID')
    cart = shoppingCart.objects.get(id = cartID)
    cart.delete()
    messages.info(request, 'Cart cleared.')
    try:
        del request.session['cartID']
        del request.session['birthday_year']
        del request.session['birthday_month']
        del request.session['birthday_day']
    except:
        pass
    return redirect('../')

def readCart(request):
    cartID = request.session.get('cartID')
    cart = shoppingCart.objects.get(id = cartID)
    records = shoppingCartHistory.objects.filter(shoppingCart = cart)
    itemlist = []
    total = 0
    for record in records:
        if record.action == 'Add':
            itemlist.append(record.item)
            total += record.item.price
        if record.action == 'Delete':
            remove_index = itemlist.index(record.item)
            del itemlist[remove_index]
            total -= record.item.price
    return itemlist, total

def deleteItem(request):
    log = shoppingCartHistory()
    cartID = request.session.get('cartID')
    log.shoppingCart = shoppingCart.objects.get(id = cartID)
    item_lookup = request.POST.get("itemtext").strip()
    log.item = Product.objects.get(name = item_lookup)
    log.action = "Delete"
    log.activate = True
    log.save()
    messages.info(request, 'Item removed.')
    return redirect('../')

def ageCheck(request):
    if request.session.get('birthday_year') is None:    
        return render(request, 'terminal/ageCheck.html', {
            'BirthdayForm': BirthdayForm,
        })
    else:
        return verifyAge(request)

def verifyAge(request):
    pass_date = date.today() - relativedelta(years=18)
    year = request.session.get('birthday_year')
    if year is None:
        year = int(request.POST.get('birthday_year'))
        month = int(request.POST.get('birthday_month'))
        day = int(request.POST.get('birthday_day'))
    else:
        year = request.session.get('birthday_year')
        month = request.session.get('birthday_month')
        day = request.session.get('birthday_day')
    
    birthday = date(year, month, day)
    
    request.session['birthday_year'] = year
    request.session['birthday_month'] = month
    request.session['birthday_day'] = day

    if birthday <= pass_date:
        return redirect('../additem_text')
    else:
        messages.info(request, 'Your age is lower than 18, purchasing of %s is not permitted.' % request.session['itemPending'].lower())
        return redirect('..')

def addItemScan(request):
    try:
        item_lookup = request.POST.get("itemscan").strip()
        try: 
            item = Product.objects.get(barcode__icontains = item_lookup)
            item_lookup = item.name
            if item.age_resticted == False:
                addLog(request, item)
                messages.info(request, '%s is added to your cart.' % item_lookup)
                return redirect('../')
            elif item.age_resticted == True :
                request.session['itemPending'] = item.name
                if request.session.get('birthday_year') is None:
                    messages.info(request, 'Item %s requires age check.' % item.name)
                return redirect('../ageCheck')
        except:
            messages.info(request, 'Item %s not found.' % item_lookup)
            return redirect('../')
    except:
        item_lookup = request.session.get('itemPending').strip()
        item = Product.objects.get(name__icontains = item_lookup)
        addLog(request, item)
        messages.info(request, '%s is added to your cart' % item_lookup)
        return redirect('../')

def addItemImage(request):
    try:
        item_lookup = request.POST.get("itemimage").strip()
        try: 
            item = Product.objects.get(imageName__icontains = item_lookup)
            item_lookup = item.name
            if item.age_resticted == False:
                addLog(request, item)
                messages.info(request, '%s is added to your cart.' % item_lookup)
                return redirect('../')
            elif item.age_resticted == True :
                request.session['itemPending'] = item.name
                if request.session.get('birthday_year') is None:
                    messages.info(request, 'Item %s requires age check.' % item.name)
                return redirect('../ageCheck')
        except:
            messages.info(request, 'Item %s not found.' % item_lookup)
            return redirect('../')
    except:
        item_lookup = request.session.get('itemPending').strip()
        item = Product.objects.get(name__icontains = item_lookup)
        addLog(request, item)
        messages.info(request, '%s is added to your cart' % item_lookup)
        return redirect('../')

def payment(request):
    itemlist, total = readCart(request)
    return render(request, 'terminal/payment.html', {
        "itemlist": itemlist,
        "total": round(total, 2),
    })