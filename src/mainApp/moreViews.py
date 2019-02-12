from django.shortcuts import render
from .forms import *
from .models import *
from .backends import *
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.db.models import Sum,Avg
import datetime



Category_set=Category.objects.all().order_by("Name")

def postReview(request):
	review=Review()
	temp=request.POST.get("star",5)
	temp=20*int(temp)
	review.Ratings=temp
	error=0
	review.Book_id=request.POST.get("bookEdition"," ")
	if not Customer.objects.filter(user_id=request.user.id).count()>0:
		# return HttpResponseRedirect('../accounts/logout')
		error=1
	if not error:
		customer=Customer.objects.get(user_id=request.user.id)
		review.Customer_id=customer.id
		review.Content=request.POST.get("content"," nice")	
		review.save()

	# print(review.Book_id)
	allReviews=Review.objects.filter(Book_id=review.Book_id).order_by("-Created_at")
	class reviewDetail:
		def __init__(self, review=None, customer=None,user=None):
			self.review = review
			self.customer = customer
			self.user=user
	
	reviewList=[]

	for aReview in allReviews:
		customer=Customer.objects.get(id=aReview.Customer_id)
		user=User.objects.get(id=customer.user_id)
		reviewList.append(reviewDetail( aReview,customer,user))
	return render(request,"commentView.html",{"categories":Category_set,"reviewList":reviewList,"error":error})



def deleteReview(request,id=None,Book_id=None):
	review=Review.objects.get(id=id)
	review.delete()
	allReviews=Review.objects.filter(Book_id=Book_id).order_by("-Created_at")
	class reviewDetail:
		def __init__(self, review=None, customer=None,user=None):
			self.review = review
			self.customer = customer
			self.user=user
	
	reviewList=[]

	for aReview in allReviews:
		customer=Customer.objects.get(id=aReview.Customer_id)
		user=User.objects.get(id=customer.user_id)
		reviewList.append(reviewDetail( aReview,customer,user))
	return render(request,"commentView.html",{"categories":Category_set,"reviewList":reviewList})


def addToCart(request,Book_id=None):
	# check=1
	# if request.POST :
	# print (request.user.id)
	if not Customer.objects.filter(user_id=request.user.id).count()>0:
		error1=1
		return render(request,"Notifications/dummy.html" ,{"error1":error1})
	customer=Customer.objects.get(user_id=request.user.id)

	cartObj=Cart.objects.filter(Book_id=Book_id,Customer_id=customer.id)
	Quantity=1;
	if  cartObj :
		# cartObj[0].Quantity+=1
		Quantity=cartObj[0].Quantity+1
		cartObj.update(Quantity=cartObj[0].Quantity+1)
		check =1
	else :
		cartObject=Cart()
		cartObject.Customer_id=customer.id
		cartObject.Quantity=1;
		cartObject.Book_id=Book_id
		cartObject.save()
		check=0
	return render(request,"Notifications/dummy.html" ,{"check":check,"Quantity":Quantity})


def cartView(request):
	if not Customer.objects.filter(user_id=request.user.id).count()>0:
		return HttpResponseRedirect('../accounts/logout')
	customer=Customer.objects.get(user_id=request.user.id)
	cartObjects=Cart.objects.filter(Customer_id=customer.id)
	class cartObjectDetail(object):
		def __init__(self, cartObject=None, bookEdition=None):
			self.cartObject = cartObject
			self.bookEdition = bookEdition
	cartObjectList=[]
	totalPrice=0
	for cartObject in cartObjects:
		bookEdition=BookEdition.objects.get(id=cartObject.Book_id)
		cartObjectList.append(cartObjectDetail(cartObject,bookEdition))
		# print (cartObjectList.count)
		totalPrice+=(cartObject.Quantity*bookEdition.Price)
	totalPrice+=150
	return render(request,"cartView.html",{"totalPrice":totalPrice,
	 "Customer":customer,"cartObjectList":cartObjectList, "categories":Category_set})





def decQuantityInCart(request,id=None):
	c=Cart.objects.filter(id=id)
	if not c[0].Quantity==1:
		c.update(Quantity=c[0].Quantity-1)
	else :
		return render(request,"Notifications/cartdec.html" ,{"dec":2,"Quantity":c[0].Quantity})
	return render(request,"Notifications/cartdec.html" ,{"dec":1,"Quantity":c[0].Quantity})




