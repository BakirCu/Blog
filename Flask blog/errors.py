from flask import render_template


class InputError(Exception):

    @staticmethod
    def raise_error(erorr_str):
        return render_template('erorrs_returned.html', erorr=erorr_str)


class MySQLError(Exception):
    pass
