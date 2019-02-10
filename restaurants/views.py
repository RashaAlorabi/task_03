from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 
    	'my_list': [
    		{
    			'restaurant_name':'TacoHut',
    			'food_type':'pasta',
    	},
    		{
    			'restaurant_name':'ShawarmaPlus',
    			'food_type':'Checken',
    	},
    		{
    			'restaurant_name':'DankenDounts',
    			'food_type':'Desert',
    	},
    	],


    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	'my_object': {
    	'restaurant_name':'DankenDounts',
    	'food_type': 'Deserts'
    	}

    }
    return render(request, 'detail.html', context)
