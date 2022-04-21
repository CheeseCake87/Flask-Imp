from ....builtins.functions.security import login_required
from ....builtins.functions.utilities import clear_message
from ....builtins.functions.utilities import clear_error
from .. import bp
from .. import struc
from .. import config
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import render_template


@bp.route("/", methods=["GET"])
def example():
    """Example of route url redirect"""
    return redirect(url_for(config["init"]["home_redirect"]))


@bp.route("/structure", methods=["GET"])
def structure():
    """
    This is an example method of rendering a template using the StructureBuilder Class
    :return:
    """
    render = "renders/render.html"
    structure = struc.name()
    extend = struc.extend("frontend.html")
    footer = struc.include("footer.html")
    error = session["error"]
    message = session["message"]

    return render_template(
        render,
        structure=structure,
        extend=extend,
        footer=footer,
        error=error,
        message=message,
        clear_error=clear_error(),
        clear_message=clear_message(),
    )


@bp.route("/local", methods=["GET"])
def local():
    """
    This is an example method of rendering a template using the local structure
    :return:
    """
    render = "renders/render.html"
    extend = "structures/base.html"
    error = session["error"]
    message = session["message"]

    # example join
    accounts = sql_do.query(Account).join(Details).all()
    for value in accounts:
        for k, v in value.__dict__.items():
            print(k)
        for ivalue in value.fk_details:
            for ik, iv in ivalue.__dict__.items():
                print(ik)

    return render_template(
        render,
        extend=extend,
        error=error,
        message=message,
        clear_error=clear_error(),
        clear_message=clear_message(),
    )


@bp.route("/login-required", methods=["GET"])
@login_required("auth", "example.login")
def locked_page():
    """
    Used to test the error catching ability of the system if a non-existent endpoint is used.
    """
    return f"""On the locked page"""


@bp.route("/no-endpoint-login-required", methods=["GET"])
@login_required("auth", "nothere")
def locked_page_no_endpoint_redir():
    """
    Used to test the error catching ability of the system if a non-existent endpoint is used.
    """
    return f"""On the locked page"""


@bp.route("/logout", methods=["GET", "POST"])
def logout():
    session["example1_auth"] = False
    return redirect(url_for("example1.login"))


@bp.route("/login", methods=["GET", "POST"])
def login():
    """
    Used to test the session set for the login_required decorator.
    """
    if request.method == "POST":
        session["auth"] = True
        return redirect(url_for("example1.account"))

    print(session)
    return f""" 
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
<form method='post'>
<input type='submit' value='login'/>
</form>
</body>
</html>
    """


@bp.route("/account", methods=["GET"])
@login_required("auth", "example1.login")
def account():
    """
    This page is protected by the login_required decorator, with the login page endpoint set.
    """
    return f"""Account Page {session}"""