def incQuantityInCart(request,id=None):
	c=Cart.objects.filter(id=id)
	c.update(Quantity=c[0].Quantity+1)
	return render(request,"Notifications/cartdec.html" ,{"dec":0,"Quantity":c[0].Quantity})


def deleteBookFromCart(request,id=None):
	book=Cart.objects.get(id=id)
	book.delete()
	if not Customer.objects.filter(user_id=request.user.id).count()>0:
		return HttpResponseRedirect('../accounts/logout')
	customer=Customer.objects.get(user_id=request.user.id)
	cartObjects=Cart.objects.filter(Customer_id=customer)
	class cartObjectDetail(object):
		def __init__(self, cartObject=None, bookEdition=None):
			self.cartObject = cartObject
			self.bookEdition = bookEdition
	cartObjectList=[]
	totalPrice=0
	for cartObject in cartObjects:
		bookEdition=BookEdition.objects.get(id=cartObject.Book_id)
		cartObjectList.append(cartObjectDetail(cartObject,bookEdition))
		totalPrice+=(cartObject.Quantity*bookEdition.Price)
	totalPrice+=150
	return render(request,"cartIndividualView.html",{"totalPrice":totalPrice,
	 "Customer":customer,"cartObjectList":cartObjectList})
# def orederViewDetail(request):




def placeOrder(request,flag=None):
	if not Customer.objects.filter(user_id=request.user.id).count()>0:
		return HttpResponseRedirect('../accounts/logout')
	customer=Customer.objects.get(user_id=request.user.id)
	cartObjects=Cart.objects.filter(Customer_id=customer)
	
	class orderObjectDetail(object):
		def __init__(self, orderObject=None, bookEdition=None):
			self.orderObject = orderObject
			self.bookEdition = bookEdition
	orderObjectList=[]
	totalPrice=0
	# print (flag)
	# print (request.user.id)
	if int(flag)==int(request.user.id):
		for cartObject in cartObjects:
			Ordr=Order()
			Ordr.Quantity=cartObject.Quantity
			Ordr.Book_id=cartObject.Book_id
			Ordr.Customer_id=cartObject.Customer_id
			Ordr.save()
			cartObject.delete()
	orderObjects=Order.objects.filter(Customer_id=customer)
	for orderObject in orderObjects:
		bookEdition=BookEdition.objects.get(id=orderObject.Book_id)
		orderObjectList.append(orderObjectDetail(orderObject,bookEdition))
		# print (ordertObjectList.count)
		totalPrice+=(orderObject.Quantity*bookEdition.Price)
	totalPrice+=150

	return render(request,"orderView.html",{"totalPrice":totalPrice,
	 "Customer":customer,"orderObjectList":orderObjectList, "categories":Category_set})

	# result = Book.objects.filter(string__icontains='%'Keyword+'%')
	
# class SearchProductView(ListView):
def getSearchResult(request):
	C="Search"
	query=request.POST.get('Search', )
	if query is not None:
		# print (query)
		books=Book.objects.filter(Title__icontains=query)
		class completeBookDetail(object):
			def __init__(self, book=None, bookEdition=None,discountedPrice=None):
				self.book = book
				self.bookEdition = bookEdition
				self.discountedPrice=discountedPrice
		bookDetailList1=[]
		for book in books:
			bookEditions=BookEdition.objects.filter(Book_id=book.id)
			if bookEditions.count()>0:
				# print (book.Title)
				for bookEdition in bookEditions :
					d=bookEdition.Price*bookEdition.Discount/100
					d=bookEdition.Price-d
					bookDetailList1.append(completeBookDetail(book,bookEdition,d))
		paginator = Paginator(bookDetailList1, 9)
		page = request.GET.get('page')
		try:
			bookDetailList = paginator.page(page)
		except PageNotAnInteger:
			bookDetailList = paginator.page(1)
		except EmptyPage:
			bookDetailList = paginator.page(paginator.num_pages)			
		return render(request,"categoryView.html",{"bookDetailList":bookDetailList,
			"categories":Category_set,"CategoryName":C})
	else :
		return HttpResponseRedirect('')

