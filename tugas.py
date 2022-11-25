from flask import Flask, render_template, request, redirect
import mysql.connector
# inisialisasi
alfin = Flask(__name__)

# database
db = mysql.connector.connect(
    host = 'localhost',
    port = 3306, 
    user = 'root',
    passwd = '',
    database = 'list_mahasiswa'
)

# routing = jalur
@alfin.route('/')
def home():
    return render_template('home.html')

@alfin.route('/login')
def login():
    return render_template('login.html')

@alfin.route('/list')
def list_mhs():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tb_mahasiswa")
    result = cursor.fetchall()

    return render_template('list_mhs.html', data=result)

@alfin.route('/input', methods = ['GET','POST'])
def input():
    if request.method == 'POST':
        data = request.form
        nama = data ['nama']
        nim = data ['nim']
        alamat = data ['alamat']

        cursor = db.cursor()
        query = f"INSERT INTO tb_mahasiswa (nama, nim, alamat) VALUES ('{nama}','{nim}','{alamat}')"

        cursor.execute(query)
        db.commit()

        return redirect('/list', code = 302, Response = None)

    return render_template('input.html') 


@alfin.route('/hapus/<id>')
def HapusMhs(id):
    cursor = db.cursor()
    query = f"DELETE FROM tb_mahasiswa WHERE id='{id}'"
    cursor.execute(query)
    db.commit()


    return redirect('/list', code = 302, Response = None)


if __name__ == '__main__':
    alfin.run()
