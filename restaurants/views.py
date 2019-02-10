from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 
    	'my_list': [
    		{
    			'restaurant_name':'takohut',
    			'food_type':'italian food',
    	},
    		{
    			'restaurant_name':'shawarma plus',
    			'food_type':'Arabic food',
    	},
    		{
    			'restaurant_name':'Anatolia',
    			'food_type':'turkish food',
    	},
    	],


    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	'my_object': {
    	'restaurant_name':'takohut',
    	'food_type': 'italian food',
    	}

    }
    return render(request, 'detail.html', context)
