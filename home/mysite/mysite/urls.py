
from django.conf.urls import patterns, include, url
from app.views import hello, current_time, hours_ahead, display
from books import views
from contact.views import contact

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		url(r'^hello/$', hello),
        url(r'^display/$', display),
		url(r'^time/$', current_time),
        url(r'^time/plus/(\d{1,2})/$', hours_ahead),

        url(r'^search/$', views.search),
        #url(r'^search_form/$', views.search_form),

        url(r'^contact/$', contact),
         url(r'^contact/thanks/$', contact),

         url(r'^admin/', include(admin.site.urls)),
	# Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)