def getBookBySeller(request,id=None):
	seller=Seller.objects.get(User_id=id)
	C="Seller"
	if str(id)==str(request.user.id):
		bookEditions=BookEdition.objects.filter(Seller_id=seller.id)
		class completeBookDetail(object):
			def __init__(self, book=None, bookEdition=None,discountedPrice=None):
				self.book = book
				self.bookEdition = bookEdition
				self.discountedPrice=discountedPrice
		bookDetailList1=[]
		if bookEditions.count()>0:
			for bookEdition in bookEditions :
				book=Book.objects.get(id=bookEdition.Book_id)
				d=bookEdition.Price*bookEdition.Discount/100
				d=bookEdition.Price-d
				bookDetailList1.append(completeBookDetail(book,bookEdition,d))
		paginator = Paginator(bookDetailList1, 9)
		page = request.GET.get('page')
		try:
			bookDetailList = paginator.page(page)
		except PageNotAnInteger:
			bookDetailList = paginator.page(1)
		except EmptyPage:
			bookDetailList = paginator.page(paginator.num_pages)
		return render(request,"Seller/categoryView.html",{"bookDetailList":bookDetailList,
			"categories":Category_set,"CategoryName":C})
		return HttpResponseRedirect('')
def deleteBook(request,Book_id=None,id=None):
	if str(id)==str(request.user.id):
		bookEdition=BookEdition.objects.get(id=Book_id)
		bookEdition.delete()
		seller=Seller.objects.get(User_id=id)
		C="Seller"
		if str(id)==str(request.user.id):
			bookEditions=BookEdition.objects.filter(Seller_id=seller.id)
			class completeBookDetail(object):
				def __init__(self, book=None, bookEdition=None,discountedPrice=None):
					self.book = book
					self.bookEdition = bookEdition
					self.discountedPrice=discountedPrice
			bookDetailList1=[]
			if bookEditions.count()>0:
				for bookEdition in bookEditions :
					book=Book.objects.get(id=bookEdition.Book_id)
					d=bookEdition.Price*bookEdition.Discount/100
					d=bookEdition.Price-d
					bookDetailList1.append(completeBookDetail(book,bookEdition,d))
			paginator = Paginator(bookDetailList1, 9)
			page = request.GET.get('page')
			try:
				bookDetailList = paginator.page(page)
			except PageNotAnInteger:
				bookDetailList = paginator.page(1)
			except EmptyPage:
				bookDetailList = paginator.page(paginator.num_pages)
			return render(request,"Seller/categoryIndividualView.html",{"bookDetailList":bookDetailList,
				"categories":Category_set,"CategoryName":C})
	return HttpResponseRedirect('')

def getSellerSingleBook(request,id=None):
	form=ReviewForm(request.POST or None)
	bookEdition=BookEdition.objects.get(id=id)
	book=Book.objects.get(id=bookEdition.Book_id)
	class completeBookDetail(object):
		def __init__(self, book=None, bookEdition=None,discountedPrice=None,categories=None):
			self.book = book
			self.bookEdition = bookEdition
			self.discountedPrice=discountedPrice
			self.categories=categories
	d=bookEdition.Price*bookEdition.Discount/100
	d=bookEdition.Price-d
	Cs=BookCategory.objects.filter(Book_id=book.id)
	C=[]
	for x in Cs:
		y=Category.objects.get(id=x.Category_id)
		C.append(str(y.Name))
	bookDetail=completeBookDetail(book,bookEdition,d,C)
		# print (bookDetailList1)\

	allReviews=Review.objects.filter(Book_id=bookEdition.id).order_by("-Created_at")
	indiRating=Review.objects.filter(Book_id=bookEdition.id).order_by("-Created_at").aggregate(Avg('Ratings'))
	class reviewDetail:
		def __init__(self, review=None, customer=None,user=None):
			self.review = review
			self.customer = customer
			self.user=user
	
	reviewList=[]

	for aReview in allReviews:
		customer=Customer.objects.get(id=aReview.Customer_id)
		user=User.objects.get(id=customer.user_id)
		reviewList.append(reviewDetail( aReview,customer,user))
	# print(indiRating)
	return render(request,"Seller/singleView.html",
		{"bookDetail":bookDetail,"categories":Category_set,"indiRating":indiRating,"form":form,"reviewList":reviewList})
def aboutUs(request):
	return render(request,"Notifications/aboutUs.html",{"categories":Category_set})

def faqsView(request):
	return render(request,"Notifications/faqs.html",{"categories":Category_set})

def recommendNewAdmin(request):
	form=adminRecommendationForm(request.POST or None)
	recommedations=adminRecommendation.objects.all()
	if request.user.is_staff:
		if form.is_valid():
			instance = form.save(commit=False)
			instance.RecommendedBy_id=request.user.id
			instance.save()
			recommedations=adminRecommendation.objects.all()
			return render(request,'Admin/recommend.html',{"form":form,"recommedations":recommedations})
			# return HttpResponseRedirect('../admin-login/')
	else :
		error=1
		return render(request,'Admin/recommend.html',{"form":form,"error":error,"recommedations":recommedations})				
	return render(request,'Admin/recommend.html',{"form":form,"recommedations":recommedations})

