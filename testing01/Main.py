from BlogProjectBuilder import BlogProjectBulder
from EcommerceProjectBuilder import ECommerceProjectBulder

builder = ECommerceProjectBulder()
builder.setLanguage("Python").setFramework("Django").setPattern("MVT")
builder.buildProject()
print(builder.getProject())

builder = BlogProjectBulder()
builder.setLanguage("Dart").setFramework("Flutter").setPattern("MVC")
builder.buildProject()
print(builder.getProject())