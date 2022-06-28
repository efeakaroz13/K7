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
                <p style="margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7</p>
                <br><br>
                <br>


                    <div style="height:100%; margin-left:30px;">
                    <h2 style="font-family: 'Libre Franklin', sans-serif;">Bağımsız basın ve bilim paylaşım platformu </h2>
                    <p style="font-family: 'Libre Franklin', sans-serif;width:60%;">K7'nin amacı her bir kullanıcısını doğru ve güvenilir bilgiye ulaştırmak; insanları eğitmek ve kültürlendirmektir. Her okuyucu K7'nin imkanlarını ücretsiz olarak kullanabilir.</p>
                    <i style="font-family: 'Libre Franklin', sans-serif; font-size:10px">K7'de bir şey yayımlamadan önce gönderileriniz moderatörlerimiz tarafından incelenmektedir.</i>
                    </div>

                <br><br>

                <br><br><br>
              

                
                <br><br>
                <center>
                <div style="border:1px solid #000;border-radius:5px;padding:30px;width:70%;">
                    <h3></h3>
                    <button class="btn btn-dark" onclick="window.location.assign('/login')">Giriş Yap</button>
                    <button class="btn btn-outline-dark">Kayıt Ol</button>
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
                <p style="margin:10px;font-size:20px;font-family: 'Rubik', sans-serif;" onclick="window.location.assign('/')">K7 - Giriş Yap</p>
                <br><br>
                <br>
                <center>
                <div class="card" style="width:80%; padding:30px">
                    <div class="card-body>
                        <h4 class="card-title" style="font-size:25px;">Giriş yap</h4><br><br>
                        <form class="card-text">
                            <input type="text" autocomplete="off" autocapitalize="off" name="username" placeholder="Kullanıcı Adı..." class="form-control" style="width:70%;margin-bottom:20px;">
                            <input type="password" autocomplete="off" autocapitalize="off" name="password" placeholder="Şifre..." class="form-control" style="width:70%;">
                        </form>
                    </div>
                </div>
                </center>


                    
            </body>
            </html>

        """