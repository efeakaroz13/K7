class Templates:
    def return_index_tr():
        return"""

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
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7</p>
                <br><br>
                <br>


                    <div style="height:100%; margin-left:30px;">
                    <h2 style="font-family: 'Libre Franklin', sans-serif;">Bağımsız bilim kuruluşu </h2>
                    <p style="font-family: 'Libre Franklin', sans-serif;width:60%;">K7'nin amacı insanları doğru ve güvenilir bilgiye ulaştırmak; insanları eğitmek ve kültürlendirmektir. Her okuyucu K7'nin imkanlarını ücretsiz olarak kullanabilir. K7 hakkında daha fazla bilgi için <a href="https://cetele.pythonanywhere.com/read/K7%20ve%20ama%C3%A7lar%C4%B1">buraya</a> gözatabilirsiniz</p>
                    <i style="font-family: 'Libre Franklin', sans-serif; font-size:10px">K7'de bir şey yayımlamadan önce gönderileriniz moderatörlerimiz tarafından incelenmektedir.</i>
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
        return"""

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
        return"""

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

    def return_home_tr(username):
        return"""

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
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - """+username+"""<a style="font-size:10px;color:red;margin-left:10px;margin-bottom:4px" href="/logout">logout</a><a style="position:fixed;right:10px" href="/user/"""+username+""""><img  src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette2.wikia.nocookie.net%2Fmafiagame%2Fimages%2F2%2F23%2FUnknown_Person.png%2Frevision%2Flatest%3Fcb%3D20151119092211&f=1&nofb=1" style="border-radius:50%;width:50px;border:1px solid #000;"></a></p>
                <br><br>
                <br>
                <center>
                    <button onclick="window.location.assign('/writearticle')">Makale Yaz</button>
                </center>


                    
            </body>
            </html>

        """

    def return_register_tr():
        return"""


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
        return"""


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
        return"""


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

                            <input type="text" name="fullName" autocomplete="off" style="border:1px solid red;" placeholder="Tam adınız" class="form-control" style="width:70%;"><br>
                            <input type="text" name="birthyear"autocomplete="off" placeholder="Doğum yılınız" class="form-control" style="width:70%;" required><br>
                            <input type="text" name="city"autocomplete="off" placeholder="Yaşadığınız şehir" class="form-control" style="width:70%;" required><br>
                            <textarea  name="talents"placeholder="Yetenekleriniz(hangi konu ile alakalı olduğu size kalmış)" class="form-control" required></textarea><br>
                            <input type="password" name="password" autocomplete="off" placeholder="Şifreniz..." class="form-control" style="width:70%;" required><br>
                            <p>"""+out+"""</p>
                            <button class="btn btn-primary">Onayla</button>
                        </form>
                    </div>
                </div>
                </center>


                    
            </body>
            </html>




        """

    def return_register_done_tr(username):
        return"""


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

                    <h2>K7'ye hoş geldin """+username+""" </h2>
                    <p>Burada bilimsel yazınlarını paylaşabilir, insanlara bir şeyler katmaya çalışabilirsin.<a href="">K7 kurallar klavuzu</a>'nu başlamadan önce okumanı tavsiye ederiz!</p>
                </center>


                    
            </body>
            </html>




        """

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
        return """
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
                <p style="color:black;margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Makale Oluştur</p>
                <br><br>
                <br>
                <center>
                    
                </center>


                    
            </body>
            </html>

        """ 
