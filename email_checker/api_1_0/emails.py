import re
import json
from email_checker.api_1_0 import api
from flask import request, jsonify, render_template, g


def unique_email_nums(emails_dict):
    type_emails = []
    names = []
    count = 0
    for email in emails_dict.values():
        is_valid = re.match(r"([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$", email)
        if is_valid:
            name = name_match(is_valid.group(1))
            type_email = is_valid.group(2)
            if type_email not in type_emails:
                type_emails.append(type_email)
                count += 1
                names.append(name)
            elif name not in names:
                names.append(name)
                count += 1
        else:
            print("email address invalid")
    return count


def name_match(name):
    ans = ""
    if not name:
        return ans
    for char in name:
        if char != ".":
            if char == '+':
                return ans
            ans += char
    return ans


count = 0


@api.route('/index', methods=['POST'])
def index():
    global count
    emails_json = request.get_json()
    # print(emails_json)
    if emails_json:
        emails_json = request.get_json()
        # print(emails_json)
        count = unique_email_nums(emails_json)
        print(count)
        return jsonify(errno=0, errmsg="commit email success")
    else:
        return jsonify(errno=1, errmsg="none email")


@api.route('/emails')
def check():
    global count
    return render_template('total.html', count=count)
