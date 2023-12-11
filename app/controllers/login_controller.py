from flask import redirect, url_for, flash, session
import app.models.login_model as login_model

def submit_login(request):
    if request.method == 'POST':
        usuario = request.form['usuario']
        password = request.form['password']
        
        # Insertar retroalimentación en la base de datos
        usu = login_model.submit_login_to_db(usuario, password)
        # hacer un if que si el usu esta vacio mande un mensaje de error
        # y si no que mande un mensaje de exito
        if usu:
            session['id'] = usu[0]
            session['username'] = usu[1]
            session['email'] = usu[2]
            session['cell_phone'] = usu[3]
            session['status'] = usu[5]
            session['type'] = usu[6]
            return usu
        else:
            flash('Usuario o contraseña incorrectos', 'error')
            return redirect(url_for('Index'))
        

        flash('procesamiento completado', 'success')

# funcion de cerrar session  vaciar las variables de session
def logout():
    session.clear()
    return redirect(url_for('Index'))