def removeRecmmendation(request,id=None):
	rec=adminRecommendation.objects.get(id=id)
	rec.delete()
	recommedations=adminRecommendation.objects.all()
	return render(request,'Admin/recomendationTable.html',{"recommedations":recommedations})


def getOrderBySeller(request):
	seller=Seller.objects.filter(User_id=request.user.id)
	orderObjectList=[]
	orderObjects=[]
	if seller.exists():
		books=BookEdition.objects.filter(Seller_id=seller[0].id)
	# 	print(books)
		
		for book in books:
			tempOrders=Order.objects.filter(Book_id=book.id)
			for tempOrder in tempOrders:
				# print('hh')
				orderObjects.append(tempOrder)
			 	
	
		class orderObjectDetail(object):
			def __init__(self, orderObject=None, bookEdition=None):
				self.orderObject = orderObject
				self.bookEdition = bookEdition

		totalPrice=0
		
		# orderObjects=Order.objects.filter(Seller_id=seller[0].id)
		for orderObject in orderObjects:
			bookEdition=BookEdition.objects.get(id=orderObject.Book_id)
			orderObjectList.append(orderObjectDetail(orderObject,bookEdition))
			# print (ordertObjectList.count)
			totalPrice+=(orderObject.Quantity*bookEdition.Price)
		totalPrice+=150

		return render(request,"Seller/sellerOrderView.html",{"totalPrice":totalPrice,
		"orderObjectList":orderObjectList, "categories":Category_set})


def updateToDelivered(request,id=None):
	order=Order.objects.filter(id=id)
	order.update(DateOfDelivary=datetime.datetime.now())
	seller=Seller.objects.filter(User_id=request.user.id)
	orderObjectList=[]
	orderObjects=[]
	if seller.exists():
		books=BookEdition.objects.filter(Seller_id=seller[0].id)
	# 	print(books)
		
		for book in books:
			tempOrders=Order.objects.filter(Book_id=book.id)
			for tempOrder in tempOrders:
				# print('hh')
				orderObjects.append(tempOrder)
			 	
	
		class orderObjectDetail(object):
			def __init__(self, orderObject=None, bookEdition=None):
				self.orderObject = orderObject
				self.bookEdition = bookEdition

		totalPrice=0
		
		# orderObjects=Order.objects.filter(Seller_id=seller[0].id)
		for orderObject in orderObjects:
			bookEdition=BookEdition.objects.get(id=orderObject.Book_id)
			orderObjectList.append(orderObjectDetail(orderObject,bookEdition))
			# print (ordertObjectList.count)
			totalPrice+=(orderObject.Quantity*bookEdition.Price)
		totalPrice+=150

		return render(request,"Seller/orderIndividualView.html",{"totalPrice":totalPrice,
		"orderObjectList":orderObjectList, "categories":Category_set})

def updateToShipped(request,id=None):
	order=Order.objects.filter(id=id)
	order.update(DateOfShipment=datetime.datetime.now())
	seller=Seller.objects.filter(User_id=request.user.id)
	orderObjectList=[]
	orderObjects=[]
	if seller.exists():
		books=BookEdition.objects.filter(Seller_id=seller[0].id)
	# 	print(books)
		
		for book in books:
			tempOrders=Order.objects.filter(Book_id=book.id)
			for tempOrder in tempOrders:
				# print('hh')
				orderObjects.append(tempOrder)
			 	
	
		class orderObjectDetail(object):
			def __init__(self, orderObject=None, bookEdition=None):
				self.orderObject = orderObject
				self.bookEdition = bookEdition

		totalPrice=0
		
		# orderObjects=Order.objects.filter(Seller_id=seller[0].id)
		for orderObject in orderObjects:
			bookEdition=BookEdition.objects.get(id=orderObject.Book_id)
			orderObjectList.append(orderObjectDetail(orderObject,bookEdition))
			# print (ordertObjectList.count)
			totalPrice+=(orderObject.Quantity*bookEdition.Price)
		totalPrice+=150

		return render(request,"Seller/orderIndividualView.html",{"totalPrice":totalPrice,
		"orderObjectList":orderObjectList, "categories":Category_set})