# BlogProject

> Simple yet powerful blog and easy to use for managing a blog. The frontend templates are taken from [here](https://bootstrapious.com/p/bootstrap-blog). Backend side is built using Django framework.

![BlogProject](https://github.com/nurettinabaci/BlogProject/blob/master/blog.png)

## Features
  - Create-update-delete post operations
  - New members can be created
  - Members can write a comment below any post
  - Login-register feature
  - Search post feature
  - Subscribe to newsletter feature powered with SendGrid API
  - TinyMCU is used for post create-update page
  - Crispy forms
    
  

## Run the project locally
1. Open the command line and clone the project to your local
```bash
git clone https://github.com/nurettinabaci/BlogProject.git
```

2. Go to project folder and create and activate a virtual environment
```bash

blogproj_env\Scripts\activate
```

3. Install project dependencies

   Make sure the environment is activated. Enter the folder where the project is located on the command line and use the package manager [pip](https://pip.pypa.io/en/stable/) to install the project [requirements](https://github.com/nurettinabaci/BlogProject/blob/master/requirements.txt) as below.

```bash
pip install -r requirements.txt
```

4. Migrate database
```bash
python manage.py migrate
```

5. Create a superuser

   After that you're going to  have full control over your blog.
```bash
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 
Don't forget to update `requirements.txt` file.

## License
This repository is licensed under the MIT License. Please see the [LICENSE](https://github.com/nurettinabaci/BlogProject/blob/master/LICENCE) file for more details.
