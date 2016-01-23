
from flask import Flask, url_for, render_template, request, \
    redirect, abort, session, g, flash, Markup
import helpers
from abapi import helpers
from abapi import app

@app.route('/event', defaults={"path": ""})
@app.route('/event/<path:whatever>')
def event_listener(whatever):
    app.logger.info(whatever)
    """
    The format of the URL should be something like 

    - SessionID: GUID (or a string for the purpose of this demo)
    - Timestamp: Int. The unix timestamp in the client
    - Client Version: String. Something to identify the version/kind/variation of the client
    - Item: String. The thing that the user has touched. 

    In this order, and validating a bit
    """
    (sesid, stamp, client, item) = parse_request(whatever)
    assert sessionid_check(sesid) is not False
    assert stamp_check(stamp) is not False
    assert client_check(client) is not False
    assert item_check(item) is not False
    return "{0} registered".format(whatever)


@app.route('/')
def index():
    return render_template("base.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

