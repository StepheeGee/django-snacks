#views.py

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["snacks"] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Oreo%2C_Traditional%2C_Chocolate_Sandwich_Cookies%2C_303g_Package_%282015%29.jpg/250px-Oreo%2C_Traditional%2C_Chocolate_Sandwich_Cookies%2C_303g_Package_%282015%29.jpg",
                "title": "Oreo",
                "description": "Oreo is a brand of cookie usually consisting of two chocolate wafers with a sweet crème filling, marketed as \"Chocolate Sandwich Cookie\".",
                "reference_url": "https://en.wikipedia.org/wiki/Oreo"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Kelloggs_Rice_Krispies_-_pantry.jpg/250px-Kelloggs_Rice_Krispies_-_pantry.jpg",
                "title": "Rice Krispies",
                "description": "Rice Krispies is a breakfast cereal marketed by Kellogg's in 1928 and released to the public in 1929.",
                "reference_url": "https://en.wikipedia.org/wiki/Rice_Krispies"
            }, {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Twinkies.jpg/250px-Twinkies.jpg",
                "title": "Twinkies",
                "description": 'Twinkies are an American snack cake, described as "golden sponge cake with a creamy filling". It was formerly made and distributed by Hostess Brands.',
                "reference_url": "https://en.wikipedia.org/wiki/Twinkie"
            }
        ]
        
        return context
    
class AboutPageView(TemplateView):
    template_name = 'about.html'
