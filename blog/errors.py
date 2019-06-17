class InputError(Exception):

    @staticmethod
    def raise_error(erorr_str):
        data = {'erorr': erorr_str}
        with open('templates/tamplate_result/erorrs_returned.html', 'r') as file:
            template = file.read()
        return template, data
