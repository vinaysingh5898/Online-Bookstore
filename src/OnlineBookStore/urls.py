from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    # Examples:
    url(r'^$', 'mainApp.views.home', name='home'),
    url(r'^add-author$', 'mainApp.views.addAuthor', name='add-author'),
    # url(r'^add-item/$', 'newsletter.views.addItem', name='add-item'),
    url(r'^delete-author/(?P<id>\w{1,50})$', 'mainApp.views.deleteAuthor', name='delete-author/id'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    
    url(r'^customer-login/','mainApp.views.customerLoginView',name='customer-login'), 
    url(r'^customer-register/','mainApp.views.customerRegisterView',name='customer-register'), 
    url(r'^seller-login/','mainApp.views.sellerLoginView',name='seller-login'), 
    url(r'^seller-register/','mainApp.views.sellerRegisterView',name='seller-register'), 
    url(r'^admin-login/','mainApp.views.adminLoginView',name='admin-login'), 
    url(r'^admin-register/','mainApp.views.adminRegisterView',name='admin-register'),
    url(r'^get-books-by-category/(?P<id>\d+)$', 'mainApp.views.getBooksByCategory', name='get_books_by_category'), 
    url(r'^get-single-book/(?P<id>\d+)$', 'mainApp.views.getSingleBook', name='get_single_book'), 
    url(r'^post-review/','mainApp.moreViews.postReview',name='post-review'), 
    url(r'^delete-review/(?P<id>\d+)/(?P<Book_id>\d+)$', 'mainApp.moreViews.deleteReview', name='delete_review'), 
    url(r'^add-to-cart/(?P<Book_id>\d+)','mainApp.moreViews.addToCart',name='add-to-cart'), 
    url(r'^cart-view/','mainApp.moreViews.cartView',name='cart-view'),
    url(r'^dec-quantity-in-cart/(?P<id>\d+)','mainApp.moreViews.decQuantityInCart',name='dec-quantity-in-cart'), 
    url(r'^inc-quantity-in-cart/(?P<id>\d+)','mainApp.moreViews.incQuantityInCart',name='inc-quantity-in-cart'), 
    url(r'^delete-book-from-cart/(?P<id>\d+)','mainApp.moreViews.deleteBookFromCart',name='delete-book-from-cart'), 
    url(r'^get-book-by-seller/(?P<id>\d+)','mainApp.moreViews.getBookBySeller',name='get-book-by-seller'), 
    url(r'^get-book-by-seller/(?P<id>\d+)','mainApp.moreViews.getBookBySeller',name='get-book-by-seller'), 
    url(r'^delete-book/(?P<Book_id>\d+)/(?P<id>\d+)','mainApp.moreViews.deleteBook',name='delete-book'), 
    url(r'^search-reasult','mainApp.moreViews.getSearchResult',name='search-reasult'), 
    url(r'^get-seller-single-book/(?P<id>\d+)$', 'mainApp.moreViews.getSellerSingleBook', name='get_seller_single_book'), 
    url(r'^about-us/','mainApp.moreViews.aboutUs',name='about-us'), 
    url(r'^faqs/','mainApp.moreViews.faqsView',name='faqs'), 
    url(r'^place-order/(?P<flag>\d+)','mainApp.moreViews.placeOrder',name='place-order'), 
    url(r'^add-publisher/', 'mainApp.views.addPublisher', name='add-publisher'),
    url(r'^recommend-new-admin/', 'mainApp.moreViews.recommendNewAdmin', name='recommend-new-admin'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^remove-recmmendation/(?P<id>\d+)$', 'mainApp.moreViews.removeRecmmendation', name='remove-recmmendation/'),
    url(r'^get-order-by-seller/$', 'mainApp.moreViews.getOrderBySeller', name='get-order-by-seller'),
    url(r'^update-to-shipped/(?P<id>\d+)$', 'mainApp.moreViews.updateToShipped', name='update-to-shipped'),
    url(r'^update-to-delivered/(?P<id>\d+)$', 'mainApp.moreViews.updateToDelivered', name='update-to-delivered'),
			
   
]


if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
