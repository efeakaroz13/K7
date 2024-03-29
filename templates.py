import time
from flask import abort


class Templates:
    def articleprofiler(articles=[], userdata=None):
        if userdata == None:
            return """
            
                <script>
                    window.location.assign('/404')
                </script>
            """
        else:
            return """

                <!DOCTYPE html>
                <html lang="tr">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width0device-width, initial-scale=1.0">
                    <title> """+userdata['fullname']+""" - K7</title>
                    <meta name="yandex-verification" content="ebb5b88813a54c1f" />
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                    <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                    <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                    <link
                    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                    rel="stylesheet"
                    />
                <!-- Google Fonts -->
                    <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />

                </head>
                <body style="color:black">
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7</p>
                <br><br>
                <center><div class="card" style="width:70%;">
                    <center>
                    <div class="card-body">
                        <h5 class="card-title">"""+userdata["username"]+" - "+userdata["fullname"]+"""</h5>
                        <p class="card-text">
                            Yetenekleri:"""+userdata["talents"]+"""
                        </p>
                    </div>
                    
                    </center>
                </div>
                <br>
                <h4> K7 üzerinden yaptığı yayımlar</h4>
                </center>
                </body>
                </html>

            """

    def return_index_tr():
        return """

            <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7</title>
                <meta name="yandex-verification" content="ebb5b88813a54c1f" />
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7</p>
                <br><br>
                <br>


                    <div style="height:100%; margin-left:30px;">
                    <h2 style="font-family: 'Libre Franklin', sans-serif;">Bağımsız bilim kuruluşu </h2>
                    <p style="font-family: 'Libre Franklin', sans-serif;width:60%;">K7'nin amacı insanları doğru ve güvenilir bilgiye ulaştırmak; insanları eğitmek ve kültürlendirmektir. Her okuyucu K7'nin imkanlarını ücretsiz olarak kullanabilir. K7 hakkında daha fazla bilgi için <a href="https://cetele.pythonanywhere.com/read/K7%20ve%20ama%C3%A7lar%C4%B1">buraya</a> gözatabilirsiniz</p>
                  </div>

                <br><br>

                <br><br><br>
              

                
                <br><br>
                <center>
                <div style="border:1px solid #000;border-radius:5px;padding:30px;width:70%;">
                    <h3></h3>
                    <button class="btn btn-dark" onclick="window.location.assign('/login')">Giriş Yap</button>
                    <button class="btn btn-outline-dark" onclick="window.location.assign('/register')">Kayıt Ol</button>
                    <div style="transition:0.5s;margin-left:20px;"><br>
                    <h4 style="font-family: 'Parisienne', cursive;font-size:20px;transition:1s;">
                        En büyük savaş, cahilliğe karşı yapılan savaştır.
                    </h4>

                    <img src="/static/mka.png" width="100">
                </div>
                </center>
            </body>
            </html>

        """

    def return_login_tr():
        return """

            <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7 - Giriş Yap</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Giriş Yap</p>
                <br><br>
                <br>
                <center>
                <div class="card" style="width:80%; padding:30px">
                    <div class="card-body>
                        <h4 class="card-title" style="font-size:25px;text-align:left;margin-left:50px;">Giriş yap</h4><br><br>
                        <form class="card-text" method="POST" action="">
                            <input type="text" autocomplete="off" autocapitalize="off" name="username" placeholder="Kullanıcı Adı..." class="form-control" style="width:70%;margin-bottom:20px;">
                            <input type="password" autocomplete="off" autocapitalize="off" name="password" placeholder="Şifre..." class="form-control" style="width:70%;">
                            <button class="btn btn-primary">Onayla</button>
                        </form>
                    </div>
                </div>
                </center>


                    
            </body>
            </html>

        """

    def return_login_err_tr():
        return """

            <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7 - Giriş Yap</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Giriş Yap</p>
                <br><br>
                <br>
                <center>
                <div class="card" style="width:80%; padding:30px">
                    <div class="card-body>
                        <h4 class="card-title" style="font-size:25px;text-align:left;margin-left:50px;">Giriş yap</h4><br><br>
                        <form class="card-text" method="POST" action="">
                            <input type="text" autocomplete="off" autocapitalize="off" name="username" placeholder="Kullanıcı Adı..." class="form-control" style="width:70%;margin-bottom:20px;">
                            <input type="password" autocomplete="off" autocapitalize="off" name="password" placeholder="Şifre..." class="form-control" style="width:70%;">
                            <button class="btn btn-danger">Onayla</button>
                            <br>
                            <i style="color:grey;font-size:13px;">Kullanıcı adı veya şifre doğru değil</i>
                        </form>
                    </div>
                </div>
                </center>


                    
            </body>
            </html>

        """

    def return_home_tr(username, articles):
        if len(articles) != 0:
            print(articles)
            articlescode = """
                <ul class="list-group" style='width:70%;'>
            """
            for ar in articles:
                articlescode = (
                    articlescode
                    + "<li class='list-group-item' style='text-align:left;'><a href='/read/"
                    + str(articles[articles.index(ar)]["data"]["articleid"])
                    + "'>"
                    + str(articles[articles.index(ar)]["data"]["title"])
                    + "</a><a style='color:red;float:right'>"
                    + str(articles[articles.index(ar)]["data"]["visibility"])
                    + "</a><br><i style='color:black'>"
                    + str(articles[articles.index(ar)]["data"]["article"])[:13]
                    + "...</i><br><i>"
                    + time.ctime(int(articles[articles.index(ar)]["data"]["lastsaved"]))
                    + "</i></li>"
                )

            articlescode = articlescode + "</ul>"
            print(articlescode)
        else:
            articlescode = """
                <ul class="list-group" style='width:70%;'>
                    <li class="list-group-item">Daha önce hiç makale yazmadınız...</li>
                </ul>
            """
        return (
            """

            <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - """
            + username
            + """<a style="font-size:10px;color:red;margin-left:10px;margin-bottom:4px" href="/logout">logout</a><a style="position:fixed;right:10px" href="/user/"""
            + username
            + """"><img  src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fmafiagame%2Fimages%2F2%2F23%2FUnknown_Person.png%2Frevision%2Flatest%3Fcb%3D20151119092211&f=1&nofb=1" style="border-radius:50%;width:50px;border:1px solid #000;"></a></p>
                <br><br>
                <br>
                <center>
                    <br>
                    """
            + articlescode
            + """<br>
                    <button onclick="window.location.assign('/writearticle')">Makale Yaz</button><button onclick="window.location.assign('/explore')">Keşfet <i class="fa-solid fa-compass"></i></button>
                </center>
                <style>
                    button{
                        background:none;
                        border:1px solid #000;
                        border-radius:5px;
                        margin:5px;
                        transition:0.5s;

                    }
                    button:hover{
                        background:#000;
                        border:1px solid #fff;
                        border-radius:5px;
                        color:white;
                        margin:5px;
                        transition:0.5s;

                    }
                </style>


                    
            </body>
            </html>

        """
        )

    def return_register_tr():
        return """


            <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7 - Kayıt ol</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Kayıt ol</p>
                <br><br>
                <br>
                <center>
                <div class="card" style="width:80%; padding:30px">
                    <div class="card-body>
                        <h4 class="card-title" style="font-size:25px;text-align:left;margin-left:50px;">Üyelik</h4><br><br>
                        <form class="card-text" method="POST" action="">
                            <input type="text" name="username" autocomplete="off" placeholder="Kullanıcı adı" class="form-control" style="width:70%;" required><br>
                            <input type="text" name="fullName" autocomplete="off" placeholder="Tam adınız" class="form-control" style="width:70%;" required><br>
                            <input type="text" name="birthyear"autocomplete="off" placeholder="Doğum yılınız" class="form-control" style="width:70%;" required><br>
                            <input type="text" name="city"autocomplete="off" placeholder="Yaşadığınız şehir" class="form-control" style="width:70%;" required><br>
                            <input type="password" name="password" autocomplete="off" placeholder="Şifreniz..." class="form-control" style="width:70%;" required><br>
                            <textarea  name="talents"placeholder="Yetenekleriniz(hangi konu ile alakalı olduğu size kalmış)" class="form-control" required></textarea><br>
                            <button class="btn btn-primary">Onayla</button>
                        </form>
                    </div>
                </div>
                </center>


                    
            </body>
            </html>




        """

    def return_register_unknown_tr():
        return """


            <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7 - Hata!</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Kayıt ol</p>
                <br><br>
                <br>
                <center>
                <div class="card" style="width:80%; padding:30px">
                    <div class="card-body>
                        <h4 class="card-title" style="font-size:25px;text-align:left;margin-left:50px;">Üyelik </h4><br><br>
                        <form class="card-text" method="POST" action="">
                            <input type="text" name="username" autocomplete="off" placeholder="Kullanıcı adı" class="form-control" style="width:70%;"><br>

                            <input type="text" name="fullName" autocomplete="off" style="border:1px solid red;" placeholder="Tam adınız" class="form-control" style="width:70%;" required><br>
                            <input type="text" name="birthyear"autocomplete="off" placeholder="Doğum yılınız" class="form-control" style="width:70%;" required><br>
                            <input type="text" name="city"autocomplete="off" placeholder="Yaşadığınız şehir" class="form-control" style="width:70%;" required><br>
                            <textarea  name="talents"placeholder="Yetenekleriniz(hangi konu ile alakalı olduğu size kalmış)" class="form-control" required></textarea><br>
                            <input type="password" name="password" autocomplete="off" placeholder="Şifreniz..." class="form-control" style="width:70%;" required><br>
                            <button class="btn btn-primary">Onayla</button>
                        </form>
                    </div>
                </div>
                </center>


                    
            </body>
            </html>




        """

    def register_err_tr(out):
        return (
            """


            <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7 - Hata!</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Edu+NSW+ACT+Foundation&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Kayıt ol</p>
                <br><br>
                <br>
                <center>
                <div class="card" style="width:80%; padding:30px">
                    <div class="card-body>
                        <h4 class="card-title" style="font-size:25px;text-align:left;margin-left:50px;">Üyelik </h4><br><br>
                        <form class="card-text" method="POST" action="">
                            <input type="text" name="username" autocomplete="off" placeholder="Kullanıcı adı" class="form-control" style="width:70%;"><br>

                            <input type="text" name="fullName" autocomplete="off" style="border:1px solid red;" placeholder="Tam adınız" class="form-control" style="width:70%;"><br>
                            <input type="text" name="birthyear"autocomplete="off" placeholder="Doğum yılınız" class="form-control" style="width:70%;" required><br>
                            <input type="text" name="city"autocomplete="off" placeholder="Yaşadığınız şehir" class="form-control" style="width:70%;" required><br>
                            <textarea  name="talents"placeholder="Yetenekleriniz(hangi konu ile alakalı olduğu size kalmış)" class="form-control" required></textarea><br>
                            <input type="password" name="password" autocomplete="off" placeholder="Şifreniz..." class="form-control" style="width:70%;" required><br>
                            <p>"""
            + out
            + """</p>
                            <button class="btn btn-primary">Onayla</button>
                        </form>
                    </div>
                </div>
                </center>


                    
            </body>
            </html>




        """
        )

    def return_register_done_tr(username):
        return (
            """


            <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7 - Hata!</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Kayıt ol</p>
                <br><br>
                <br>
                <center>

                    <h2>K7'ye hoş geldin """
            + username
            + """ </h2>
                    <p>Burada bilimsel yazınlarını paylaşabilir, insanlara bir şeyler katmaya çalışabilirsin.<a href="">K7 kurallar klavuzu</a>'nu başlamadan önce okumanı tavsiye ederiz!</p>
                </center>


                    
            </body>
            </html>




        """
        )

    def notfound():
        return """
            <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7 - Sayfa bulunamadı</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Sayfa bulunamadı!(404)</p>
                <br><br>
                <br>
                <center>
                    <p style="font-size:30px;padding:20px">Aradığınız sayfayı sunucumuzda göremiyoruz. Ancak anasayfamızı ziyaret edip ücretsiz bir şekilde araştırmalarımızı okuyabilirsiniz!</p>
                    <a href="/">K7 Anasayfası<a> | <a href="/register">Kayıt Ol</a> | <a href="/login">Üyeysen giriş yap</a>
                    <i style="position:fixed;bottom:10px;left:10px">Özgür ve bağımsız bilim platformu</i>
                </center>


                    
            </body>
            </html>

        """

    def writeart(username):

        return (
            """
            <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7 - Makale Oluştur</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Edu+NSW+ACT+Foundation&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Makale Oluştur <code>"""
            + username
            + """</code></p>
                <br><br>
                <br>
                <script src="/static/article.js"></script>
                <center>
                    <form action="" method="POST">
                        <input type="text" name="title"placeholder="Yazın Başlığı..." name="title" style="width:70%;"><br><br>
                        <textarea id="article" name="article"class="form-control" style="width:70%;height:400px;" placeholder="İçerik..." ></textarea><br>
                        <input id="fontfamily" name="fontfamily" class="disabled" value="default"type="text" placeholder="Yazı stili..." style="width:70%;display:none;">
                        <select name="visibility" class="form-control"style="width:70%;margin-bottom:10pxd">
                            <option value="public">Herkese Açık</option>
                            <option value="private">Gizli</option>
                        </select>
                        <button>Kaydet</button><br><br>
                    </form>
                    <button onclick="setfont('verdana')" style="font-family:verdana">Verdana</button>
                    <button onclick="setfont('monospace')" style="font-family:monospace">Monospace</button>
                    <button onclick="setfont('default')">Default</button>
                    <button onclick="setfont('Edu NSW ACT Foundation')" style="font-family: 'Edu NSW ACT Foundation', cursive;">Edu NSW ACT Foundation</button>
                </center>
                    
            </body>
            </html>

        """
        )

    def articlereadsingle(articledata, username=None, views=0):
        print(articledata["data1"].keys())
        if username == None:
            username = ""
            profilebar = ""
        else:
            profilebar = (
                """
            <a style="position:fixed;right:10px" href="/user/"""
                + username
                + """"><img  src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fmafiagame%2Fimages%2F2%2F23%2FUnknown_Person.png%2Frevision%2Flatest%3Fcb%3D20151119092211&f=1&nofb=1" style="border-radius:50%;width:50px;border:1px solid #000;"></a>
            """
            )
        if articledata["edit"] == True:
            title = (
                """
                <h2>"""
                + articledata["data1"]["title"]
                + """<a style='margin-left:10px' href="?edit=BLYAD"><i class="fa-solid fa-pencil"></i></a></h2>
            """
            )
            if articledata["data1"]["visibility"] == "public":
                visibility = """<p>Herkese Açık <i class="fa-solid fa-eye"></i><p>"""
            else:
                visibility = """<p>Gizli <i class="fa-solid fa-lock" ></i><p>"""

        else:
            visibility = ""
            title = (
                """
                <h2>"""
                + articledata["data1"]["title"]
                + """</h2>
            """
            )
        credit = (
            """<i><a style='color:red'>"""
            + articledata["data1"]["username"]
            + """</a> Tarafından <a style='color:blue'>"""
            + time.ctime(articledata["data1"]["lastsaved"])
            + """</a> tarihinde kaydedildi</i>"""
        )

        article = (
            """<p style="color:black;font-family:"""
            + articledata["data1"]["fontfamily"]
            + ";word-wrap: break-word; white-space: pre-wrap;"
            + """">"""
            + articledata["data1"]["article"]
            + """</p>"""
        )
        return (
            """
        <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Edu+NSW+ACT+Foundation&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Okuyucu <code>"""
            + username
            + """</code>"""
            + profilebar
            + """</p>
                <br><br>
                <br>
                <center>
                <div class='titlething' style="width:80%;text-align:left">
                    """
            + title
            + """
                    <i style='font-size:10px'>"""
            + views
            + """ kere görüntülendi</i><br><br>
                    """
            + visibility
            + """
                    """
            + credit
            + """
                    <br><br>
                    
                </div>

                    <div style="width:80%;text-align:left">
                    """
            + article
            + """
                    </div>
                </center>
                    
            </body>
            </html>
        """
        )

    def articleedit(articledata, username=None):
        print(articledata["data1"].keys())
        if username == None:
            username = ""
            profilebar = ""
        else:
            profilebar = (
                """
            <a style="position:fixed;right:10px" href="/user/"""
                + username
                + """"><img  src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fmafiagame%2Fimages%2F2%2F23%2FUnknown_Person.png%2Frevision%2Flatest%3Fcb%3D20151119092211&f=1&nofb=1" style="border-radius:50%;width:50px;border:1px solid #000;"></a>
            """
            )

        title = (
            """
            <input name='title' class='form-control' style='width:80%;' value='"""
            + articledata["data1"]["title"]
            + """'/>
        """
        )
        selectorform1 = """<br>
            <select name="visibility" class='form-control'style='width:80%;'>
                <option value="public">Herkese Açık</option>
                <option value="private">Gizli</option>
            </select>
        """
        selectorform2 = """<br>
            <select name="visibility"  class='form-control'style='width:80%;'>
                <option value="private">Gizli</option>
                <option value="public">Herkese Açık</option>
                
            </select><br>
        """

        if articledata["data1"]["visibility"] == "public":
            visibility = str(selectorform1)
        else:
            visibility = str(selectorform2)

        credit = (
            """<i><a style='color:blue'>"""
            + time.ctime(articledata["data1"]["lastsaved"])
            + """</a> tarihinde kaydedildi</i>"""
        )

        article = (
            """<textarea  name='article' class='form-control' id='article' style="width:80%;height:400px;color:black;font-family:"""
            + articledata["data1"]["fontfamily"]
            + """ ">"""
            + articledata["data1"]["article"]
            + """</textarea>"""
        )
        return (
            """
        <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7 - Makale Oluştur</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Edu+NSW+ACT+Foundation&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
                <script src="https://code.jquery.com/jquery-3.6.1.js" integrity="sha256-3zlB5s2uwoUzrXK3BT7AX3FyvojsraNFxCc2vC/7pNI=" crossorigin="anonymous"></script>
                <link rel="stylesheet" src="/static/articlestylerstuff.css">
                
                <script src="https://code.jquery.com/jquery-3.6.1.js" integrity="sha256-3zlB5s2uwoUzrXK3BT7AX3FyvojsraNFxCc2vC/7pNI=" crossorigin="anonymous"></script>
                <script src="/static/iframeEditor.js"></script>
                
            </head>
            <body>

                <div id="wikiframe" style="display:none;position:absolute;">
                    <button style="position:fixed;top:10px;right:10px;font-family:verdana;font-size:30px;background:none;border:0px;" onclick="OpenWikipedia()">-</button>
                    <iframe src="/wikipedia_data" id="iframerwikipedia" style="width:100%;"></iframe>
                </div>
                <div id="iframesearch" style="display:none;">
                    <div style="width:100%;height:130vh;background-color:#151519;">
                    <button onclick="openEngine()" style="background-color:red;color:white;border:1px solid #fff;margin:10px;border-radius:50%;width:20px;height:20px;position:absolute;right:20px;top:20px;"></button>

                    <center><iframe src="https://searx.thegpm.org/" id="searx"style="width:97%;height:98vh;border:1px solid#000;"></iframe></center>
                    </div>
                </div>
                <script src="/static/sozluk.js" ></script>
                <style>
                .desktop{
                    position:absolute;
                    right:0px;
                    top:120px;
                    width:50vh;
                    height:55vh;
                    border:1px solid #000;

                }
                #trdict{
                    border:1px solid #000;
                    width:70%;
                    position:fixed;
                    top:150px;
                    margin-bottom:100px;
                    right:15%;
                    left:15%;
                    padding-top:10px;
                    padding-bottom:10px;
                    border-radius:5px;
                    background:#fff;
                    color:black;
                    font-family:sans-serif;

                }
                #results{
                    text-align:left;

                }
                li{margin-top:6px;}
                .desktop2{
                    width:100%;
                    height:49vh;
                }


                #close{
                    color:black;
                    background:none;
                    border:0px;
                    font-family:sans-serif;

                    position:relative;
                    left:10px;
                    transition:0.5s;
                    border-radius:50%;
                    width:30px;
                    height:30px;
                }
                #close:hover{
                    color:white;
                    background:black;
                    border:0px;
                    font-family:sans-serif;

                    position:relative;
                    left:10px;
                    transition:0.5s;
                }






                </style>
                <div id="everystuff" style="display:;">

                    <script src="/static/article.js"></script>
                    <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Düzenleyici <code>"""
            + username
            + """</code>"""
            + profilebar
            + """</p>
                    <br><br>
                    
                        <div id="trdict" style="display:none;">

                            <button id='close' onclick="SOZLUK()">x</button><br>
                            <center>
                            <h2>TDK Sözlük</h2><br>
                            <input id="search" type="text" placeholder="Kelime girin..." autocomplete="off"><button onclick="searchDOM()">Ara</button><br>
                            </center>
                            <ul id="results">
                            </ul>
                        </div>
                     
                    <br>
                    <div >
                        <center>
                        <button class="btn btn-outline-dark"style="position:fixed;right:-20px;" onclick="openEngine()"><i class="fas fa-search" style="margin-right:8px"></i></button><br><br>
                        <button class="btn btn-outline-dark"style="position:fixed;right:-20px;margin-top:-10px"><i class="fa-solid fa-book-atlas" style="margin-right:8px;"></i></button><br><br>
                        <button class="btn btn-danger"style="position:fixed;right:-20px;margin-top:-20px;background-color:#ff0505" onclick="SOZLUK()"><a style="margin-right:5px;">tr</a></button><br><br>
                        <button class="btn btn-outline-dark"style="position:fixed;right:-20px;margin-top:-20px;" onclick="OpenWikipedia()"><i class="fa-brands fa-wikipedia-w" style="margin-right:8px"></i></button><br><br>
                        
                        <form action="" method="POST">
                            <div class='titlething' >
                                """
            + title
            + """
                                """
            + visibility
            + """
                                """
            + credit
            + """
                                <br><br>
                                <input type='text' id="fontfamily" style='display:none;' name='fontfamily'>
                            </div>

                            <div >
                            """
            + article
            + """
                            </div>
                            <br>
                            <button type="submit">Kaydet</button><br><br>
                        </form>
                            <button onclick="setfont('verdana')" style="font-family:verdana">Verdana</button>
                            <button onclick="setfont('monospace')" style="font-family:monospace">Monospace</button>
                            <button onclick="setfont('default')">Default</button>
                            <button onclick="setfont('Edu NSW ACT Foundation')" style="font-family: 'Edu NSW ACT Foundation', cursive;">Edu NSW ACT Foundation</button>
                        </center>
                    </div>
                </div>
                    
            </body>
            </html>
        """
        )

    def makearticle_visible(articledata):
        return f"""<!DOCTYPE html>
                    <html lang="tr">
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>K7 - Makale Oluştur</title>
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                        <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                        <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                        <link rel="preconnect" href="https://fonts.googleapis.com">
                        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                        <link href="https://fonts.googleapis.com/css2?family=Edu+NSW+ACT+Foundation&display=swap" rel="stylesheet">
                        <link
                          href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                          rel="stylesheet"
                        />
                        <!-- Google Fonts -->
                        <link
                          href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                          rel="stylesheet"
                        />
                        <!-- MDB -->
                        <link
                          href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                          rel="stylesheet"
                        />
                    </head>
                    <body>
                        <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Makale Doğrulama</p>
                        <br><br>
                        <div style="color:black">
                        <center>
                            <h2>{articledata['title']}</h2>
                            <p>{articledata['article']}</p>
                            <form action="" method="POST">
                                <select name="approved" class="form-control" style="width:60%">
                                    <option value="true">Onayla</option>
                                    <option value="false">Reddet</option>
                                </select>
                                <button class="btn btn-primary">Tamamla</button>
                            </form>
                        </center>
                        </div>


                    </body>
                    </html>"""

    def profiler(userdata, lastarticle, profileofmine, outlist):

        if profileofmine == True:
            codeinjector1card = """
            
                <a style='text-align:left;margin-left:20px;margin-bottom:20px'><i class="fa-solid fa-gear" style="background: linear-gradient(to right, #d2d5d6,#3d515e, #2f4451, #214052);-webkit-text-fill-color: transparent;-webkit-background-clip: text;"></i> Ayarlar</a><center><div style='margin-top:10px;width:100%;height:2px;border:1px solid #888688; '></div></center>
                <br>
                <a href="/change/password">Şifreni değiştir</a>
            """
            codeinjector2list = """
                            <ul class="list-group" style='width:80%;'>
                        """
            if len(outlist) > 1:
                for ar in outlist:
                    codeinjector2list = (
                        codeinjector2list
                        + "<li class='list-group-item' style='text-align:left;'><a href='/read/"
                        + str(outlist[outlist.index(ar)]["articleid"])
                        + "'>"
                        + str(outlist[outlist.index(ar)]["title"])
                        + "</a><a style='color:red;float:right'>"
                        + str(outlist[outlist.index(ar)]["visibility"])
                        + "</a><br><i style='color:black'>"
                        + str(outlist[outlist.index(ar)]["article"])[:20]
                        + "...</i><br><i>"
                        + time.ctime(int(outlist[outlist.index(ar)]["lastsaved"]))
                        + "</i></li>"
                    )
            else:
                pass
            codeinjector2list = codeinjector2list + "</ul>"

        else:
            codeinjector1card = ""
            codeinjector2list = """
            <ul class="list-group" style='width:80%;'>
            
            """
            if len(outlist) > 1:
                for ar in outlist:
                    if outlist[outlist.index(ar)]["visibility"] == "public":
                        codeinjector2list = (
                            codeinjector2list
                            + "<li class='list-group-item' style='text-align:left;'><a href='/read/"
                            + str(outlist[outlist.index(ar)]["articleid"])
                            + "'>"
                            + str(outlist[outlist.index(ar)]["title"])
                            + "</a><a style='color:red;float:right'>"
                            + str(outlist[outlist.index(ar)]["visibility"])
                            + "</a><br><i style='color:black'>"
                            + str(outlist[outlist.index(ar)]["article"])[:20]
                            + "...</i><br><i>"
                            + time.ctime(int(outlist[outlist.index(ar)]["lastsaved"]))
                            + "</i></li>"
                        )
            else:
                pass
            codeinjector2list = codeinjector2list + "</ul>"

        return (
            """
        <!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7 - Makale Oluştur</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Edu+NSW+ACT+Foundation&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <script src="/static/article.js"></script>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7</p>
                <br><br>
                <center>
                <div class="card" style="width:80%;text-align:left;">
                    <div class="card-body">
                        <h5 class="card-title">"""
            + userdata["fullname"]
            + """</h5>
                        <i>"""
            + userdata["username"]
            + """</i>
                        <p class="card-body">
                            <p><i class="fa-solid fa-newspaper"  style="background: linear-gradient(to right, #d2d5d6,#3d515e, #2f4451, #214052);-webkit-text-fill-color: transparent;-webkit-background-clip: text;margin-right:10px"></i>Son düzenleme: """
            + lastarticle
            + """</p>
                            <p><i style="background: linear-gradient(to right, #f00821,#f10821, #f00834, #f00821);-webkit-text-fill-color: transparent;-webkit-background-clip: text;margin-right:10px" class="fa-solid fa-location-dot"></i>"""
            + userdata["city"]
            + """</p>
                        </p>
                        <br>
                        """
            + codeinjector1card
            + """
                    </div>
                </div><br>
                """
            + codeinjector2list
            + """
                </center>
                
                    
            </body>
            </html>
        """
        )

    def changepassword(username_, error__):

        toreturn = """<!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7 - Makale Oluştur</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Edu+NSW+ACT+Foundation&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Şifreni Değiştir</p>
                <br><br>
                <center>
                <div class="card" style="width:70%;">
                    <div class="card-body">
                        <h5 class="card-title" style="color:black;font-family:verdana">Şifreni Değiştir</h5>
                        <form action="" method="POST"><br>
                            <input type="text" style="width:70%;" placeholder="Kullanıcı adınız(doğrulama için)" name="username_verify" class="form-control" required>
                            <input type="password" style="width:70%;" placeholder="Mevcut şifreniz..." name="oldpassword" class="form-control" required>
                            <input type="password" style="width:70%;color:black;" placeholder="Yeni şifreniz..." name="newpassword" class="form-control" required><br>
                            <button class="btn btn-outline-dark">Şifreyi Kaydet</button><br>
                            
                        </form>
                        <i style='color:red;font-size:10px;'>"""

        secondpart = """</i>
                    </div>
                
                </div>
                </center>
                
                    
            </body>
            </html>"""

        return toreturn + secondpart

    def changepassword_err(username_, error__):

        toreturn = """<!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7 - Makale Oluştur</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Edu+NSW+ACT+Foundation&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Şifreni Değiştir</p>
                <br><br>
                <center>
                <div class="card" style="width:70%;">
                    <div class="card-body">
                        <h5 class="card-title" style="color:black;font-family:verdana">Şifreni Değiştir</h5>
                        <form action="" method="POST"><br>
                            <input type="text" style="width:70%;" placeholder="Kullanıcı adınız(doğrulama için)" name="username_verify" class="form-control" required>
                            <input type="password" style="width:70%;" placeholder="Mevcut şifreniz..." name="oldpassword" class="form-control" required>
                            <input type="password" style="width:70%;color:black;" placeholder="Yeni şifreniz..." name="newpassword" class="form-control" required><br>
                            <button class="btn btn-outline-dark">Şifreyi Kaydet</button><br>

                        </form>
                        <i style='color:red;font-size:10px;'>"""

        secondpart = """</i>
                    </div>

                </div>
                </center>


            </body>
            </html>"""

        return toreturn + error__ + secondpart

    def explore(data):
        return """<!DOCTYPE html>
            <html lang="tr">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>K7 - Makale Oluştur</title>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Edu+NSW+ACT+Foundation&display=swap" rel="stylesheet">
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                  rel="stylesheet"
                />
                <!-- Google Fonts -->
                <link
                  href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                  rel="stylesheet"
                />
                <!-- MDB -->
                <link
                  href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                  rel="stylesheet"
                />
            </head>
            <body>
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Keşfet</p>
                <br><br>
                <center>
                
                </center>


            </body>
            </html>"""

    def rsorthing():
        return """<!DOCTYPE html>
                <html lang="tr">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>K7 - RSOR</title>
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                    <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                    <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Edu+NSW+ACT+Foundation&display=swap" rel="stylesheet">
                    <link
                      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                      rel="stylesheet"
                    />
                    <!-- Google Fonts -->
                    <link
                      href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                      rel="stylesheet"
                    />
                    <!-- MDB -->
                    <link
                      href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                      rel="stylesheet"
                    />
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@300&display=swap" rel="stylesheet">
                </head>
                <body>

                    <br><br>
                    <center>
                    <h2>RSOR</h2>
                    <div style="width:60%;">
                    <form action="" method="POST">
                    <input type="text" name="search" placeholder="Arama Yapın" class="search"><button>Ara</button>
                    </div>
                    </form>
                    </center>
                    <style>
                        h2{
                            font-family: 'Rajdhani', sans-serif;
                            color:black;
                            font-size:50px;
                        }
                        .search{
                            padding-left:10px;
                            
                            width:80%;
                            
                        }
                        input[type="text"].search::-webkit-input-placeholder {
                            color: black;
                            font-family: 'Rajdhani', sans-serif;

                        }
                        button{
                            font-family: 'Rajdhani', sans-serif;
                            border:1px solid #000;
                            padding:3px;
                            background:none;
                            border-radius:3px;
                            width:10%;
                            padding-bottom:1px;
                            border-left:0px;

                        }
                    </style>


                </body>
                </html>"""

    def rsorthingPOST(search, data):
        if len(data["wikipedia"]) > 0:
            output = """
                <details>
                <summary id="result">Vikipedi Sonuçları</summary>
                <div id="wiki" style="width:60%;">

            """
        else:
            output = ""

        for w in data["wikipedia"]:

            snippetter = f"""
            <details>
              <summary>{w['title']}</summary>
              <p style="margin-left:5px;font-size:15px">{w['snippet']}...</p><br>
              <i style="color:#2d2d2d">Kelime sayısı:{w['wordcount']}</i><br>
              <a href="/wikipediaopener/{w['pageid']}">Vikipedi'de Oku</a>
            </details>
            """
            output = output + str(snippetter) + "<br>"
        output = output + "</div></details>"

        output = (
            output
            + """
        <p class="google"><a style="color:#4285F4;">G</a><a style="color:#EA4335;">o</a><a style="color:#FBBC05;">o</a><a style="color:#4285F4;">g</a><a style="color:#34A853;">l</a><a style="color:#FBBC05">e</a></p>
            <div id="wiki" style="width:60%;">"""
        )
        for g in data["google"]:
            try:
                image = f"""<img width="100"  loading="lazy" src="{g["pagemap"]["cse_image"][0]["src"]}"/> """
            except Exception as e:
                image = f""
            try:
                themecolor = f"""{g["pagemap"]["metatags"][0]["theme-color"]}"""
            except:
                themecolor = ""

            try:
                rating = f"""<i>Puan:{g["pagemap"]["aggregaterating"][0]["ratingvalue"]}({g["pagemap"]["aggregaterating"][0]["ratingcount"]})</i><br>"""

            except:
                rating = ""

            thestring = f"""
            <p><a href="{g['htmlFormattedUrl']}">{g['htmlTitle']}</a><br>
            <a style="color:green;"href="{g['htmlFormattedUrl']}">{g['displayLink']}</a><br>
            {rating}
            <i style="color:grey;font-size:13px;">{g["htmlSnippet"]}</i><br>
            {image}
            
            </p><br>

            """
            output = output + thestring
        output = output + "</div>"

        return (
            """<!DOCTYPE html>
                <html lang="tr">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>K7 - RSOR</title>
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Rubik:wght@500&display=swap" rel="stylesheet">
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&display=swap" rel="stylesheet">
                    <link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@100&family=Rubik:wght@500&family=Yellowtail&display=swap" rel="stylesheet">
                    <link href="https://fonts.googleapis.com/css2?family=Parisienne&display=swap" rel="stylesheet">
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Edu+NSW+ACT+Foundation&display=swap" rel="stylesheet">
                    <link
                      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
                      rel="stylesheet"
                    />
                    <!-- Google Fonts -->
                    <link
                      href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
                      rel="stylesheet"
                    />
                    <!-- MDB -->
                    <link
                      href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.2.0/mdb.min.css"
                      rel="stylesheet"
                    />
                    <link rel="preconnect" href="https://fonts.googleapis.com">
                    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                    <link href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@300;700&display=swap" rel="stylesheet">
                </head>
                <body>

                    <br>

                    <h2>RSOR</h2>
                    <div style="width:70%;">
                    <form action="" method="POST">
                    <input type="text" name="search" placeholder="Arama Yapın" class="search" value='"""
            + search
            + """'><button>Ara</button>
                    </div>
                    </form>
                    """
            + output
            + """

                    <style>
                        h2{
                            font-family: 'Rajdhani', sans-serif;
                            color:black;
                            font-weight:300;
                            font-size:30px;
                            margin-left:30px;
                        }
                        .search{
                            padding-left:10px;
                            margin-left:30px;
                            width:70%;
                            
                        }
                        input[type="text"].search::-webkit-input-placeholder {
                            color: black;
                            font-family: 'Rajdhani', sans-serif;

                        }
                        button{
                            font-family: 'Rajdhani', sans-serif;
                            border:1px solid #000;
                            padding:3px;
                            background:none;
                            border-radius:3px;
                            width:10%;
                            padding-bottom:1px;
                            border-left:0px;

                        }
                        #result{
                            font-family:  sans-serif;
                            margin-left:30px;
                            margin-top:50px;
                            font-weight:bold;
                            color:black;
                        }
                        #wiki{
                        color:black;
                        margin-left:30px;
                        }
                        .google{
                            font-family: 'Rajdhani', sans-serif;
                            color:black;
                            font-weight:700;
                            margin:30px;
                            font-size:40px
                        }
                        .duckduck{
                        color:orange;
                        }
                    </style>


                </body>
                </html>"""
        )
